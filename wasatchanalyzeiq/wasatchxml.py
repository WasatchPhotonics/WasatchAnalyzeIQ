""" wasatchxml - Classes to Acquire data from Wasatch Photonics
spectrometers, write out in xml format for use in AnalyzeIQ. Designed to
be used as part of the WasatchDevice script.
"""

import sys
import numpy
import logging
import datetime
from PyQt4 import QtGui, QtCore
from string import Template

from wasatchanalyzeiq.ui.AnalyzeIQLayout import Ui_MainWindow
from wasatchusb.camera import SimulatedUSB
from wasatchusb.camera import CameraUSB
from wasatchusb.utils import FindDevices

log = logging.getLogger(__name__)

class WasatchXML(QtGui.QMainWindow):
    
    def __init__(self):
        super(WasatchXML, self).__init__()

        self.generated_xml_str = "invalid"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupSignals()
 
        self.ui.lcdNumber.setVisible(False)
        self.countdown_interval = 10
       
        self.set_device() 
        self.show()

    def setupSignals(self):
        """ Create signals and slots 
        """
        self.ui.toolButtonAcquire.clicked.connect(self.acquire)

    def set_device(self, device=None):
        """ If no external device is specified, find the first device on
        the usb bus, connect. The external device assumes that it has
        already been setup. This is for assigning devices during the
        tests.
        """
        if device is not None:
            self.device = device

        else:
            self.device = self.find_first_device_or_simulate()

        self.ui.labelDeviceText.setText("Connected to %s" %
            self.device.serial_number)

        return True

    def find_first_device_or_simulate(self):
        simulated_device = SimulatedUSB()
        try:
            fd = FindDevices()
            result, usb_info = fd.list_usb()
            log.debug(" USB ID strings: %s" % usb_info[0])
            (vid, pid) = usb_info[0].split(':')[0:2]
        except:
            log.debug("Error find devices: %s" % str(sys.exc_info()))
            

        try:
            real_device = CameraUSB()
            log.debug("Attempt real device connection")
            if real_device.connect(9386, pid):
                log.debug("Succesfull connection to: %s" % pid)
                return real_device
        except:
            log.debug("Exception %s" % str(sys.exc_info()))
            pass

        log.debug("Return simulated device")
        simulated_device.assign("Stroker785L")
        simulated_device.serial_number = "Simulated Stroker785L"
        return simulated_device            

    def acquire(self):
        """ Connect to the device, acquire a spectra, send the pixel
        results to the build xml function.
        """
        log.debug("acquire")       
        self.apply_coefficients()
        int_time = self.ui.spinBoxIntegrationTime.value()
        self.device.set_integration_time(int_time)

        laser = self.ui.checkBoxLaserEnable.isChecked()
        self.device.set_laser_enable(laser)

        log.debug("call get line wavenumber")
        wavenum_axis, intensity_data = self.device.get_line_wavenumber()
        self.build_xml(wavenum_axis, intensity_data)

        self.delay_close()


    def delay_close(self):
        """ Set the delay close timer to the integration time plus a
        margin, show the status with the lcdNumber countdown timer, and 
        exit the program when the timer is done.
        """
        exit_margin = 100
        int_time = self.ui.spinBoxIntegrationTime.value() 
        exit_wait = int_time + exit_margin
        self.closeTimer = QtCore.QTimer()
        self.closeTimer.timeout.connect(self.close)
        self.closeTimer.start(exit_wait)

        self.ui.lcdNumber.display(int_time)
        self.countdownTimer = QtCore.QTimer()
        self.countdownTimer.timeout.connect(self.update_lcd_display)
        self.countdownTimer.start(10)

        # Attempt to turn the laser off
        try:
            self.device.set_laser_enable(False)
        except:
            log.debug("Problem disabling laser")
                   

    def update_lcd_display(self):
        """ Show the current countdown information.
        """
        curr_value = self.ui.lcdNumber.value()
        curr_value -= self.countdown_interval
        if curr_value > 0:
            self.ui.lcdNumber.setVisible(True)
            self.ui.lcdNumber.display(curr_value)
            self.countdownTimer.start(10)
         
    def apply_coefficients(self): 
        # Make sure any changes to the coefficients are applied
        coeff_dict = {"C0": float(self.ui.lineEditCoeff0.text()),
                      "C1": float(self.ui.lineEditCoeff1.text()),
                      "C2": float(self.ui.lineEditCoeff2.text()),
                      "C3": float(self.ui.lineEditCoeff3.text())
                     }
        self.device.new_coefficients(coeff_dict)


    def build_xml(self, x_data, y_data):
        """ Use python string template to build the AnalyzeIQ xml output
        file. Uses the AIQ_TEMPLATE at the end of this file.
        """
        xml = Template(AIQ_TEMPLATE)

        ts = datetime.datetime.now()
        date_str = ts.strftime("%m/%d/%Y")
        time_str = ts.strftime("%H:%M:%S")
        scanduration = self.ui.spinBoxIntegrationTime.value()

        space_x_data = ""
        faker_x = 0
        for item in x_data:
            space_x_data += "%s " % (item + faker_x)
            faker_x += 0

        space_y_data = ""
        for item in y_data:
            space_y_data += "%s " % item

        populated = {"datestamp": date_str,
                     "timestamp": time_str,
                     "scanduration": scanduration,
                     "comment": "Wasatch Photonics Device",
                     "dim_x" : space_x_data,
                     "dim_y" : space_y_data
                    }

        self.generated_xml_str = xml.safe_substitute(populated)

    def last_xml_output(self):
        """ Make sure all of the timers are forced stop if the program is
        exited, catch the exceptions if they have not been created.
        """

        try:
            self.closeTimer.stop()
        except:
            pass

        try:
            self.countdownTimer.stop()
        except:
            pass

        return self.generated_xml_str

AIQ_TEMPLATE = """<?xml version="1.0" encoding="iso-8859-1"?>
<AIQ version="1.0">
    <experiment type="Raman" language="en-us">
      <file>
         <title>Data from Wasatch Photonics device</title>
      </file>
      <instrument>
         <instrumentDescription>
            <instrumentDesignation>
               <identifier></identifier>
               <manufacturer>Wasatch Photonics</manufacturer>
               <model>Stroker Spectrometer</model>
            </instrumentDesignation>
            <instrumentApplication>
               <software>wasatch_inst.exe</software>
               <version>1.0</version>
               <operatingSystem>Windows 7</operatingSystem>               
            </instrumentApplication>
         </instrumentDescription>
         <instrumentProperty>
            <instrumentSetting>
               <resolution unit="cm-1">10</resolution>
			   <excitationline unit="nm">785</excitationline>
			   <detectorTypes>CCD linear detector</detectorTypes>
            </instrumentSetting>
         </instrumentProperty>
      </instrument>
      <measurement>
         <measurementDescription >
            <measurementExecution>
               <timeStamp>
                  <date>$datestamp</date>
                  <time>$timestamp</time>
               </timeStamp>
               <operator>
                  <name>WasatchAnalyzeIQ</name>
               </operator>
            </measurementExecution>
         </measurementDescription>
         <measurementProperty>
            <measurementParameter>
                <scanDuration unit="ms">$scanduration</scanDuration>
                <comment>$comment</comment>
            </measurementParameter>
        </measurementProperty>
      </measurement>
      <data>
         <dataProperty>
            <dataParameter>
			<axisLabel>                  
				<axis dim="x">Raman Shift</axis>                  
				<axis dim="y">Intensity</axis>               
			</axisLabel>               
			<axisUnit>                  
				<axis dim="x">cm-1</axis>                  
				<axis dim="y">Arbitrary</axis>               
			</axisUnit>            
            </dataParameter>
         </dataProperty>
         <dataCore>
		<values dim = "x">
			$dim_x
		</values>            
		<values dim = "y">
			$dim_y
		</values>         
         </dataCore>
      </data>
   </experiment>
</AIQ>
"""

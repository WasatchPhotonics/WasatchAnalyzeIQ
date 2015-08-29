""" Tests for wasatchxml gui
"""

import unittest

from PyQt4 import QtGui, QtTest, QtCore

from wasatchanalyzeiq import wasatchxml
from wasatchusb.camera import SimulatedUSB

class Test(unittest.TestCase):

    def setUp(self):
        self.app = QtGui.QApplication([])
        self.form = wasatchxml.WasatchXML()

    def tearDown(self):
        # This may help with segfaults
        self.app.closeAllWindows()

    def test_startup_layout(self):
        # window is correct size
        self.assertEqual(self.form.width(), 622)
        self.assertEqual(self.form.height(), 302)
        
        # Basic controls are available
        fui = self.form.ui
        self.assertTrue(fui.checkBoxLaserEnable.isVisible())
        self.assertTrue(fui.checkBoxLaserEnable.isEnabled())

        # Lcd number is invisible
        self.assertFalse(self.form.ui.lcdNumber.isVisible())

        # wasatch logo is present
        self.assertTrue(fui.labelLogo.isVisible())

        # Acquire and cancel buttons are available
        self.assertTrue(fui.toolButtonAcquire.isVisible())
        self.assertTrue(fui.toolButtonCancel.isVisible())

    def test_control_limits(self):
        fui = self.form.ui

        # Laser enable starts off unchecked, can be checked
        self.assertFalse(fui.checkBoxLaserEnable.isChecked())

        clk = QtTest.QTest.mouseClick

        clk(fui.checkBoxLaserEnable, QtCore.Qt.LeftButton)
        self.assertTrue(fui.checkBoxLaserEnable.isChecked())

        # Integration time is 10-60000
        # Try setting outside of low and high range, make sure it
        # doesn't deviate from default '10'
       
        spb = self.form.ui.spinBoxIntegrationTime 
        self.assertEqual(spb.value(), 100)
        
        spb.setValue(60001)
        self.assertEqual(spb.value(), 60000)

        spb.setValue(900000)
        self.assertEqual(spb.value(), 60000)

        spb.setValue(-1)
        self.assertEqual(spb.value(), 10)
        
        spb.setValue(9)
        self.assertEqual(spb.value(), 10)

        # Set it to a common value, make sure it takes
        spb.setValue(100)
        self.assertEqual(spb.value(), 100)

    def test_xml_output(self):
        # Click the acquire button, read from the last generated xml
        # output variable 
        xml_output = self.form.last_xml_output()
        self.assertEqual(xml_output, "invalid")

        # Simulated device is rquired
        sim_device = SimulatedUSB()
        sim_device.assign("Stroker785L")
        self.assertTrue(self.form.set_device(sim_device))

        QtTest.QTest.mouseClick(self.form.ui.toolButtonAcquire,
            QtCore.Qt.LeftButton)
        xml_output = self.form.last_xml_output()

        head_str = "<title>Data from Wasatch Photonics device</title>"
        self.assertTrue(head_str in xml_output)

        self.assertTrue("$datestamp" not in xml_output)
        self.assertTrue("$timestamp" not in xml_output)

        # Make sure none of the python string template tags persist in
        # the xml output - check for $ which as of this writing only
        # appears in the python template tag areas
        self.assertFalse("$" in xml_output)

    def test_acquire_closes_window(self):
        # Simulated device is rquired
        sim_device = SimulatedUSB()
        sim_device.assign("Stroker785L")
        self.assertTrue(self.form.set_device(sim_device))
        self.form.ui.spinBoxIntegrationTime.setValue(3000)

        QtTest.QTest.mouseClick(self.form.ui.toolButtonAcquire,
            QtCore.Qt.LeftButton)
        xml_output = self.form.last_xml_output()

        QtTest.QTest.qWait(3000)
        self.assertFalse(self.form.isVisible())

    def test_wavenumber_translation(self):
        # Create a simulation device, assign it to the device in the
        # application
        sim_device = SimulatedUSB()
        self.assertTrue(sim_device.assign("Stroker785L"))

        # Assign the calibration coefficients
        self.form.ui.lineEditCoeff0.setText("7.25405E+02")
        self.form.ui.lineEditCoeff1.setText("1.43880E-01")
        self.form.ui.lineEditCoeff2.setText("7.16617E-06")
        self.form.ui.lineEditCoeff3.setText("-8.68137E-09")

        self.assertTrue(self.form.set_device(sim_device))
        # Click the acquire button, expect the Y axis to match the
        # wavenumbers specified by the calibration coefficients
        QtTest.QTest.mouseClick(self.form.ui.toolButtonAcquire,
            QtCore.Qt.LeftButton)
        xml_output = self.form.last_xml_output()

        xval = xml_output.split("dim = \"x\">")[1]
        xval = xval.split(" \n\t\t</values>")[0]
        xval = xval.replace('\n\t\t\t', '') # remove prefix
        xaxis_data = xval.split(' ')

        first_conv = "-1046.55"
        last_conv = "12738.79"
        self.assertEqual("%05.2f" % float(xaxis_data[0]), first_conv)
        self.assertEqual("%05.2f" % float(xaxis_data[-1]), last_conv)

    def test_device_status_displayed(self):
        # Create a simulation device, set in form, make sure the device
        # label updates
        sim_device = SimulatedUSB()
        sim_device.assign("Stroker785L")

        self.assertEqual(self.form.ui.labelDeviceText.text(), 
            "Searching for device...")

        self.assertTrue(self.form.set_device(sim_device))
        self.assertEqual(self.form.ui.labelDeviceText.text(), 
            "Connected to Stroker785L")
    
    def test_long_integration_feedback(self):
        # Set the lcdnumber to a known value
            
        # Trigger the acquisition

        # make sure halfway through the numbers are in range

        # After the total integration time has passed, make sure the box
        # says zero
        pass

if __name__ == "__main__":
    unittest.main()

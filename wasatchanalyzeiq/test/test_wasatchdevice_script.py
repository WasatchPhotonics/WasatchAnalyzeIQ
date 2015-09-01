""" WasatchDevice.py tests for the command line script that is in turn
called by analyze iq.
"""

import unittest

from scripts import wasatchdevice

from PyQt4 import QtGui

app = QtGui.QApplication([])

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_command_line_options(self):
        # Accept one option, auto - which auto closes the box
        wsdapp = wasatchdevice.WasatchDeviceApplication() 
         
        args = wsdapp.parse_args(["-a", "-t"])
        self.assertIsNotNone(args.auto_capture)


    def test_scripts_main(self):
        # Enter no command line options, expect it to operate
        result = wasatchdevice.main()
        self.assertEquals(0, result)

        bad = "C:\Analyze IQ V2\Common\InstrumentData\11-" \
              + "WasatchPhotonicsStroker_0"
        result = wasatchdevice.main(bad)
        self.assertEquals(0, result)

    def test_auto_close(self):
        # Enter a valid set of command line options, expect success
        result = wasatchdevice.main(["unittest", "-a", "-t"])
        self.assertEquals(0, result)
        
#usage: wasatch_inst.exe [-h] [-a] [-t]
#wasatch_inst.exe: error: unrecognized arguments: C:\Analyze IQ V2\Common\InstrumentData\11-WasatchPhotonicsStroker_0
#Traceback (most recent call last):


if __name__ == "__main__":
    unittest.main()

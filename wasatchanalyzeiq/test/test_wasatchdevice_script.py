""" WasatchDevice.py tests for the command line script that is in turn
called by analyze iq.
"""

import unittest

from scripts import wasatchdevice

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_command_line_options(self):
        # Accept one option, auto - which auto closes the box
        wsdapp = wasatchdevice.WasatchDeviceApplication() 
         
        args = wsdapp.parse_args(["-a", "-t"])
        self.assertIsNotNone(args.auto_capture)


    def test_scripts_main(self):
        result = wasatchdevice.main()
        self.assertEquals(2, result)

        result = wasatchdevice.main(["unittest", "-a", "-t"])
        self.assertEquals(0, result)
        


if __name__ == "__main__":
    unittest.main()

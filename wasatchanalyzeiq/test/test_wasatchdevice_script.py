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
         
        args = wsdapp.parse_args(["-a"])
        self.assertIsNotNone(args.auto_capture)


    def test_scripts_main(self):
        result = wasatchdevice.main(["-a"])
        self.assertEquals(0, result)
        

        # if it starts at all, it returns at least a simulation device

    def test_with_gui_main(self):
        # create the qtapp requirements, use the testing flag to
        # instruct the visualize app not to recreate it
        self.add_known_group(["3"])
        proc = broaster.ProcessBroaster()

        self.app = QtGui.QApplication([])

        # Run with no args, expect error code 
        result = visualize.main()
        self.assertEquals(2, result)

        # Specify a non-existent graph type, expect error code
        argv = ["unittest exec", "-n", self.node_root, "-g", "badg"]
        result = visualize.main()
        self.assertEquals(2, result)
        
        # Run with correct arguments, in test mode, should be no error
        # code
        argv = ["unittest exec", "-n", self.node_root, "-t"]
        result = visualize.main(argv)
        self.assertEquals(0, result)

        # Run with explicitly stated gaps graph type
        argv = ["unittest exec", "-n", self.node_root, "-t", 
                "-g", "gaps"
               ]
        result = visualize.main(argv)
        self.assertEquals(0, result)

        # Run with heatmap graph type
        argv = ["unittest exec", "-n", self.node_root, "-t", 
                "-g", "heatmap"
               ]
        result = visualize.main(argv)
        self.assertEquals(0, result)


if __name__ == "__main__":
    unittest.main()

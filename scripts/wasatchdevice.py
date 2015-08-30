""" wasatchdevice - command line application to read from a wasatch
photonics device and return data on stdout. Designed to be called from
the AnalyzeIQ product. Produces xml output on stdout.
"""

import sys
import argparse

from PyQt4 import QtGui

class WasatchDeviceApplication(object):
    """ Wrapper around application control code based on:
    https://groups.google.com/d/msg/comp.lang.python/j_tFS3uUFBY/\
        ciA7xQMe6TMJ
    Specifically, this means breaking out all of the functions from main
    into this application object so they can have a narrow interface,
    suitable for unit testing.
    """
    def __init__(self):
        super(WasatchDeviceApplication, self).__init__()
        self.parser = self.create_parser()

    def parse_args(self, argv):
        print "Full parse args: [%s]" % argv
        self.args = self.parser.parse_args(argv)
        return self.args

    def create_parser(self):
        desc = "wasatch device acquisition, xml stdout for AnalyzeIQ"
        parser = argparse.ArgumentParser(description=desc)
    
        parser.add_argument("-a", "--auto-capture", action="store_true",
            help="Automatically acquire after startup")
    
        return parser

    def run(self):
        """ Create the Qt application if required, execute the specific
        processing collation steps for the designated graph mode. Then
        exit with the app.exec if the unittest has not created the qt 
        application.
        """

       # if not self.args.testing:
       #     app = QtGui.QApplication(sys.argv)
            
        app = QtGui.QApplication(sys.argv)

        print "Need auto click"

        #if not self.args.testing:
            #sys.exit(app.exec_())
        sys.exit(app.exec_())


def main(argv=None): 
    """ main calls the wrapper code around the application objects with
    as little framework as possible. See:
    https://groups.google.com/d/msg/comp.lang.python/j_tFS3uUFBY/\
        ciA7xQMe6TMJ
    """
    
    if argv is None: 
        from sys import argv as sys_argv 
        argv = sys_argv 
    else:
        # Strip out the program name to match the unittest setup
        argv = argv[1:]

    exit_code = 0
    try:
        wsdapp = WasatchDeviceApplication()
        wsdapp.parse_args(argv)
        wsdapp.run()
    except SystemExit, exc:
        exit_code = exc.code

    return exit_code 

if __name__ == "__main__":
    sys.exit(main(sys.argv))



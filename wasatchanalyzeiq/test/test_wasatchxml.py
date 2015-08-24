""" Tests for wasatchxml gui
"""

import unittest

from PyQt4 import QtGui, QtTest

from wasatchanalyzeiq import wasatchxml

class Test(unittest.TestCase):

    def setUp(self):
        self.app = QtGui.QApplication([])
        self.form = wasatchxml.WasatchXML()

    def tearDown(self):
        # This may help with segfaults
        self.app.closeAllWindows()

    def test_startup_layout(self):
        # window is correct size
        self.assertEqual(self.form.width(), 496)
        self.assertEqual(self.form.height(), 302)
        
        # Basic controls are available
        fui = self.form.ui
        self.assertTrue(fui.checkBoxLaserEnable.isVisible())
        self.assertTrue(fui.checkBoxLaserEnable.isEnabled())

        # Lcd number is invisible
        self.assertFalse(self.form.ui.lcdNumber.isVisible())

    def test_control_limits(self):
        fui = self.form.ui

        # Laser enable starts off unchecked
        self.assertFalse(fui.checkBoxLaserEnable.isChecked())
    
    #def test_xml_output(self):
    #def test_long_integration_feedback(self):
if __name__ == "__main__":
    unittest.main()

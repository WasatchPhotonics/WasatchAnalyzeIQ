""" Tests for wasatchxml gui
"""

import unittest

from PyQt4 import QtGui, QtTest, QtCore

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

    #def test_xml_output(self):
    #def test_long_integration_feedback(self):
if __name__ == "__main__":
    unittest.main()

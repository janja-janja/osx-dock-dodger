from unittest import TestCase
from ..dock_dodger import OSXDodger


class OSXDockDodgerTests(TestCase):
    def test_applications_folder_is_correct(self):
        """
        Test that the applications folder is
        indeed `/Applications/`
        """
        expected = "/Applications/"
        result = OSXDodger().app_dir
        self.assertEqual(result, expected)

    def test_allowed_system_is_mac(self):
        """
        Allowed system to run this script should be
        a machine running on OS X
        """
        expected = "darwin"
        result = OSXDodger().allowed_sys
        self.assertEqual(result, expected)

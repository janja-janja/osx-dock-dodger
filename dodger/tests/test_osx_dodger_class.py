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

    def test_allowed_version_is_10_6_1(self):
        """
        Test that the actual OS X version is 10.6.1
        """
        test_value = "10.6.1"
        expected = True
        result = OSXDodger().os_version(test_value)
        self.assertEqual(result, expected)

    def test_allowed_version_is_greater_than_10_6_1(self):
        """
        Test that the actual OS X version is greater than 10.6.1
        """
        test_value = "10.11.1"
        expected = True
        result = OSXDodger().os_version(test_value)
        self.assertEqual(result, expected)

    def test_allowed_version_is_less_than_10_6_1(self):
        """
        Test that the actual OS version is less than 10.6.1
        """
        test_value = "10.5.9"
        expected = False
        result = OSXDodger().os_version(test_value)
        self.assertEqual(result, expected)

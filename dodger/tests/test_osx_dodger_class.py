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

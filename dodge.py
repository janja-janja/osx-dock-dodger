import platform


class OSXDodger(object):
    allowed_version = "10.12.1"

    def __init__(self, applications_dir):
        self.app_dir = applications_dir

    def load_applications(self):
        """
        Read all applications in the `/Applications/` dir
        """
        self.pc_is_macintosh()

    def select_applications(self):
        """
        Allow user to select an application they want
        not to appear on the Dock
        """
        pass

    def load_dodger_filer(self):
        """
        Load the file to modify for the application
        chosen by the user in `select_applications`

        The file to be loaded for is `info.plist`
        """
        pass

    def dodge_application(self):
        """
        Remive the application from the Dock
        """
        pass

    @classmethod
    def pc_is_macintosh(cls):
        """
        Check if it is an `Apple Computer` i.e a Mac
        @return bool
        """
        system = platform.system().lower()
        sys_version = int((platform.mac_ver())[0].replace(".", ""))
        allowed_version = int(cls.allowed_version.replace(".", ""))

        if (system == "darwin") and (sys_version >= allowed_version):
            return True
        else:
            print("\nSorry :(")
            print("FAILED. OsX-dock-dodger is only applicable to computers " +
                  "running OS X {} or higher".format(cls.allowed_version))
            return False

dodge = OSXDodger("/Applications/")
dodge.load_applications()

import platform
import time
import os


class BaseColors(object):
    """
    Holds color codes to be used in the `terminal`
    """
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDCOLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class OSXDodger(BaseColors):
    allowed_version = "10.6.1"
    allowed_system = "darwin"
    system_files = [".DS_Store", ".localized"]

    def __init__(self, applications_dir):
        self.app_dir = applications_dir

    def load_applications(self):
        """
        Read all applications in the `/Applications/` dir
        """
        if self.pc_is_macintosh():
            all_apps = os.listdir(self.app_dir)
            print(self.GREEN + "Loading applications..." + self.ENDCOLOR)
            time.sleep(1)

            print(self.WARNING + "\n\nAPP NUMBER\t\tAPPLICATION NAME" +
                  self.ENDCOLOR)

            for index, app in enumerate(all_apps):
                if app not in self.system_files:
                    print (index + 1), "\t\t\t" + app.replace(".app", "")

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

        if (system == cls.allowed_system) and (sys_version >= allowed_version):
            return True
        else:
            print("\nSorry :(")
            print("FAILED. OsX-dock-dodger is only applicable to computers " +
                  "running OS X {} or higher".format(cls.allowed_version))
            return False

dodge = OSXDodger("/Applications/")
dodge.load_applications()

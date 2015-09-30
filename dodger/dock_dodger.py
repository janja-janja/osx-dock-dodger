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
    def __init__(self):
        self.app_dir = "/Applications/"
        self.allowed_version = "10.6.1"
        self.allowed_sys = "darwin"
        self.system_files = [".DS_Store", ".localized"]

    def load_applications(self):
        """
        Read all applications in the `/Applications/` dir
        """
        if self.pc_is_macintosh():
            all_apps = os.listdir(self.app_dir)
            print(self.GREEN + "Loading applications..." + self.ENDCOLOR)
            time.sleep(1)

            print(self.WARNING + "\n\nAPP NUMBER\t\t\tAPPLICATION NAME" +
                  self.ENDCOLOR)

            for index, app in enumerate(all_apps):
                if app not in self.system_files:
                    seperator = "-------------------->"
                    tabs = "\t"
                    print (index + 1), tabs + seperator + tabs + \
                        app.replace(".app", "")

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

    def pc_is_macintosh(self):
        """
        Check if it is an `Apple Computer` i.e a Mac
        @return bool
        """
        system = platform.system().lower()

        if (system == self.allowed_sys) and (self.check_os_version()):
            return True
        else:
            print("\nSorry :(")
            print("FAILED. OsX-dock-dodger is only applicable to computers " +
                  "running OS X {} or higher".format(self.allowed_version))
            return False

    def check_os_version(self):
        """
        Check that the OS X version meets the requiredments
        """
        sys_version = int((platform.mac_ver())[0].replace(".", ""))
        allowed_version = int(self.allowed_version.replace(".", ""))

        if sys_version >= allowed_version:
            return True
        else:
            return False

dodge = OSXDodger()
dodge.load_applications()

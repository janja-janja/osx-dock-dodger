#!/usr/bin/env python
"""
Hide a running application from showing on the dock.
The application runs as a daemon i.e in the background
"""
import platform
import time
import os


class BaseColors(object):
    """
    Holds color codes to be used in the `terminal`
    """
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    RED = "\033[91m"
    ENDCOLOR = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


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
            self.all_apps = os.listdir(self.app_dir)
            print(self.GREEN + "Loading applications..." + self.ENDCOLOR)
            time.sleep(1)

            print(self.WARNING + "\n\nAPP NUMBER\t\t\tAPPLICATION NAME" +
                  self.ENDCOLOR)

            for self.index, app in enumerate(self.all_apps):
                if app not in self.system_files:
                    seperator = "-------------------->"
                    tabs = "\t"
                    print (self.index), tabs + seperator + tabs + \
                        app.replace(".app", "")

    def select_applications(self):
        """
        Allow user to select an application they want
        not to appear on the Dock
        """
        # load applications
        self.load_applications()

        print(self.BOLD)
        print("\nPlease choose an application to hide from the dock.\n(Enter "
              "the application number provided on the left hand side)")
        print(self.ENDCOLOR)

        done = True
        while done:
            selected_app_number = raw_input(self.RED + ">>> " + self.ENDCOLOR)
            try:
                selected_app_number = int(selected_app_number)
                if selected_app_number < 2 or selected_app_number > self.index:
                    # system dot files (<2)
                    # unavailable applications (>self.index)
                    print("That app doesn't exist. Please enter a number"
                          "between 2 and {0}".format(self.index))
                else:
                    done = False

            except ValueError:
                print("Please enter a number between 2"
                      " and {0}".format(self.index))

        selected_app = self.all_apps[selected_app_number].replace(".app", "")
        print("Are you sure you want to hide " + self.RED + "{}"
              .format(selected_app.upper() + self.ENDCOLOR + " from the Dock?")
              )
        # access the dir holding the selected application
        directory = "{0}{1}.app/".format(self.app_dir, selected_app)

        try:
            os.chdir(directory)
        except OSError:
            print("Failed to to dock dodge :(")

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
        sys_version = platform.mac_ver()[0]
        if (system == self.allowed_sys) and (self.os_version(sys_version)):
            return True
        else:
            print("\nSorry :(")
            print("FAILED. OsX-dock-dodger is only applicable to computers " +
                  "running OS X {} or higher".format(self.allowed_version))
            return False

    def os_version(self, sys_version):
        """
        Check that the OS X version meets the requiredments
        """
        sys_version = int((sys_version).replace(".", ""))
        allowed_version = int(self.allowed_version.replace(".", ""))

        return (sys_version >= allowed_version)

dodge = OSXDodger()
dodge.select_applications()

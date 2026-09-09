import configparser
import os


class DotDrop:

    def __init__(self):

        self.USER_DEFAULT_CONFIG = """[paths]
        log_file = "~/.config/DotDrop/log.txt"
        """

        self.USER_CONFIG_PATH = '~/.config/DotDrop/'
        self.USER_CONFIG_FILE = 'config.ini'

    def CheckConfigExists(self):

        if !(os.isdir(self.USER_CONFIG_FILE)):
            os.mkdir(self.USER_CONFIG_FILE)

        if !(os.isfile(self.USER_CONFIG_PATH+self.USER_CONFIG_FILE)):
            with open(self.USER_CONFIG_PATH+self.USER_CONFIG_FILE) as f:
                f.wite(self.USER_DEFAULT_CONFIG)

from LogIt import LogIt

import configparser
import os
from pathlib import Path


class DotDrop:

    def __init__(self):

        self.USER_DEFAULT_CONFIG = """[paths]
log_file = ~/.config/DotDrop/log.txt

        """

        LOG_LEVELS = {'info': '',
                      'warning': 'WARN',
                      'user_error': '!MISS',
                      'program_error': '! ERROR !'}

        LINE_FORMAT = '[{session_name}] {time_date} | {level} --> {message}'


        self.USER_CONFIG_DIR = str(Path('~/.config/DotDrop/').expanduser()) + '/'
        print(self.USER_CONFIG_DIR)
        self.USER_CONFIG_FILE = 'config.ini'

        if self.CheckConfigExists():

            self.config = configparser.ConfigParser()
            self.config.read(self.USER_CONFIG_DIR+self.USER_CONFIG_FILE)

            print(self.GetLogFile())

            log = LogIt(log_file=self.GetLogFile(), levels=LOG_LEVELS)
            log.SetFormats(text_format=LINE_FORMAT)
            if log.TestFormating(test_data={'session_name': '123', 'time_date': log.GetTimeViaFormat(), 'level': '', 'message': 'testing'}):
                log.WriteStartLine(line='<<< ================== {session_name} ================== >>>', data={'session_name': log.data['session_name']})


    def CheckConfigExists(self):

        try:
            if not (os.path.isdir(self.USER_CONFIG_DIR)):
                os.mkdir(self.USER_CONFIG_DIR)

            if not (os.path.isfile(self.USER_CONFIG_DIR+self.USER_CONFIG_FILE)):
                with open(self.USER_CONFIG_DIR+self.USER_CONFIG_FILE, 'w') as f:
                    f.write(self.USER_DEFAULT_CONFIG)

        except Exception as e:
            print(e)
        else:
            return True


    def GetLogFile(self):
        return Path(self.config['paths']['log_file']).expanduser()

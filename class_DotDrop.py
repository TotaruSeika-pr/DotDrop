from LogIt import LogIt
from ArgumentParser import ArgumentParser

import configparser
import os
from pathlib import Path


class DotDrop:

    def __init__(self):

        self.USER_DEFAULT_CONFIG = """[paths]
log_file = ~/.config/DotDrop/log.txt

themes_dir = ~/.config/DotDrop/themes

[themes]
"""

        LOG_LEVELS = {'info': '',
                      'warning': 'WARN',
                      'user_error': '!MISS',
                      'program_error': '! ERROR !'}

        LINE_FORMAT = '[{session_name}] {time_date} | {level} --> {message}'


        self.USER_CONFIG_DIR = str(Path('~/.config/DotDrop/').expanduser()) + '/'
        print(self.USER_CONFIG_DIR)
        self.USER_CONFIG_FILE = 'dotdrop.conf'

        if self.CheckConfigExists():

            self.config = configparser.ConfigParser()
            self.config.read(self.USER_CONFIG_DIR+self.USER_CONFIG_FILE)

            print(self.GetLogFile())

            log = LogIt(log_file=self.GetLogFile(), levels=LOG_LEVELS)
            log.SetFormats(text_format=LINE_FORMAT)
            if log.TestFormating(test_data={'session_name': '123', 'time_date': log.GetTimeViaFormat(), 'level': '', 'message': 'testing'}):
                log.WriteStartLine(line='<<< ================== {session_name} ================== >>>', data={'session_name': log.data['session_name']})


        self.ap = ArgumentParser()
        self.args = self.ap.GetArguments()
        print('asdasd')
        log.Write(message=f'Arguments connected! ARGS: {self.args}', level='info')

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

    def ProcessArguments(self):

        pass


    def CreatingNewArchive(self):

        DE = ['1) Hyprland']

        print('Welcome to the creation of a new archive!\nEnter the name for the new topic without spaces (e.g., dark-tokyo):\n')

        new_theme_name = input('>>> ')

        print('\nSpecify the DE from the list below:')

        while True:

            for i in DE: print(i)

            DE_seleceted = int(input('\n>>> '))

            if DE_seleceted > len(DE):
                print('Invalid choice! Select a number from the list below:')
                continue
            else:
                break





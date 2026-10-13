import argparse

class ArgumentParser:

    def __init__(self):

        self.parser = argparse.ArgumentParser(description="Configuration File Management Manager")

        self.parser.add_argument('-cnt', '--create-new-theme', help='Creating a new topic archive')

        self.parser.add_argument('-e')


    def GetArguments(self):

        return self.parser.parse_args()

    def ListArguments(self):
        pass


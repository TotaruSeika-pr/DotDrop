import time


class LogIt:
    """
        LogIt is a custom-written module to replace the built-in logging.
        LogIt was developed as a universal module with the ability to change message string formats.
        Use LogIt as an instance of a class so you can pass it around without changing the settings.
    """

    SESSION_NAME_TYPES = ['time', 'custom'] # Possible types of session names


    def __init__(self,
                 log_file='log.txt',
                 levels=None,
                 session_name_type='time',
                 session_name='',
                 ):
        """
            When initializing a class instance, you can specify:
                - log_file: path to the log file
                - levels: You can pass your message importance levels in dictionary format. Example: {"INFO": "Information", "ERR": "error-message"}
                    key - level indication
                    value - the level value that will be written to the file.
                    !!! When attempting to access a level that does not exist, an error occurs. !!!
                - session_type: a parameter that allows you to set your own session name through the custom parameter, or using ready-made solutions. Check LogIt.SESSION_NAME_TYPES value
                - session_name: Pass this parameter if you use the custom session name type.
        """

        self.VERSION = 'dev 1.0.0' # module version

        if session_name_type in self.SESSION_NAME_TYPES: # checking for correct session name types
            if session_name_type == 'time':
                self.session_name = round(time.time())

            elif session_name_type == 'custom' and session_name != '':
                self.session_name = session_name

            else:
                raise Error('"session_name" is required when "session_name_type" is set to "custom"')
        else:
            raise Error(f'Invalid "session_name_type" specified, try: {SESSION_NAME_TYPES}')
        
        self.levels = levels

        self.log_file = log_file # path to the log file
        self.text_format = '[{session_name}] {time_date} !{level}! -> {message}' # default log text format
        self.date_format = '%Y-%m-%d %H:%M:%S' # default log date and time format


        self.data = {'session_name': self.session_name, 'time_date': time.strftime(self.date_format, time.localtime()), 'level': 'INFO', 'message': 'Hello world!'}
        # ^^^ The data variable stores all the information for messages. In this case, default values ​​are defined.

    def WriteStartLine(self, line='<<< ================== NEW SESSION ================== >>>', data=None):
        """
            This method is designed to write the first line when a session is created. Note the parameters:
                - line: The string itself. You can specify some data in the string using curly braces. Example: "START_SESSION {xyz}"
                - data: A parameter that stores and sets a value in a string. Specify the same values ​​that you specified in line. The data must be in dictionary format.
        """

        with open(self.log_file, 'a') as f:
            line += '\n'
            if data != None:
                f.write(line.format(**data))
            else:
                f.write(line)

    def GetTimeViaFormat(self):
        """
            In order to save module imports, this method was created for conveniently obtaining the date and time in an already specified format.
        """
        return time.strftime(self.date_format, time.localtime())

    def SetFormats(self, text_format=None, date_format=None, format_check=False):
        """
            Use this function to set the format for text and time. Pass on:
                - text_format: set text format
                - date_format: set the date format according to the time module
        """

        if text_format == None and date_format == None:
            raise Error("Pass at least one of the parameters!")

        if text_format != None:
            self.text_format = text_format

        if date_format != None:
            self.date_format = date_format

    def TestFormating(self,
                      test_text_format=None,
                      test_date_format=None,
                      test_data=None,
                      verbos=False
                      ):
        """
            This function is used to verify string formatting.
            It primarily checks for errors, but it also provides a brief report that includes the formatted strings themselves.
            You can also use this function simply to check your time formats for errors.
            Pass these parameters for:
            (If the parameters below are not passed, the values ​​already set in `self` will be used.)
                - test_text_format: your test format for the text
                - test_date_format: parameter to specify date format
                - test_data: Specify this parameter if your formats use values ​​other than the defaults.
                - verbos: By default, the function returns either True or False. To obtain a more detailed response, set this parameter to True.
        """

        answer = {
            'bool_text_format_check': False,
            'text_formating': '',
            'bool_date_format_check': False,
            'date_formating': ''
            }

        if test_text_format == None:
            test_text_format = self.text_format

        if test_date_format == None:
            test_date_format=self.date_format

        if test_data == None:
            test_data = self.data


        if test_data == None:

            raise Error("The 'data' parameter is required, but it was not specified")
        else:
            if type(test_data) != dict:
                raise Error("Invalid type for the 'data' variable. Only 'dict' is accepted.")
            else:
                # Text Format Check
                try:
                    test_text_format.format(**test_data)

                except KeyError as e:
                    raise Error(f"Parameter {e} not found! Check that the message text format is specified correctly!")

                except Exception as e:
                    raise Error(f"An unexpected error occurred: {e}.")

                else:
                    answer['bool_text_format_check'] = True
                    if verbos: answer['text_formating'] = test_text_format.format(**test_data)

                # Date Format Check
                try:
                    time.strftime(test_date_format, time.localtime())
                except Exception as e:
                    raise Error(f"An unexpected error occurred: {e}.")
                else:
                    answer['bool_date_format_check'] = True
                    if verbos: answer['date_formating'] = time.strftime(test_date_format, time.localtime())

        if verbos:
            return answer
        else:
            return answer['bool_text_format_check'] & answer['bool_date_format_check']


    def Write(self, message='Hello world!', level='INFO', data=''):
        """
            A function that writes a message to the log. It accepts the following parameters:
                - message: the message itself
                - level: The importance level of the message. If no levels have been defined previously, the recording will occur normally.
                  Otherwise, an attempt will be made to obtain a level from those already defined.
                - data: If a parameter other than the usual one was passed to text_format, then the same parameters must be passed in this variable.
        """

        self.data['message'] = message
        if self.levels != None:
            try:
                self.levels[level]
            except KeyError:
                raise Error(f"Error defining the level key. Either it doesn't exist, or the key is specified incorrectly. {self.levels}")
            else:
                self.data['level'] = self.levels[level]
        else:
            self.data['level'] = level
        
        self.data['time_date'] = time.strftime(self.date_format, time.localtime())
        with open(self.log_file, 'a') as f:
            f.write(self.text_format.format(**self.data)+'\n')

class Error(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return '{0} '.format(self.message)


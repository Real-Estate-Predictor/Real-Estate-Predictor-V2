import logging
import sys


class Logger:

    def __init__(self, debug_level=logging.DEBUG):
        # reference: https://realpython.com/python-logging/

        self.logger = logging.getLogger(__name__)

        # default log level is debug
        self.logger.setLevel(debug_level)

        # formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
        #                             '%m-%d-%Y %H:%M:%S')

        # stdout_handler = logging.StreamHandler(sys.stdout)
        # stdout_handler.setLevel(logging.DEBUG)
        # stdout_handler.setFormatter(formatter)

        # file_handler = logging.FileHandler('logs.log')
        # file_handler.setLevel(logging.DEBUG)
        # file_handler.setFormatter(formatter)

        # self.logger.addHandler(file_handler)
        # self.logger.addHandler(stdout_handler)

    
    def debug(self, message):
        self.logger.debug(message)

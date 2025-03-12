import sys
import logging
from src.logger import logging

def get_exception_details(error_message, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message_format = "Error occurred in python script [{0}], line number [{1}], error message [{2}]".format(
        file_name, line_number, str(error_message)
    )
    return error_message_format

class CustomException(Exception):
    def __init__(self, error_message, error_details):
        error_details_formatted = get_exception_details(error_message, error_details)
        super().__init__(error_details_formatted)
        self.error_message = error_details_formatted

    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1 / 0  # Intentional division by zero
    except Exception as e:
        logging.info('Exception divided by zero') # Logs traceback
        raise CustomException(e, sys)


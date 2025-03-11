'''
1. what is the error due to get exception?
2. in which line number
3. in which file
'''
import sys
import logging
def get_exception_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error = error
    error_message = 'Error occured in python script [{0}], line number [{1}] and error message [{2}]'.format(
        file_name, line_number, error
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error,error_details:sys):
        super().__init__(error)
        self.error = get_exception_details(error=error, error_details=error_details)

    def __str__(self):
        return self.error
    
    



    



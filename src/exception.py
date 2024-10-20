import sys  #sys library has all the info about the exceptions
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  #exc_info is the exception info of sys module which returns 3 objects in tuple
    file_name=exc_tb.tb_frame.f_code.co_filename   #exc_tb is exception tracback.tb_frame,f_code and co_filename gives line, function metadata and filename where the error occured
    error_message="Error occurred in python script [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
         super().__init__(error_message)
         self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def _str_(self):
        return self.error_message            

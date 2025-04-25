import sys
import logging

# Function to create a detailed error message with line number
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script [{file_name}], line number [{line_number}], and error message is [{str(error)}]"
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Main block for testing the exception handling
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Set up logging
    try:
        a = 1 / 0  # Division by zero to trigger the exception
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys)  # Raise the custom exception

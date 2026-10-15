import logging

logging.basicConfig(level=logging.DEBUG, filename='recorder_ErrorsandExceptions.log', filemode="w", force=True, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1/0
except ZeroDivisionError as e:
    #print(e)
    logging.exception("This is a divide by zero error.")
    

# Note, though the logging level = DEBUG, the logging.info is being printed.
# Thats because all the logging levels above logging.debug will be executed
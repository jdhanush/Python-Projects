import logging

logging.basicConfig(level=logging.DEBUG, filename='recorder_with_format.log', filemode="w", force=True, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

x = 3
logging.info(f"The value of x: {x}")

# Note, though the logging level = DEBUG, the logging.info is being printed.
# Thats because all the logging levels above logging.debug will be executed
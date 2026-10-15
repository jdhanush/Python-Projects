#############
# This is an incomplete program from 'logging video from Tech with Tim'

import logging

logging.basicConfig(level=logging.DEBUG, filename='recorder_ErrorsandExceptions.log', filemode="w", force=True, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# creating a custom logger
logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %')
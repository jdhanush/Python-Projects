import logging

# Below are the five levels of logging and they go in this order 
# 'critical' is of highest importance and 'debug' is of least important

logging.basicConfig(level=logging.INFO, filename='recorder_wo_format.log', filemode="w", force=True)


#Priority order in ascending order from top to bottom
logging.debug("debug - this will be printed")
logging.info("info - this will be printed")
logging.warning("warning - this will be printed")
logging.error("error - this will be printed")
logging.critical("critical - this will be printed")


# By default, when you use the logging module, the output appear only for warning() 
# level and above


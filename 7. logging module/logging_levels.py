import logging

# Below are the five levels of logging and they go in this order 
# 'critical' is of highest importance and 'debug' is of least important

logging.basicConfig(level=logging.DEBUG, force=True)

# If level=logging.INFO, the logs are printed for priority info and above
# If level=logging.DEBUG, the logs are printed for priority DEBUG and above

#Priority order in ascending order from top to bottom
logging.critical("critical - this will be printed")     # priority-1
logging.error("error - this will be printed")           # priority-2
logging.warning("warning - this will be printed")       # priority-3
logging.info("info - this will be printed")             # priority-4
logging.debug("debug - this will be printed")           # priority-5

# By default, i.e., if you comment ( logging.basicConfig(level=logging.INFO, force=True) )
# the logging module gives the output only for warning() level and above


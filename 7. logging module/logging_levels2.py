import logging
logging.basicConfig(level="INFO")
logging.debug("debug text is logged - Severity_Level = 0")
logging.info("info text is logged - Severity_Level = 1")
logging.warning("warning text is logged by Default - Severity_Level = 2")
logging.error("error text is logged by Default - Severity_Level = 3")
logging.critical("critical text is logged by Default- Severity_Level = 4")



# DEBUG (=10) - Provides detailed information that’s valuable to you as a developer.

# INFO (=20) - Provides general information about what’s going on with your program.
#logging.basicConfig(level="INFO") or logging.basicConfig(level=20) or logging.basicConfig(level=logging.INFO)

# WARNING (=30) - Indicates that there’s something you should look into.  

# ERROR (=40) - Alerts you to an unexpected problem that’s occurred in your program.

# CRITICAL (=50) - Tells you that a serious error has occurred and may have crashed your app.
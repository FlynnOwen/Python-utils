import logging

# Define a file to write the logs to. Level is the minimum level written.
# Logs are appended to the file by default (filemode = 'a')
# Use filemode = 'w' to overwrite the log
logging.basicConfig(filename='test_log.log', level=logging.WARNING, filemode='w')

# debug is lowest level
logging.debug('This is a debug message')

# Followed by info
logging.info('This is an info message')

# Warning next. It will show in console
logging.warning('This is a Warning')

# Error is 2nd highest - also shows in console
logging.error('This is an error')

# Critical is highest level - also in console
logging.critical('This is critical')


'''
Writing to a logging file through the duration of a script.
'''
import logging
from datetime import datetime

# Define a file to write the logs to. Level is the minimum level written.
# Logs are appended to the file by default (filemode = 'a')
# Use filemode = 'w' to overwrite the log
logging.basicConfig(filename=str(datetime.today()) + '.log', level=logging.DEBUG, filemode='w')

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


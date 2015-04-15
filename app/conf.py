import logging

from logging.handlers import RotatingFileHandler


# creating loggin object
logger = logging.getLogger()
# setting the lowest loggin level (DEBUG <-> everything)
logger.setLevel(logging.DEBUG)
# formating logs
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

# specify file handler in 'append' mode with 1Mo size and backup
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# set the level of which to register in the file
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# attach the handler to our loggin object
logger.addHandler(file_handler)
# stream to console
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.INFO)
steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)

# How to log:
# logger.info('Hello')
# logger.warning('Testing %s', 'foo')

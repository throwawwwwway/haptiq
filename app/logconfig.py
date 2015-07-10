import logging

from logging.handlers import RotatingFileHandler


# creating loggin object
log = logging.getLogger()
# setting the lowest loggin level (DEBUG <-> everything)
log.setLevel(logging.DEBUG)
# formating logs
# formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
formatter = logging.Formatter('%(levelname)s :: %(message)s')

# specify file handler in 'append' mode with 1Mo size and backup
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# set the level of which to register in the file
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

# attach the handler to our loggin object
log.addHandler(file_handler)
# stream to console
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)
log.addHandler(steam_handler)

# How to log:
# log.info('Hello')
# log.warning('Testing %s', 'foo')
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('/path/file.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
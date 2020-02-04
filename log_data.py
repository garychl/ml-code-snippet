import logging
from datetime import datetime


def get_logger_style(logger, path):
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger = get_logger_style(logger, './log/log_file.txt')
    logger.info('Start running at: {}'.format(
        datetime.today().strftime('%Y-%m-%d-%H:%M:%S')))
import logging

import pytest


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name) :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger


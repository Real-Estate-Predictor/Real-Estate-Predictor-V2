
from Logger import Logger

def test_debug():

    logger = Logger()

    logger.debug("this is a debug message")

def test_info():

    logger = Logger()

    logger.info("this is a info message")

def test_warning():

    logger = Logger()

    logger.warning("this is a warning message")

if __name__ == "__main__":

    # debug does not work for some reason
    test_debug()
    test_info()
    test_warning()
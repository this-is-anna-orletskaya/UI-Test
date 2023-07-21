import os
import logging


def add_log(request):
    test_name = request.node.name
    logger  = logging.getLogger(name=test_name)
    logger.setLevel(logging.DEBUG)
    fileHandler  = logging.FileHandler(f'.\logs\\{test_name}.log') 
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger



   
import os
import logging



class Logger:

    @classmethod
    def add_to_log(cls, request):
        test_name = request.node.name
        logger  = logging.getLogger(name=test_name)
        logger.setLevel(logging.DEBUG)
        if (logger.hasHandlers()):
            logger.handlers.clear()
        fileHandler  = logging.FileHandler(f'.\logs\\{test_name}.log') 
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger



   
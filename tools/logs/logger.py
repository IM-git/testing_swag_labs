from loguru import logger


class Logger:

    logger.add("debug.json", format="{time} {level} {message}",
               level="DEBUG", retention="1 day", serialize=True)

    @staticmethod
    def info(value):
        return logger.info(f' : {value}')

    @staticmethod
    def debug(value):
        return logger.debug(f' : {value}')

    @staticmethod
    def warning(value):
        return logger.warning(f' : {value}')

    @staticmethod
    def error(value):
        return logger.error(f' : {value}')

    @staticmethod
    def critical(value):
        return logger.critical(f' : {value}')

import logging
import os
import allure



class AllureLoggingHandler(logging.Handler):
    def log(self, level_name, message):
        with allure.step(f"Log ({level_name}) {message}"):
            if level_name.lower() == "error":
                allure.attach.file(source="path.jpg", attachment_type=allure.attachment_type.JPG, name="Screenshot")

    def emit(self, record):
        self.log(record.levelname, record.getMessage())

@staticmethod
def loggen():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    # Uncomment the below COde to displaye log on console
    logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")
    allure_handler = AllureLoggingHandler()
    logger.setLevel(logging.INFO)
    p = os.getcwd()
    path = p.__add__("\\Logs\\logfile.log")
    handler_info = logging.FileHandler(path, mode="w")
    handler_info.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")
    handler_info.setFormatter(formatter)
    logger.addHandler(handler_info)
    logger.addHandler(allure_handler)
    return logger


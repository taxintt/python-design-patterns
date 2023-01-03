from logger import Logger
from decorator_logger import SyslogLogger

def output_log():
    with open("sample.log", 'w') as file:
        logger = Logger(file)
        logger.log('message')
    
    logger = SyslogLogger("warn")
    logger.log("hoge")

if __name__ == "__main__":
    output_log()
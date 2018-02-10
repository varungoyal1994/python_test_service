import logging;

"""This is logging class which is used for logging purpose"""


class CLoggerWrapper:

    logLevelDict = {}
    LOG_INFO = 3;
    LOG_DEBUG = 4;
    LOG_ERROR = 2;
    LOG_EXCEPTION = 1;

    def __init__(self,fileName,logLevel,enableconsolelog):

        self.fileName = fileName
        self.consolelog = enableconsolelog;
        logLevelDict = {
            CLoggerWrapper.LOG_EXCEPTION : logging.CRITICAL,
            CLoggerWrapper.LOG_ERROR : logging.ERROR,
            CLoggerWrapper.LOG_DEBUG : logging.DEBUG,
            CLoggerWrapper.LOG_INFO : logging.INFO
        }
        logInitLevel = logLevelDict.get(logLevel,logging.DEBUG);
        FORMAT = '%(asctime)s %(levelname)s %(message)s'
        print "LoggerWrapper :: Logging Level ",logInitLevel,"File Name: ",fileName;
        logging.basicConfig(filename=self.fileName, level=logInitLevel,format=FORMAT)
        logging.error("Logger Initalized :: ");

    def print_log(self,level,message, *args):
        if self.consolelog:
            print(message % args)

        if level == CLoggerWrapper.LOG_DEBUG:
            self.DEBUG(message,args)
        if level == CLoggerWrapper.LOG_ERROR:
            self.ERROR(message, args)
        if level == CLoggerWrapper.LOG_INFO:
            self.INFO(message, args)
        if level == CLoggerWrapper.LOG_EXCEPTION:
            self.EXCEPTION(message, args)

    def ERROR(self,message, args):
        logging.error(message % args)

    def EXCEPTION(self,message, *args):
        logging.exception(message % args)

    def DEBUG(self,message, args):
        logging.debug(message % args)

    def INFO(self,message, args):
        logging.info(message % args)


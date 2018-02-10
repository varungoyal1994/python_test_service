import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil

from CustomLogger.LoggerWrapper import  CLoggerWrapper;

class TestService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.objCustomLogger = CLoggerWrapper("D:\\TestService.log",CLoggerWrapper.LOG_INFO,0)

    def SvcStop(self):
        self.objCustomLogger.print_log(CLoggerWrapper.LOG_INFO, "Hey this is custom Log Service is Stopping ")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            with open('D:\\TestService.log', 'a') as f:
                self.objCustomLogger.print_log(CLoggerWrapper.LOG_INFO,"Hey this is custom Log Service is running ")
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TestService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TestService)
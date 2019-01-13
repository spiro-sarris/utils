import logging	
import LoggerTestFile
from IPython.core.logger import Logger

mytest = LoggerTestFile.LoggerSession('todaysession')

ipylogger = LoggerTestFile.IPythonLoggerChild('mychild','~/')
ipylogger.logstart(log_output=True, log_raw_input=True)

mytest.createShow()
mytest.mycomp.doSomething()

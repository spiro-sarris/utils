import LoggerTestFile
# Import short function names into iPython namespace
from LoggerTestFunctions import *

mytest = LoggerTestFile.LoggerTestClass('my name')

mytest.startLog()
mytest.showMe()
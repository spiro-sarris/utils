import logging
import coloredlogs

def logConfig(logger):		
	logger.setLevel(logging.DEBUG)
	fmt_file = '%(asctime)s [%(levelname)s] %(module)s.%(name)s.%(funcName)s() line %(lineno)s: %(message)s'
	fmt_scrn = '%(asctime)s [%(levelname)s] %(module)s.%(name)s.%(funcName)s() line %(lineno)s: %(message)s'
	formatter_file = logging.Formatter(fmt_file)
	formatter_screen = coloredlogs.ColoredFormatter(fmt_scrn)

	# creating a handler to log on the filesystem
	handler_file=logging.FileHandler(filename='logfile.log', mode='a')
	handler_file.setFormatter(formatter_file)
	handler_file.setLevel(logging.DEBUG)

	# creating a handler to log on the console
	handler_screen=logging.StreamHandler()
	handler_screen.setFormatter(formatter_screen)
	handler_screen.setLevel(logging.DEBUG)

	# adding handlers to our logger
	logger.addHandler(handler_screen)
	logger.addHandler(handler_file)

class LoggerSession:
	def __init__(self, name):
		self.name = name
		self.logger = None
		self.mycomp = None
		
		self.logger = logging.getLogger(self.__class__.__name__)
		logConfig(self.logger)
		self.logger.info('Starting log for object %s' % self.name)		
	
	def createShow(self):
		self.mycomp = ShowOff('hello')

class ShowOff:
	def __init__(self, name):
		self.name = name
		self.logger = None
		self.logger = logging.getLogger(self.__class__.__name__)
		logConfig(self.logger)
		self.logger.info('Starting log for object %s' % self.name)		

	def doSomething(self):
		self.logger.error('what is happening')

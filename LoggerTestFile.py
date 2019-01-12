import logging
import coloredlogs

class LoggerTestClass:
	def __init__(self, name):
		self.name = name
		self.logger = None

	def startLog(self):
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		formatter_file = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s.%(funcName)s at line %(lineno)s: %(message)s')
		formatter_screen = coloredlogs.ColoredFormatter('%(asctime)s [%(levelname)s] %(module)s.%(funcName)s at line %(lineno)s: %(message)s')

		# creating a handler to log on the filesystem
		handler_file=logging.FileHandler('logfile.log')
		handler_file.setFormatter(formatter_file)
		handler_file.setLevel(logging.DEBUG)

		# creating a handler to log on the console
		handler_screen=logging.StreamHandler()
		handler_screen.setFormatter(formatter_screen)
		handler_screen.setLevel(logging.DEBUG)

		# adding handlers to our logger
		self.logger.addHandler(handler_screen)
		self.logger.addHandler(handler_file)
		self.logger.info('logger started')
		self.logger.debug('qty names %d %s' % (len(self.logger.handlers), str(self.logger.handlers)))


	def showMe(self):
		self.logger.debug('debug message')
		self.logger.info('info message')
		self.logger.warning('warning message')
		self.logger.error('error message')
		self.logger.critical('critical message')

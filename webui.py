import sys
from threading import Thread

import PySide.QtCore as qt_core
import PySide.QtWebKit as web_core
import PySide.QtGui as gui_core


class Core(object):

	def __init__(self, url):
		self.url = url
		self.app = gui_core.QApplication(sys.argv)
		self.view =  web_core.QWebView(self.app.activeModalWidget())

	def run(self):
		self.view.load(qt_core.QUrl(self.url))
		self.view.show()
		self.app.exec_()


def main():

	core = Core("http://127.0.0.1:5000")
	sys.exit()

if __name__ == '__main__':
	main()
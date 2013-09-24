import pythoncom
from threading import Thread

import PySide.QtCore as qt_core
import PySide.QtWebKit as web_core
import PySide.QtGui as gui_core

class WebUI(object):
  def __init__(self, app, url="http://127.0.0.1:5000", debug=False):
    self.flask_app = app
    self.flask_thread = Thread(target=self._run_flask, args=(debug,))
    self.flask_thread.daemon = True;

    self.url = url
    self.app = gui_core.QApplication([])
    self.view =  web_core.QWebView(self.app.activeModalWidget())

  def run(self):
    self.run_flask()
    self.run_gui()

     
  def run_flask(self):
    self.flask_thread.start()

  def run_gui(self):
    self.view.load(qt_core.QUrl(self.url))
    self.view.show()
    self.app.exec_()
 
  def _run_flask(self, debug):
    pythoncom.CoInitialize()
    self.flask_app.run(debug=debug, use_reloader=False)
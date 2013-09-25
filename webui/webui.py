from threading import Thread

import PySide.QtCore as qt_core
import PySide.QtWebKit as web_core
import PySide.QtGui as gui_core

class WebUI(object):
    def __init__(self, app, url="http://127.0.0.1:5000", debug=False, using_win32=False):
        self.flask_app = app
        self.flask_thread = Thread(target=self._run_flask, args=(debug, using_win32,))
        self.flask_thread.daemon = True;
        self.debug = debug

        self.url = url
        self.app = gui_core.QApplication([])
        self.view = web_core.QWebView(self.app.activeModalWidget())

    def run(self):
        self.run_flask()
        self.run_gui(inspector=self.debug)

    def run_flask(self):
        self.flask_thread.start()

    def run_gui(self, inspector=False):
        self.view.load(qt_core.QUrl(self.url))

        change_setting = self.view.page().settings().setAttribute
        change_setting(web_core.QWebSettings.DeveloperExtrasEnabled, True)
        change_setting(web_core.QWebSettings.LocalStorageEnabled, True)
        change_setting(web_core.QWebSettings.OfflineStorageDatabaseEnabled, True)
        change_setting(web_core.QWebSettings.OfflineWebApplicationCacheEnabled, True)
        change_setting(web_core.QWebSettings.PluginsEnabled, True)

        self.view.show()

        if inspector:
            self.inspector = web_core.QWebInspector()
            self.inspector.setPage(self.view.page())
            self.inspector.show()

        self.app.exec_()

    def _run_flask(self, debug=False, using_win32=False):
        if using_win32:
            import pythoncom
            pythoncom.CoInitialize()
        self.flask_app.run(debug=debug, use_reloader=False)

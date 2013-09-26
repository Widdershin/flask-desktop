from threading import Thread

import PySide.QtCore as qt_core
import PySide.QtWebKit as web_core
import PySide.QtGui as gui_core

default_url = "127.0.0.1"


class WebUI(object):
    def __init__(self, app, url=default_url, port=5000,
                 debug=False, using_win32=False):
        self.flask_app = app
        self.flask_thread = Thread(target=self._run_flask,
                                   args=(url, port, debug, using_win32))
        self.flask_thread.daemon = True
        self.debug = debug

        self.url = "http://{}:{}".format(url, port)
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
        settings = web_core.QWebSettings
        change_setting(settings.DeveloperExtrasEnabled, True)
        change_setting(settings.LocalStorageEnabled, True)
        change_setting(settings.OfflineStorageDatabaseEnabled, True)
        change_setting(settings.OfflineWebApplicationCacheEnabled, True)
        change_setting(settings.PluginsEnabled, True)

        self.view.show()

        if inspector:
            self.inspector = web_core.QWebInspector()
            self.inspector.setPage(self.view.page())
            self.inspector.show()

        self.app.exec_()

    def _run_flask(self, host, port, debug=False, using_win32=False):
        print host
        if using_win32:
            import pythoncom
            pythoncom.CoInitialize()
        self.flask_app.run(debug=debug, host=host, port=port, use_reloader=False)

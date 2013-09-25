WebUI
=====

WebUI is a Python module that allows you to convert Flask apps into cross platform desktop apps with three lines of code.

Installation:
-------------
::

    easy_install pyside # Only use this command on Windows, as pip does not install binaries      
    pip install WebUI


Usage:
------
::

    from WebUI import WebUI # Add WebUI to your imports
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    ui = WebUI(app, debug=True) # Create a WebUI instance

    # all of your standard flask logic

    if __name__ == '__main__':
      ui.run() #replace app.run() with ui.run(), and that's it


WebUI is powered by PySide, and should run on Windows, Mac and Linux. You can even create standalone executables using PyInstaller!

License
-------
WebUI is licensed under the MIT License. See the LICENSE file for more details.

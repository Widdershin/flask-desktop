from flask import Flask, render_template, request
from webui import WebUI
from threading import Thread

import os

app = Flask(__name__)
ui = WebUI(app, debug=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
  file_path = "C:"+request.path
  return render_template("basic.html", url=request.path, items= [".."] + os.listdir(file_path))

if __name__ == '__main__':
  ui.run()
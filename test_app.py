from flask import Flask, render_template, request
from webui import Core
from multiprocessing import Process

import os

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
  file_path = "C:"+request.path
  return render_template("basic.html", url=request.path, items= [".."] + os.listdir(file_path))

def run_web_app():
  app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
  core = Core("http://127.0.0.1:5000")
  flask_proc = Process(target=run_web_app)
  flask_proc.daemon = False
  flask_proc.start()
  core.run()
  flask_proc.terminate()

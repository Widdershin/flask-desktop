from flask import Flask
from webui import Core
from multiprocessing import Process

import os

app = Flask(__name__)

@app.route('/')
def main():
  output = ""
  for i in os.listdir('.'):
    output += "{}</br>".format(i)
  return output

def run_web_app():
  app.run()

if __name__ == '__main__':
  core = Core("http://127.0.0.1:5000")
  flask_proc = Process(target=run_web_app)
  flask_proc.daemon = False
  flask_proc.start()
  core.run()
  flask_proc.terminate()

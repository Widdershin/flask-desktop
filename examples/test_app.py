from flask import Flask, render_template, request
from webui import WebUI

import os

app = Flask(__name__)
ui = WebUI(app, debug=True)

@app.route('/')
def main():
  return "Hello world!"

if __name__ == '__main__':
  ui.run()

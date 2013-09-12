from flask import Flask
from webui import Core
from threading import Thread

import os

app = Flask(__name__)

@app.route('/')
def main():
	return os.listdir('.')

def run_web_app():
	app.run()

if __name__ == '__main__':
	core = Core("http://127.0.0.1:5000")
	thread = Thread(target=run_web_app)
	thread.start()
	core.run()
	thread.join()
	sys.exit()

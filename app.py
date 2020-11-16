import os
import signal

from flask import Flask

from project import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><head></head><meta content="text/html; charset=windows-1251"><body><h1>'
    #page += generator.generate_buzz()
    page += 'SALAM ALEIKUM, РАБОТАЕТ'
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
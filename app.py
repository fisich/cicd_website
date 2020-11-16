import os
import signal

from flask import Flask, request, render_template

from project import generator

app = Flask(__name__, template_folder='resources', static_folder='resources')

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route('/')
def generate_buzz():
    page = '<html><head><meta content="text/html; charset=windows-1251"><title>Мой CI/CD проект</title><style>'
    page += '.txt {font-family: "Comic Sans", cursive; font-size:50px; letter-spacing:2px; width:100%; ' \
            'position: relative; display: block; top: 7%; margin: 0 auto; margin-left: auto;' \
            'margin-right: auto; text-align: center;}'
    page += '.ex5 .txt:before {content: ""; position: absolute; height: 3px; width: 400px;' \
            'background:rgb(81, 227, 213); top: -7%;margin: 0 auto; left: 0;right: 0;}'
    page += 'body {background-image: url("/resources/bg.jpeg"); background-size: cover; color: white}</style></head>' \
            '<body><div class="ex5"><p class="txt">CI/CD Парсер</p></div>'

    if len(request.args) != 0:
        page += '<br>Параметры страницы:<br>'
    else:
        page += '<br>Введите в качестве параметра страницы url любого сайта<br>'
    for key in request.args:
        page += key + ' = ' + request.args.get(key) + '<br>'

    page += '</body></html>'
    return page

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
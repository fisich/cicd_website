import os
import signal

from flask import Flask, request, render_template

from project import generator, parser

app = Flask(__name__, template_folder='resources', static_folder='resources')

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route('/')
def generate_buzz():
    page = '<html><head><meta content="text/html; charset=windows-1251"><title>Мой CI/CD проект</title><style>'
    page += 'table {font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;font-size: 14px; ' \
            'border-collapse: collapse; text-align: center; margin: auto;}' \
            'th, td:first-child { background: #a1b4e5; color: white; padding: 10px 20px; } th, td { border-style: solid;' \
            'border-width: 0 2px 2px 0; border-color: white; }' \
            'td { background: #D8E6F3; }' \
            'th:first-child, td:first-child { text-align: left; }'
    page += '.txt {font-family: "Comic Sans", cursive; font-size:50px; letter-spacing:2px; width:100%; ' \
            'position: relative; display: block; top: 7%; margin: 0 auto; margin-left: auto;' \
            'margin-right: auto; text-align: center;}'
    page += '.ex5 .txt:before {content: ""; position: absolute; height: 3px; width: 400px;' \
            'background:rgb(81, 227, 213); top: -7%;margin: 0 auto; left: 0;right: 0;}'
    page += 'body {background-image: url("/resources/bg.jpg"); background-size: cover;}</style></head>' \
            '<body><div class="ex5"><p class="txt" style="color: white;">CI/CD Новости</p></div>'

    page += '<h2 style="color: white;" align="center">Горячие новости</h2>'
    page += parser.collectNews("https://mignews.com/")
    page += '<h3 style="color: white" align="center">Все новости<h3>'
    page += parser.collectNews("https://mignews.com/", False)

    page += '</body></html>'
    return page

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
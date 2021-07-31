from flask import Flask, render_template
import argparse

_default_host = 'localhost'

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<path>")
def echo(path):
    return "echoing {0}".format(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start the echo server')
    parser.add_argument("--host", action='store')
    parser.add_argument("--port", "-p", action='store')
    args = parser.parse_args()
    host = args.host if args.host else _default_host
    app.run(host, args.port)
from flask import Flask

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
  # return 'hello world'
  return render_template("index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5001, debug=True)

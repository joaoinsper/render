from flask import Flask

app = Flask(__name__)

@app.roupe("/")
def index():
  return "Olá, <b>tudo bem</b>?"

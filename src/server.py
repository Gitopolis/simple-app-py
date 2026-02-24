from flask import Flask

from version import project_version

app = Flask(__name__)

@app.route("/version")
def version():
  return project_version()

@app.route("/healthz")
def healthz():
  return {"status": "OK"}

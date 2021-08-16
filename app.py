from flask import Flask
from flask import request
from bulidExcel import buildData, bulidExcel
import json

app = Flask(__name__)

@app.route("/getData", methods = ['POST'])
def hello_world():
    return json.dumps(buildData(request.data),ensure_ascii=False)
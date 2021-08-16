from flask import Flask
from flask import request
from BuildExcelOprate import buildData
import json

app = Flask(__name__)

@app.route("/getData", methods = ['POST'])
def hello_world():
    return json.dumps(buildData(request.data),ensure_ascii=False)
import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello GitGuardian!.\n'

@app.route('/<string:pod_id>')
def getPodId(pod_id):
    pod_id=sys.argv[1]
    return '{}'.format(pod_id)

if __name__ == "__main__":
    app.run(debug="true", host='0.0.0.0')
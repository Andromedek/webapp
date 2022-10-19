from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello GitGuardian!.\n'

if __name__ == "__main__":
    app.run(debug="true", host='0.0.0.0')
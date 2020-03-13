from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! We have made a new deployment. Hope you enjoyed!'

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
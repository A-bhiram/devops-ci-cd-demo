from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '✅ Live Update: CD pipeline is fully working on May 13'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


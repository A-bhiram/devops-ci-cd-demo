from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '🚀 CD Test: App auto-deployed successfully!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   return '🔁 Re-test: Final CD check after Day 6!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


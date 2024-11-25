from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask! Here is a start web page developed by Sergei's project. We will continue. And fuck u!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)


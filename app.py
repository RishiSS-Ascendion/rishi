from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if__name__=="__main__": # type: ignore
app.run(debug=True)
from flask import Flask

app=Flask(__name__)


@app.get("/")
def hello_world():
    return "hello_world"


app.run(port=5000,host="localhost")
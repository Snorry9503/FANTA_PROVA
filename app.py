from flask import Flask
import flask_socketio

app=Flask(__name__)

@app.route("/")
def helloWorld():
 return "<p>Ciao Mimi!</p>"

@app.route("/db")
def dbShow():
    return "<h1>questa è la parte db</h1>"
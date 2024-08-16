from flask import Flask
import flask_socketio
import gestioneDBfanta


app=Flask(__name__)

@app.route("/")
def index():
 return "<p>Indice, cosa vuoi ?</p>"

@app.route("/db")
def dbShow():
    if __name__ == 'main':
       return f"<h1>questa è la parte if {__name__}</h1>"   
    else:
       return f"<h1>questa è la parte else {__name__}</h1>"


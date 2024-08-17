from flask import Flask
import flask_socketio
import gestioneDBfanta


app=Flask(__name__)

@app.route("/")
def index():
 return "<p>Indice, cosa vuoi ?</p>"



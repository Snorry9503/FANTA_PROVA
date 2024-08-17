from flask import Flask
import flask_socketio
import gestioneDBfanta
import json
from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route("/")
def index():
 return "<p>Indice, cosa vuoi ?</p>"



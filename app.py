from flask import Flask
import flask_socketio
import gestioneDBfanta
import json
from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route("/")
def index():
 return "<p>Indice, cosa vuoi ?</p>"

@app.route("/dbIngest", method="[GET]")
def dbingest():
    return "<p>codice Ingest database</p>"

@app.route("/getGiocatore/<id>", method="[GET]")
def getGiocatore():
   return "<p>Ritorna il giocatore</p>"

@app.route("/getGiocatori", method="[GET]")
def getGiocatori():
   return "<p>Ritorna tutta la lista dei giocatori</p>"

@app.route("/setSquadraFantaGiocatore/<id>", method="[PUT]")
def setFantaSquadra():
   return "<p>Fa un update del giocatore e lo assegna ad una Fantasquadra</p>"

@app.route("/setIngaggioGiocatore/<id>", method="[PUT]")
def setIngaggioGiocarore():
   return "<p>Setta l'ingaggio che ha pagato il fantagiocatore per la squadra</p>"
from flask import Flask
import flask_socketio
import gestioneDBfanta as fdb
import json
from flask import Flask, jsonify, request
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
 return "<p>Indice, cosa vuoi ?</p>"

@app.route("/dbIngest", methods=['GET','POST'])
def dbingest():
    nome_db='fantasavoia.db'
    conn = sqlite3.connect(nome_db)
    cursor = conn.cursor()

    count = cursor.execute('''SELECT COUNT(*) FROM giocatoriap''')
    giocatoriap=[]

    if count != 0:
       giocatoriap=fdb.caricaGiocatoreAP('C:\\Users\\gabri\\Desktop\\FANTA_PROVA\\statisticheAP.xlsx')       

       for r in giocatoriap:
          fdb.popolaDatabase('fantasavoia.db',
                             'giocatoriap',
                             giocatoriap.anno,
                             giocatoriap.id,
                             giocatoriap.ruolo,
                             giocatoriap.ruoloMantra,
                             giocatoriap.nome,
                             giocatoriap.squadra,
                             giocatoriap.pv,
                             giocatoriap.mv,
                             giocatoriap.fm,
                             giocatoriap.gf,
                             giocatoriap.gs,
                             giocatoriap.rp,
                             giocatoriap.rc,
                             giocatoriap.rplus,
                             giocatoriap.rminus,
                             giocatoriap.assenze,
                             giocatoriap.amm,
                             giocatoriap.esp,
                             giocatoriap.au,
                             '')
        

       return f"<p>numero giocatori presenti{count}</p>"
    else:
       return f"<p>numero giocatori presenti{count}</p>"

@app.route("/getGiocatore/<id>", methods=['GET'])
def getGiocatore():
   return "<p>Ritorna il giocatore</p>"

@app.route("/getGiocatori", methods=['GET'])
def getGiocatori():
   return "<p>Ritorna tutta la lista dei giocatori</p>"

@app.route("/setSquadraFantaGiocatore/<id>", methods=['PUT'])
def setFantaSquadra():
   return "<p>Fa un update del giocatore e lo assegna ad una Fantasquadra</p>"

@app.route("/setIngaggioGiocatore/<id>", methods=['PUT'])
def setIngaggioGiocarore():
   return "<p>Setta l'ingaggio che ha pagato il fantagiocatore per la squadra</p>"
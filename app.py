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
    print(count)

    if count != 0:
       giocatoriap=fdb.caricaGiocatoreAP('C:\\Users\\gabri\\Desktop\\FANTA_PROVA')
       print(giocatoriap.id)      

       for r in giocatoriap:
          fdb.popolaDatabase('fantasavoia.db',
                             'giocatoriap',
                             r.anno,
                             r.id,
                             r.ruolo,
                             r.ruoloMantra,
                             r.nome,
                             r.squadra,
                             r.pv,
                             r.mv,
                             r.fm,
                             r.gf,
                             r.gs,
                             r.rp,
                             r.rc,
                             r.rplus,
                             r.rminus,
                             r.assenze,
                             r.amm,
                             r.esp,
                             r.au,
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
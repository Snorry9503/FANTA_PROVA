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

@app.route("/dbIngestAP", methods=['GET','POST'])
def dbingestAP():
    
    nome_db='fantasavoia.db'
    giocatoriap=[]
    
    giocatoriap=fdb.caricaGiocatoreAP('C:\\Users\\gabri\\Desktop\\FANTA_PROVA')
    #print(giocatoriap.id)      
    countgiro=0
    for r in giocatoriap:
       countgiro=countgiro+1
       fdb.popolaDatabase(    nome_db,
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
    return f"<p>numero giocatori immessi {countgiro}</p>"
         
    

@app.route("/dbIngestAC", methods=['GET','POST'])
def dbingestAC():
    
    nome_db='fantasavoia.db'
    giocatoriac=[]
    
    giocatoriac=fdb.caricaGiocatoreAC('C:\\Users\\gabri\\Desktop\\FANTA_PROVA')
    #print(giocatoriap.id)      
    countgiro=0
    for r in giocatoriac:
       countgiro=countgiro+1
       fdb.popolaDatabase(    nome_db,
                             'giocatoriac',
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
    return f"<p>numero giocatori immessi {countgiro}</p>"
         
    

   





@app.route("/getGiocatoreAC/<id>", methods=['GET'])
def getGiocatore(id):
   giocatore=fdb.selectGiocatoreIdAC('fantasavoia.db',id)
   

   return f"<p>Ritorna il giocatore {giocatore}</p>"


@app.route("/getGiocatoriAC", methods=['GET'])
def getALLGiocatoriAC():
   nomedb='fantasavoia.db'
   giocatoriAC=fdb.selectGiocatoriAC(nomedb)   
   return jsonify(giocatoriAC)

@app.route("/getGiocatoriAP", methods=['GET'])
def getALLGiocatoriAP():
   nomedb='fantasavoia.db'
   giocatoriAP=fdb.selectGiocatoriAP(nomedb)   
   return jsonify(giocatoriAP)

@app.route("/setSquadraFantaGiocatore/<id>", methods=['PUT'])
def setFantaSquadra():
   return "<p>Fa un update del giocatore e lo assegna ad una Fantasquadra</p>"

@app.route("/setIngaggioGiocatore/<id>", methods=['PUT'])
def setIngaggioGiocarore():
   return "<p>Setta l'ingaggio che ha pagato il fantagiocatore per la squadra</p>"

@app.route("/cancellaDB", methods=['GET', 'DELETE','POST'])
def provaCursore():
    
    nome_db='fantasavoia.db'
    fdb.cancellaDatabase(nome_db)

    return "<h1> giocatori cancellati </h1>"
    


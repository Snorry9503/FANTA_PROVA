import openpyxl
import sqlite3

class Calciatore:
   
   def __init__(self,
                id,
                ruolo,
                ruoloMantra,
                nome,
                squadra,
                squadraFanta,
                pv,
                mv,
                fm,
                gf,
                gs,
                rp,
                rc,
                rplus,
                rminus,
                assenze,
                amm,
                esp,
                au,
               appv,                
               apmv,
               apfm,
               apgf,
               apgs,
               aprp,
               aprc,
               aprplus,
               aprminus,
               apassenze,
               apamm,
               apesp,
               apau):    
    self.id=id
    self.ruolo = ruolo
    self.ruoloMantra = ruoloMantra
    self.nome = nome
    self.squadra = squadra
    self.squadraFanta = squadraFanta
    self.pv = pv 
    self.mv = mv 
    self.fm = fm 
    self.gf = gf 
    self.gs = gs 
    self.rp = rp 
    self.rc = rc 
    self.rplus   = rplus  
    self.rminus  = rminus 
    self.assenze = assenze
    self.amm     = amm    
    self.esp     = esp    
    self.au      = au 



def caricaGiocatore(directory_path):
   #Caricamento directory Padre Excel

   statAC = openpyxl.load_workbook(f"{directory_path}/StatisticheAC.xlsx")
   statAP = openpyxl.load_workbook(f"{directory_path}/StatisticheAP.xlsx")
   quotAC = openpyxl.load_workbook(f"{directory_path}/QuotazioniAC.xlsx")
   quotAP = openpyxl.load_workbook(f"{directory_path}/QuotazioniAP.xlsx")

#Caricamento file foglio Excel
   sheetStatAC = statAC.active
   sheetStatAP = statAP.active
   sheetQuotAC = quotAC.active
   sheetQuotAP = quotAP.active
    
   nuoviGiocatori=[]

   for rowAP in sheetStatAP.iter_rows(min_row=3, values_only=True):
    for rowAC in sheetStatAC.iter_rows(min_row=3, values_only=True):
        if rowAC[0] == rowAP[0]:
            nuoviGiocatori.append(Calciatore(
                            rowAC[0],
                            rowAC[1],
                            rowAC[2],
                            rowAC[3],
                            rowAC[4],
                            None,
                            rowAC[5],
                            rowAC[6],
                            rowAC[7],
                            rowAC[8],
                            rowAC[9],
                            rowAC[10],
                            rowAC[11],
                            rowAC[12],
                            rowAC[13],
                            rowAC[14],
                            rowAC[15],
                            rowAC[16],
                            rowAC[17],
                            rowAP[5],
                            rowAP[6],
                            rowAP[7],
                            rowAP[8],
                            rowAP[9],
                            rowAP[10],
                            rowAP[11],
                            rowAP[12],
                            rowAP[13],
                            rowAP[14],
                            rowAP[15],
                            rowAP[16],
                            rowAP[17]))
            return nuoviGiocatori
        elif rowAC[0] != rowAP[0] & rowAC:
           continue

def creaGiocatoriDatabase():
   statAC = openpyxl.load_workbook(f"{directory_path}/StatisticheAC.xlsx")
   statAP = openpyxl.load_workbook(f"{directory_path}/StatisticheAP.xlsx")
   quotAC = openpyxl.load_workbook(f"{directory_path}/QuotazioniAC.xlsx")
   quotAP = openpyxl.load_workbook(f"{directory_path}/QuotazioniAP.xlsx")
   
   #Caricamento file foglio Excel
   sheetStatAC = statAC.active
   sheetStatAP = statAP.active
   sheetQuotAC = quotAC.active
   sheetQuotAP = quotAP.active   

def crea_database(nome_db):
    conn = sqlite3.connect(nome_db)
    cursor = conn.cursor()
    
    # Creazione della tabella dei giocatori anno corrente
    cursor.execute('''CREATE TABLE IF NOT EXISTS giocatoriac (
	id INTEGER PRIMARY KEY ,
    ruolo TEXT			,
    ruoloMantra	 TEXT		,
    nome		 TEXT		,
    squadra		 TEXT		,
    squadraFanta TEXT		,
    pv			 INTEGER		,
    mv			 INTEGER		,
    fm			 INTEGER		,
    gf			 INTEGER		,
    gs			 INTEGER		,
    rp			 INTEGER		,
    rc			 INTEGER		,
    rplus		 INTEGER		,
    rminus		 INTEGER		,
    assenze		 INTEGER		,
    amm			 INTEGER		,
    esp			 INTEGER		,
    au           INTEGER)
	 ''')
    
    # Creazione della tabella dei giocatori anno precedente
    cursor.execute('''CREATE TABLE IF NOT EXISTS giocatoriap (
	id INTEGER PRIMARY KEY ,
    ruolo TEXT			,
    ruoloMantra	 TEXT		,
    nome		 TEXT		,
    squadra		 TEXT		,
    squadraFanta TEXT		,
    pv			 INTEGER		,
    mv			 INTEGER		,
    fm			 INTEGER		,
    gf			 INTEGER		,
    gs			 INTEGER		,
    rp			 INTEGER		,
    rc			 INTEGER		,
    rplus		 INTEGER		,
    rminus		 INTEGER		,
    assenze		 INTEGER		,
    amm			 INTEGER		,
    esp			 INTEGER		,
    au           INTEGER)
	 ''')
    conn.commit()
    conn.close()

def popolaDatabase(
      nomedb, 
      nometabella,
                id,
                ruolo,
                ruoloMantra,
                nome,
                squadra,
                squadraFanta,
                pv,
                mv,
                fm,
                gf,
                gs,
                rp,
                rc,
                rplus,
                rminus,
                assenze,
                amm,
                esp,
                au):
   conn = sqlite3.connect(nomedb)
   cursor = conn.cursor()
   if nometabella == 'giocatoriac':
      cursor.execute('''
        INSERT INTO giocatoriac ( id,
                ruolo,
                ruoloMantra,
                nome,
                squadra,
                squadraFanta,
                pv,
                mv,
                fm,
                gf,
                gs,
                rp,
                rc,
                rplus,
                rminus,
                assenze,
                amm,
                esp,
                au)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                id,
                ruolo,
                ruoloMantra,
                nome,
                squadra,
                squadraFanta,
                pv,
                mv,
                fm,
                gf,
                gs,
                rp,
                rc,
                rplus,
                rminus,
                assenze,
                amm,
                esp,
                au))
   
   
      conn.commit()
      conn.close()
   elif nometabella == 'giocatoriap':
      cursor.execute('''
        INSERT INTO giocatoriap ( id,
                ruolo,
                ruoloMantra,
                nome,
                squadra,
                squadraFanta,
                pv,
                mv,
                fm,
                gf,
                gs,
                rp,
                rc,
                rplus,
                rminus,
                assenze,
                amm,
                esp,
                au)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                id,
                ruolo,
                ruoloMantra,
                nome,
                squadra,
                squadraFanta,
                pv,
                mv,
                fm,
                gf,
                gs,
                rp,
                rc,
                rplus,
                rminus,
                assenze,
                amm,
                esp,
                au))
   
   conn.commit()
   conn.close()   

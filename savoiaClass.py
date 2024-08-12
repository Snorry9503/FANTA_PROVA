class Squad:
    def __init__(self, squadName, squadLogo, squadAbbr, squadNOplayer, squadPts, squadGoal, squadGoalsubiti):

        self.squadName= squadName
        self.squadLogo= squadLogo
        self.squadAbbr= squadAbbr
        self.squadNOplayer = squadNOplayer
        self.squadPts = squadPts
        self.squadGoal = squadGoal
        self.squadlGoalsubiti=squadGoalsubiti
    
    def getGoal(self):
       print(self.squadGoal)
    def getGoalsubiti(self):
       print(self.getGoalsubiti)
    

class Allenatore:
    def __init__(self, allenatoreName, allenatoreSurname, allenatoreSquad):
        self.name=allenatoreName
        self.allenatoreSurname=allenatoreSurname
        self.allenatoreSquad=allenatoreSquad

    
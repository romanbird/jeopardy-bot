from csv import reader
from random import sample
import numpy as np
from time import time

class Question:
    def __init__(self, line): #parses through database
        self.id = line[0]
        self.round = 1 if line[1]=="Jeopardy!" else 2
        self.topic=line[2]
        self.value=int(line[3][1:].replace(",","")) if int(self.id) > 3966 else int(line[3][1:].replace(",","")) * 2
        self.question=line[4]
        self.answer=line[5]
        self.dailyDouble=False
        self.expired=False
    
    def __repr__(self): #visualisation for debugging purposes
        return "\nTopic: {}, Round:{}, {}, {}, [{}]".format(self.topic[:5],self.round,self.value,self.question[:5],"x" if self.expired else " ")

    def fetchRoundUID(self, roundN): #wtf is this meant to do??? fix later
        return (self.id,self.round,self.topic) if self.round == roundN else None
    
    def returnSelected(self, uIDs):
        if (self.id,self.round,self.topic) in uIDs:
            return self
    
    def checkExpiration(self):
        return "[x]" if self.expired else str(self.value).ljust(4)

    def presentQuestion(self):
        return "{} {}: {}".format(self.topic, self.formatMoney(), self.question)
    
    def formatMoney(self):
        return "${}".format(self.value)

class Player:
    def __init__(self, line):
        self.id = line
        self.money = int(0)

    def __repr__(self):
        return "{}: {}".format(self.id, self.formatMoney())
    
    def formatMoney(self):
        return "${}".format(self.money)

def main():
    with open('db.csv', encoding='utf8') as dbraw:
        db = [Question(i) for i in list(reader(dbraw))]

    #players = genPlayers()
    players = [Player("Roman"), Player("George")]

    roundN = 1
    docket = docketGenerator(db, roundN)

    game(docket, players)



def priceNormalise(docket, roundN): #overwrites price (accounts for confusion in the database)
    for n,i in enumerate(docket):
        i.value = ([200,400,600,800,1000][n%5])*roundN
    return docket

def docketGenerator(db, roundN): #generates the 25 question table for a single round
    categories = sample(set([i.fetchRoundUID(roundN) for i in db if i.round == roundN]),5)
    return priceNormalise([i.returnSelected(categories) for i in db if i.returnSelected(categories) != None], roundN)

def genPlayers(): #inputs players
    players = []
    while True:
        x = input("Enter player name, or 'start' to begin. ")
        if x == "start":
            break
        players.append(Player(x))
    return players

def lookupDocket(docket, x, y):
    return docket[(int(y)*5)+int(x)]

def printBoard(docket):
    for i in range(5):
        print(docket[(i*5)+0].checkExpiration(), docket[(i*5)+1].checkExpiration(), docket[(i*5)+2].checkExpiration(), docket[(i*5)+3].checkExpiration(), docket[(i*5)+4].checkExpiration())
    

def game(docket, players):
    startingTime = 0
    ROUNDDURATION = 20 #Default: 390
    roundN = 1
    docket = np.array(docket).reshape(5,5)
    docket = list(np.swapaxes(docket, 0, 1).flatten()) #This seems somewhat inefficient, will optimise later
    topics = [i.topic for i in docket[0:5]]
    print("TONIGHT'S TOPICS ARE...")
    roundStart = time()
    while (time()-roundStart < ROUNDDURATION):
        print(", ".join(topics))
        printBoard(docket)
        print()
        selection = input("Choose board (i.e. 1,600) ").replace(" ","").split(",")
        questionSelected = lookupDocket(docket, int(selection[0])-1, int(selection[1])/(200*roundN)-1)
        if questionSelected.expired:
            print("Hey, that's already been chosen")
            continue
        questionSelected.expired = True
        print(questionSelected.presentQuestion())
        print("")
        answerResponse = "Template string"
    print("Round Complete!")
        



if __name__ == "__main__":
    main()
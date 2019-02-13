from csv import reader
from random import sample
import numpy as np

class Question:
    def __init__(self, line):
        self.id = line[0]
        self.round = 1 if line[1]=="Jeopardy!" else 2
        self.topic=line[2]
        self.value=int(line[3][1:].replace(",","")) if int(self.id) > 3966 else int(line[3][1:].replace(",","")) * 2
        self.question=line[4]
        self.answer=line[5]
    
    def __repr__(self):
        return "\nTopic: {}, Round:{}, {}, {}".format(self.topic[:5],self.round,self.value,self.question[:5])

    def fetchRoundUID(self, roundN):
        return self.fetchUID() if self.round == roundN else None
    
    def fetchUID(self):
        return (self.id,self.round,self.topic)

    def isSelected(self, uIDs):
        if (self.id,self.round,self.topic) in uIDs:
            return self

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

    #players = fetchPlayers()
    players = [Player("Roman"), Player("George")]

    roundN = 1
    docket = docketGenerator(db, roundN)

    game(docket, players)



def priceNormalise(docket, roundN):
    for n,i in enumerate(docket):
        i.value = ([200,400,600,800,1000][n%5])*roundN
    return docket

def docketGenerator(db, roundN):
    categories = sample(set([i.fetchRoundUID(roundN) for i in db if i.round == roundN]),5)
    return priceNormalise([i.isSelected(categories) for i in db if i.isSelected(categories) != None], roundN)

def fetchPlayers():
    players = []
    while True:
        x = input("Enter player name, or 'start' to begin. ")
        if x == "start":
            break
        players.append(Player(x))
    return players

def game(docket, players):
    topics = [i for i in set([i.topic for i in docket])]
    print("TONIGHT'S TOPICS ARE...")
    print(", ".join(topics))
    docket = np.array(docket).reshape(5,5)

if __name__ == "__main__":
    main()
from csv import reader
from random import sample

class Question:
    def __init__(self, line):
        self.id = line[0]
        if line[1]=="Jeopardy!":
            self.round=1
        else:
            self.round=2
        self.topic=line[2]
        self.value=int(line[3]) if int(self.id) > 3966 else int(line[3]) * 2
        self.question=line[4]
        self.answer=line[5]
    
    def __repr__(self):
        return "\nTopic: {}, {}, {}, {}".format(self.topic,self.round,self.value,self.question)

    def returnUID(self, roundN):
        return (self.id,self.round,self.topic) if self.round == roundN else None
    
    def isSelected(self, uIDs):
        if (self.id,self.round,self.topic) in uIDs:
            return self


def main():
    with open('sample.csv', encoding='utf8') as dbraw:
        db = [Question(i) for i in list(reader(dbraw))]
    roundGenerator(db, 1)

def roundGenerator(db, roundN):
    categories = sample(set([i.returnUID(roundN) for i in db if i.round == roundN]),5)
    print([i.isSelected(categories) for i in db if i.isSelected(categories) != None])

if __name__ == "__main__":
    main()
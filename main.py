import csv
class Question:
    def __init__(self, line):
        print(line)
        self.id = line[0]
        if line[1]=="Jeopardy!":
            self.round=1
        else:
            self.round=2
        self.topic=line[2]
        self.value=line[3]
        self.question=line[4]
        self.answer=line[5]

def main():
    db = []
    with open('sample.csv', encoding='utf8') as dbraw:
        for i in list(csv.reader(dbraw)):
            db.append(i)

if __name__ == "__main__":
    main()
import csv
import pandas as pd
dbRead = open('db.csv', "r", newline='', encoding='utf8')
db = list(csv.reader(dbRead, delimiter=","))
for n,row in enumerate(db[1:]):
        row[-2]=sum(i.count(row[-1]) for i in db)
        print("Line {} of {}".format(n+1,len(db)),end="\r",flush=True)
df=pd.DataFrame(data=db)
df.to_csv('db.csv', sep=",", encoding='utf8')
import csv
import pandas as pd
dbRead = open('db.csv', "r", newline='', encoding='utf8')
db = list(csv.reader(dbRead, delimiter=","))
for row in db[1:]:
        row[-2]=sum(i.count(row[-1]) for i in db)
df=pd.DataFrame(data=db)
df.to_csv('db.csv', sep=",", encoding='utf8')
import csv
import pandas as pd
dbRead = open('db.csv', "r", newline='', encoding='utf8')
db = list(csv.reader(dbRead, delimiter=","))
for i in db:
    if int(i[-2])%5!=0:
        i[-2]="delete_this"
df=pd.DataFrame(data=db)
df.to_csv('db.csv', sep=",", encoding='utf8')
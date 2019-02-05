import csv
import pandas as pd
dbRead = open('db_sample.csv', "r", newline='', encoding='utf8')
initial=1
db = list(csv.reader(dbRead, delimiter=","))
for i in db[1:]:
    if int(i[-1])%5!=0:
        i[-1]="delete_this"
df=pd.DataFrame(data=db)
df.to_csv('db_sample.csv', sep=",", encoding='utf8')
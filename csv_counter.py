import csv
import pandas as pd
from tqdm import tqdm
dbRead = open('db.csv', "r", newline='', encoding='utf8')
db = list(csv.reader(dbRead, delimiter=","))
column = [row[-1] for row in db]
for row in tqdm(db[1:]):
        row[-2]=sum(i.count(row[-1]) for i in column)
df=pd.DataFrame(data=db)
df.to_csv('db.csv', sep=",", encoding='utf8')
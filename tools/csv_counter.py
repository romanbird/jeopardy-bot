import csv
import pandas as pd
from tqdm import tqdm
from collections import Counter
dbRead = open('db.csv', "r", newline='', encoding='utf8')
db = list(csv.reader(dbRead, delimiter=","))
column = [row[-1] for row in db]
for row in tqdm(db):
    row[-2]=Counter(column)[row[-1]]
df=pd.DataFrame(data=db)
df.to_csv('db.csv', sep=",", encoding='utf8')
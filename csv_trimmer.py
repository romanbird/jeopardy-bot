import csv
dbRaw = open('db_sample.csv', "w+", newline='', encoding='utf8')
initial=1
db = list(csv.reader(dbRaw, delimiter=","))
for i in db[1:]:
    if int(i[-1])%5!=0:
        i[-1]="delete_this"
writer=csv.writer(dbRaw, delimiter=",")
writer.writerows(db)

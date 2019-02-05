import csv
with open('db_sample.csv', "r+", newline='', encoding='utf8') as dbRaw:
    initial=1
    db = list(csv.reader(dbRaw, delimiter=","))
    for i in db[1:]:
        if int(i[-1])%5!=0:
            i[-1]="delete_this"
    writer=csv.writer(dbRaw)
    writer.writerows(db)

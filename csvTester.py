import csv

with open("mainResult.txt-01.csv", 'r') as csvFile:
    csvRead = csv.reader(csvFile)

    for i in range(4):
        next(csvRead)

    for line in csvRead:
        csv.writer(line)
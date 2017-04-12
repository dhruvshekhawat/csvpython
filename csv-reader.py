import csv

f = open('imports-85.csv', 'a')
writer = csv.writer(f)

writer.writerow(('title1', 'title2', 'title3'))

f.close()
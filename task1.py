import csv


f = open('imports-85.csv', 'r')

myreader = csv.reader(f)

row = [r for r in myreader]

for r in row:
	if(r[2]=='chevrolet' and r[6]=='hatchback'):
		r[25] = int(r[25]) + 1000


f.close()

f = open('imports-85.csv', 'w')
writer = csv.writer(f)
for i in range(len(row)):
	writer.writerow(row[i])

f.close()

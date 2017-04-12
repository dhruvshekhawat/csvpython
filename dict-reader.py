import csv

f = open('imports-85.csv', 'r')
reader = csv.reader(f)
row = [r for r in reader]

fieldnames = row[0]

f.close()

f = open('imports-85.csv', 'r')
reader = csv.DictReader(f)

row = [r for r in reader]

for r in row:
	if(r['make']=='chevrolet' and r['body-style']=='hatchback'):
		r['price'] = int(r['price']) + 1000


f.close()
'''
fieldnames = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location',\
	'wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio',\
	'horsepower','peak-rpm','city-mpg','highway-mpg','price']
'''
f = open('imports-85.csv', 'w')
writer = csv.DictWriter(f, fieldnames = fieldnames)
writer.writeheader()
for i in range(len(row)):
	writer.writerow(row[i])

f.close()
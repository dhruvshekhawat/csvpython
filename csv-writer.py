import csv

f = open('date_output.csv', 'wt')

writer = csv.writer(f)
writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
for i in range(10):
	writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )

f.close()
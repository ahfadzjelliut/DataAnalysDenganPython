import requests
from contextlib import closing
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
url = 'https://opendata.limapuluhkotakab.go.id/download/c01e5dc1d2b9467a944519ec10c45862.csv'

# baca file csv secara streaming
with closing(requests.get(url, stream=True)) as r:
	f = (line.decode('utf-8') for line in r.iter_lines())
	
	reader = csv.reader(f, delimiter=',')
	
	# membaca baris perbaris
	for row in reader:
		print(row)

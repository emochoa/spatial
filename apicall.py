import urllib3
import json
from sys import argv

# Not entirely sure what this does, but trying it anyway.
script, fips.txt = argv

rawdata = []
uri = []
fips = []

http = urllib3.PoolManager()

start = 'http://data.fcc.gov/api/block/2010/find?format=json&latitude='
mid = '&longitude='

cols, locations = read_file('homicides-lat-long.csv')

lat = locations[:,0]
lon = locations[:,1]

size = len(lat)



for i in range(size):
   uri.append(start + lat[i] + mid + lon[i]) 

json.loads(r.data.decode('utf-8'))

for addr in uri:
    datum = http.request('GET', addr)
    clean_datum = json.loads(datum.data.decode('utf-8'))
    fips.append(clean_datum['Block']['FIPS']

fipsout = open(filename, 'w')

for item in fips:
    fipsout.write(item)
    fipsout.write('\n')

fipsout.close()

import numpy as np
import urllib3
import json
from sys import argv

#Modified from code given to us for PA5 in CS121
def read_file(filename):
    '''
    Read data from the specified file.  Split the lines and convert
    float strings into floats.  Assumes the first row contains labels
    for the columns.

    Inputs:
      filename: name of the file to be read

    Returns:
      (list of strings, 2D array)
    '''
    with open(filename) as f:
        labels = f.readline().strip().split(',')
        data = np.loadtxt(f, delimiter=',')#, dtype=np.float64)
        return labels, data


uri = []
fips = []

http = urllib3.PoolManager()

start = 'http://data.fcc.gov/api/block/2010/find?format=json&latitude='
mid = '&longitude='

cols, locations = read_file('homicides-lat-long2.csv')

cno = locations[:,0]
lat = locations[:,1]
lon = locations[:,2]

size = len(lat)

print("lat and lon created; size = ",size)


for i in range(size):
   uri.append(tuple(cno,start + str(lat[i]) + mid + str(lon[i]) ) )


print("\nuri created; len(uri) =",len(uri))

#json.loads(r.data.decode('utf-8'))

i = 0

for line in uri:
    i += 1
    cno = line[0]
    addr = line[1]
    datum = http.request('GET', addr)
    clean_datum = json.loads(datum.data.decode('utf-8'))
    fips.append(tuple(cno, clean_datum['Block']['FIPS']))
    if i % 100 == 0:
    	print("\tinside fips-creation for-loop; i = ",i)

print("\nfips created; len(fips) =", len(fips))

fipsout = open("fips2.txt", 'w')

for item in fips:
    fipsout.write(str(item))
    fipsout.write('\n')

fipsout.close()

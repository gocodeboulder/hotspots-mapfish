import psycopg2, ppygis, csv
from decimal import *

f = csv.DictReader(open('Cellular_Performance_Ag.csv', mode='rt', ), skipinitialspace=True)
db = psycopg2.connect(database='hotspotmapfish', user='gocode')
c=db.cursor()

nullchar = "NA"

c.execute('CREATE TABLE cellular_performance('
          'latitude NUMERIC, longitude NUMERIC, downloadSpeed NUMERIC, '
          'latencyAverage NUMERIC, deviceSignalStrength NUMERIC, uploadSpeed NUMERIC, '
          'geom GEOGRAPHY(POINT,4326), )')
for row in f:
    for i in row.iteritems():
        if i == nullchar:
            i = None
    print row
    #c.execute('
    c.execute('INSERT INTO cellular_performance VALUES(%s, %s, %s, %s, %s,)',
              (Decimal(row['downloadSpeed']), Decimal('latencyAverage'), Decimal('deviceSignalstrength'),
               ppygis.Gppygis.Point(row['Latitude'], row['Longitude']) ))
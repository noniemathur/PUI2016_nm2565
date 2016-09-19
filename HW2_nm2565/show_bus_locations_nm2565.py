from __future__ import print_function
import pylab as pl
import json
import urllib as urllib
import sys

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1] + '&VehicleMonitoringDetailLevel=calls&LineRef=' + sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

bus_line = 'Bus line: B52'
busesonroad = len(location)
print (bus_line)
print ('Number of active buses:' , busesonroad)

w = 0
for i in location:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus',w,'is at latitude', latitude, 'and longitude', longitude) 
    w = w + 1

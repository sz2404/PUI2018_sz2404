#System and packages set up
from __future__ import print_function
import numpy as np
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
#from sys import argv

#mykey = sys.argv[1]
#busline = sys.argv[2]

#Direct link to mta bus real-time data

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
print (url)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#data.keys()

#In the JSON file, after key 'VehicleActivity', the active bus are listed. 
#Q102 shows to display the current activites of on duty buses at the type of download. 
#BusN extracts the number of on duty buses through finding the length of VehicleActivity container. 
#== is for checking and = is for assigning a value. 
#Select Bus Services Reference: http://web.mta.info/nyct/service/bus/mhtnsch.htm

try: 
    Q102bus=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    BusN=len(Q102bus)

except KeyError:
    Q102bus="Select Bus Service"
    BusN=0
    if BusN==0:
        print("Select Bus Service")
#np.nan will return "not a number".

#Print the information as directed in the instruction. First two lines are bus information.
print("Bus Line:" + sys.argv[2])
print("The Number of Vehicles: " + str(BusN))

#Print the activie bus locations.


for i in range(BusN):
    
    try:
        Long = Q102bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        Lat = Q102bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    
    except KeyError:
        Long = "N/A"
        Lat = "N/A"

    print("Bus", str(i), "is at Latitude ", Lat, "and Longitude", Long)


              
             
              




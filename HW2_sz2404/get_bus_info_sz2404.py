from __future__ import print_function
import json
import csv
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

#Load JSON data first.

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
print (url)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#Set up for open and writing
fout=open(sys.argv[3], "w")



#Set up initial

try:
    Q102bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    BusN = len(Q102bus)
except KeyError:
    Q102bus = "Select bus service"
    BusN = 0
    if BusN == 0:
        print("Select bus service")

#Print column title
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

#Set up catching onwardcall information and print

for i in range (BusN):

    try:
        StopName = Q102bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        Status = Q102bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    
    except KeyError:
        StopName = 'N/A'
        Status = 'N/A'
  
    Long = Q102bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Lat = Q102bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    
#print(Lat, Long, StopName, Status)
#Reference for converting list to a string: https://www.quora.com/In-Python-how-do-you-convert-a-list-to-a-string

    businfo = (str(Lat), str(Long), str(StopName), str(Status)+"\n")
    bi = str(','.join(businfo))
    fout.writelines(bi)

fout.close()
    
    




#!/usr/bin/env python3
import requests
import json
import time
#setup
timestr = time.strftime("%Y-%m-%d___%H:%M:%S")
API_KEY="--API KEY---"
# DEBUG url = "https://aviation-edge.com/v2/public/airplaneDatabase?key="
url2 = "http://aviation-edge.com/api/public/flights?&key="
# DEBUG airline = "&codeIataAirline=AA"
aircode =  "&airlineicaoCode="
stat = "&status=en-route" #only pulls those en-route
limiter = "&limit=30000"
airline = ['AAL','BAW','CPA','FIN','IBE','JAL','LAN','MAS','GFA','QTR','RJA','SBI','ALK']
#airline = ['BAW']
#res = requests.get('https://aviation-edge.com/v2/public/airplaneDatabase?key='+API_KEY+'&codeIataAirline=AA')
#x = requests.get(url+API_KEY+airline)

#####Feeds airline icao code to the API and pulls back data
def print_data(airline):
   x = requests.get(url2+API_KEY+limiter+aircode+airline+stat) ###THIS PULLS THE {AIRLINE} WITH ENROUTE STATUS
   #print(x.text) DEBUG
   f = open("/shared/sos/json/geo/"+airline+".json", "w") ### Writes the data to the JSON
   f.write(x.text)
   f.close()

####Filters the JSON files for the parts we want, lat long flight#
def json_filter(airline):
    with open('/shared/sos/json/geo/'+ airline +'.json') as f:
      data = json.load(f)
      x = len(data)
      print(x)
      for d in range(0,x):
            #print (data[d]["aircraft"])               ######DEBUG
            lat = (data[d]["geography"]["latitude"])
            lon = (data[d]["geography"]["longitude"])
            fli = (data[d]["flight"]["icaoNumber"])
            #print (data[d]["geography"]["latitude"])  ######DEBUG
            #print (data[d]["geography"]["longitude"]) ######DEBUG
            #print (data[d]["flight"]["icaoNumber"])   ######DEBUG
            zed = open(airline + '.csv', 'a')
            #print (fli,",",lat,",",lon )
            print (str(fli) + "," + str(lat) + "," + str(lon) + "\n", file = zed)
            #zed.close()
            line = (str(fli) + "," + str(lat) +"," + str(lon) +"\n" )
            print (line)
            log = open('/shared/sos/json/geo/' + airline + ".csv","a")
            log.writelines(str(fli) + "," + str(lat) +"," + str(lon) + "\n")
            log = open('/shared/sos/json/geo/ALL.csv',"a")
            log.writelines(str(fli) + "," + str(lat) +"," + str(lon) + "\n")

for z in airline:
    print(timestr)
    print_data(z)
    json_filter(z)
    log = open("/shared/sos/json/logs/AVedge.txt","a")
    log.writelines("PULLED----" + z + "----" + timestr +"\n")
    print(z)
    log.close()

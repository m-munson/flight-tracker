#!/usr/bin/env python3
import requests
import json
import time
#setup
timestr = time.strftime("%Y-%m-%d___%H:%M:%S") ### (YEAR)-(MONTH)-(DAY)___(HOUR):(MIN):(SEC)
API_KEY="--API KEY---"
url2 = "http://aviation-edge.com/api/public/flights?&key="
aircode =  "&airlineicaoCode="
stat = "&status=en-route" ###only pulls those en-route
limiter = "&limit=30000"  ###Limits to 30K records
airline = ['AAL','BAW','CPA','FIN','IBE','JAL','LAN','MAS','GFA','QTR','RJA','SBI','ALK']
#airline = ['BAW'] ### DEBUG --runs BAW solo


#####Feeds airline icao code to the API and pulls back data and write to a JSON files. 
def print_data(airline):
   x = requests.get(url2+API_KEY+limiter+aircode+airline+stat) ###THIS PULLS THE {AIRLINE} WITH ENROUTE STATUS
   #print(x.text) ### DEBUG -- will puke the json data to terminal
   f = open("/shared/sos/json/geo/"+airline+".json", "w") ### Opens the json file
   f.write(x.text) ## Pukes the data in to a file
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
            #print (data[d]["geography"]["latitude"])  ######DEBUG --will print this as a line to terminal
            #print (data[d]["geography"]["longitude"]) ######DEBUG --will print this as a line to terminal
            #print (data[d]["flight"]["icaoNumber"])   ######DEBUG --will print this as a line to terminal
            zed = open(airline + '.csv', 'a')
            #print (fli,",",lat,",",lon )
            print (str(fli) + "," + str(lat) + "," + str(lon) + "\n", file = zed)
            #zed.close()
            line = (str(fli) + "," + str(lat) +"," + str(lon) +"\n" )
            print (line)
            log = open('/shared/sos/json/geo/' + airline + ".csv","a") #### Appends the line to the {airline}.CSV
            log.writelines(str(fli) + "," + str(lat) +"," + str(lon) + "\n")
            log = open('/shared/sos/json/geo/ALL.csv',"a")             #### Appends the line to the cumulative.CSV
            log.writelines(str(fli) + "," + str(lat) +"," + str(lon) + "\n")

for z in airline:
    print(timestr) 
    print_data(z)
    json_filter(z)
    log = open("/shared/sos/json/logs/AVedge.txt","a") ## opens log file
    log.writelines("PULLED----" + z + "----" + timestr +"\n") ## writes to log file
    print(z)
    log.close()

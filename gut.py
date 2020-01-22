#!/usr/bin/env python

import time
#setup
timestr = time.strftime("%Y-%m-%d___%H:%M:%S")
### LIST OF AIRLINES
airline = ['UAL','BAW','CPA','FIN','IBE','JAL','LAN','MAS','GFA','QTR','RJA','SBI','ALK']
###OPENS AND FLUSHES THE FILES
def clear_data(airline):
   f = open("/shared/sos/json/geo/"+airline+".json", "w").close()
   f = open("/shared/sos/json/geo/"+airline+".csv", "w").close()
   f = open("/shared/sos/json/geo/ALL.csv", "w").close()

for z in airline:
    clear_data(z)
    log = open("/shared/sos/json/logs/AVedge.txt","a")
    log.writelines("GUTTED----" + z + "----" + timestr +"\n")
    f = open("/shared/sos/json/geo/ALL.csv", "w").close()
    log.writelines("GUTTED----ALL.CSV----" + timestr +"\n")
    log.close()

#!/usr/bin/env python3
import matplotlib as mpl
mpl.use('Agg') ##lets me run this in cron
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook
#import matplotlib.image as mpimg
from datetime import datetime
import time
import csv
import os
from PIL import Image

lats,lons,names = [],[],[]
print ("CREATING MAP")
# miller projection
plt.figure(figsize=(13,6.5))
timestr = time.strftime("%Y-%m-%d  %H:%M")
map = Basemap(projection='cyl')#, resolution= None#ax=axes  area_thresh=None
# plot coastlines
map.drawcoastlines(linewidth=0.1, color='k')
#map.drawmapboundary(fill_color='#1300af')
map.drawmapboundary(fill_color='#0080ff')
map.fillcontinents(color='#333333',lake_color='#0080ff')
map.drawrivers(linewidth=0.1, linestyle='solid', color='k')
map.drawcountries(linewidth=0.15, linestyle='solid', color='grey', antialiased=1, ax=None, zorder=None)
# shade the night areas, with alpha transparency so the
# map shows through. Use current time in UTC.
### PULLS DATA FROM CSV >>>FLIGHT,LAT,LON

with open('/shared/sos/json/geo/ALL.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for data in reader:
        names.append(str(data[0]))
        lats.append(float(data[1]))
        lons.append(float(data[2]))
x,y = map(lons,lats)
#x,y,name = map(lons,lats,names)
#name = map(names)
map.plot(x,y,'r*',markersize=0.05,color='white',marker=',')
#plt.text(x,y,name, fontsize=4,color='grey')

with open('/shared/sos/json/geo/AAL.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for data in reader:
        names.append(str(data[0]))
        lats.append(float(data[1]))
        lons.append(float(data[2]))
f,g = map(lons,lats)
map.plot(f,g,'r*',markersize=0.02,color='#FF2400',marker=',')

#plt.imshow(plt.imread('/shared/sos/json/legend.png'),  extent = (x0, x1, y0, y1))
a,b = map(-30,-15)
plt.text(a,b,timestr, fontsize='xx-small',color='white')    ##########TIMESTAMP FOR MAP >>ATLANTIC<<
plt.text(a-120,b,timestr, fontsize='xx-small',color='white')    ##########TIMESTAMP FOR MAP >>Pacific<<
plt.text(a+118,b,timestr, fontsize='xx-small',color='white')    ##########TIMESTAMP FOR MAP >>INDIAN<<

m, n = map(-20, -20)
#img = mpimg.imread('/shared/sos/json/legend.png')
#m.imshow(img, extent=(m,m-10,n,n-20)




log=open("/shared/sos/json/logs/AVedge.txt","a")
log.writelines("GENERATED----MAP ----" + timestr +"\n")
#x, y = map(40.8228,47.9151)
#plt.plot(x, y, marker='D',color='yellow',markersize=1)

date = datetime.utcnow()
CS=map.nightshade(date)

#plt.title('Day/Night Map for %s (UTC)' %strftime("%d %b %Y %H:%M:%S"))
#plt.show()
plt.savefig( '/shared/sos/json/dataset/'+timestr+".png", bbox_inches = 'tight', pad_inches = -0.037, dpi=200)
plt.savefig( "/shared/sos/json/dataset/flights.png", bbox_inches = 'tight', pad_inches = -0.037, dpi=200)

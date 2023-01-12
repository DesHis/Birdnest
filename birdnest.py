import requests
import xml.etree.ElementTree as ElementTree
import math 
import json 
import time


violators=[]
while True:


    #get data from GET request and parse into tree
    response = requests.get("http://assignments.reaktor.com/birdnest/drones")
    try:
        tree = ElementTree.fromstring(response.content)
        capture=tree.find("capture")
    except:
        print("404 error")


    #if drone is within the circle, add its pilot data to violators list
    circleCenter=[250000, 250000]
    for drone in capture:
        dronePosition=[float(drone.find("positionX").text), float(drone.find("positionY").text)]
        distanceFromNest=math.dist(circleCenter, dronePosition)
        if(distanceFromNest<=100000):
            try:
                AlreadyAdded=False
                serialNumber=drone.find("serialNumber").text
                violatorResponse = requests.get("http://assignments.reaktor.com/birdnest/pilots/"+serialNumber)
                violatorData=json.loads(violatorResponse.content)
                pilotInfo=[violatorData["firstName"], violatorData["lastName"], violatorData["email"], violatorData["phoneNumber"], time.time(), distanceFromNest, serialNumber]

                for v in violators: #check if pilot has violated before
                    if(v[6]==serialNumber):
                        if(distanceFromNest<=v[5]): #update closest distance 
                            v[5]=distanceFromNest
                        AlreadyAdded=True
                if(not AlreadyAdded):
                    violators.insert(0, pilotInfo)

            except:
                print("404 error")


    #write violating pilot information to html file
    site1='<!DOCTYPE html><html lang="en"><head><title>Project Birdnest</title><meta http-equiv="refresh" content="2"></head><body><main><h1>Project Birdnest</h1> <h2> Recent violators:</h2>'
    site2='</main></body></html>'
    recentViolators=""  

    for pilotInfo in violators:

        if(time.time()-pilotInfo[4]>600): #remove if older than 10 minutes 
            violators.remove(pilotInfo) 
        recentViolators+=str(int(time.time()-pilotInfo[4]))+" SECONDS AGO "
        for i in range(4):
            recentViolators+=str(pilotInfo[i])+" "
        recentViolators+="closest distance: "+str(int(pilotInfo[5])/1000)+" meters "
        recentViolators+="<br>"

    site = open("templates/index.html", "w")
    print("write to file templates/index.html")
    site.write(site1+recentViolators+site2)
    site.close

    print("eepy")
    #since the XML data is updated every 2 seconds, we can sleep to avoid spamming the server with unnecessary requests 
    time.sleep(2)
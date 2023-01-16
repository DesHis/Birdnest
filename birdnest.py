import requests
import xml.etree.ElementTree as ElementTree
import math
import json
import time
import os

violators=[]
dir_path = os.path.dirname(os.path.realpath(__file__))

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

    #write violating pilot information a json file
    recentViolators=""
    for pilotInfo in violators:
        if(time.time()-pilotInfo[4]>600): #remove if older than 10 minutes
            violators.remove(pilotInfo)
        recentViolators+=str(int(time.time()-pilotInfo[4]))+" SECONDS AGO "
        for i in range(4):
            recentViolators+=str(pilotInfo[i])+" "
        recentViolators+="closest distance: "+str(int(pilotInfo[5])/1000)+" meters "
        recentViolators+="<br>"

    json_object=json.dumps(recentViolators)
    with open(dir_path+"/violators.json", "w") as outfile:
        outfile.write(json_object)

    #since the XML data is updated every 2 seconds, we can sleep to avoid spamming the server with unnecessary requests
    time.sleep(2)
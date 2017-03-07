import serial
import pynmea2
import time

#Search for and open the correct GPS stream
def testStreams():
    for i in range(0, 5):
        try:
            serialStream = serial.Serial("/dev/ttyUSB"+str(i), 9600, timeout=0.5)
            sentance = serialStream.readline()
            if(sentance != None):
                break
        except:
            serialStream = None
    return serialStream

def getGPSStream():
    actualGPS = 0
    while (actualGPS == 0):
        serialStream = testStreams()
        if(serialStream == None):
            print "GPS module not found"
            time.sleep(2)
        else:
            actualGPS = 1
    print "Found GPS Module"
    return serialStream

def getRMCData(GPSStream):
    found = 0
    while (found == 0):
        try:
            sentance = GPSStream.readline()
            gpsData = pynmea2.parse(sentance)
            if "RMC" in sentance:
                found = 1
                return gpsData
        except:
            print "could not parse string"

def loop():
    GPSStream = getGPSStream()
    RMCData = getRMCData(GPSStream)
    print RMCData.lat


#Main function
if __name__ == "__main__":
    while(True):
        loop()

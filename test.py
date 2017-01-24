import serial
import pynmea2

def test():
    serialStream = serial.Serial("/dev/ttyUSB1", 9600, timeout=0.5)

    while True:
        sentance = serialStream.readline()
        if sentance.find('RMC') > 0:
            if hasattr(sentance, 'lon'):
                print sentance


#Main function
if __name__ == "__main__":
    test()

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blink(pin):
    print("ON")
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    print("OFF")
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

def checkBattSense(sensePin):
    sensorValue = GPIO.input(sensePin)
    connected = 0
    
    if sensorValue == 0:
        for i in range(0,50):
            sensorValue = GPIO.input(sensePin)
            if sensorValue == 1:
                connected = 1
            time.sleep(0.01)
    else:
        connected = 1
    return connected
                

#Main function
if __name__ == "__main__":
    os.system("./sleep.sh")
    while True:
        connected = checkBattSense(16)
        print "Value: " + str(connected)
        if(connected == 0):
            time.sleep(3)
            connected = checkBattSense(16)
            if(connected == 0):
                print "Shutting down"
                os.system("sudo shutdown -h now")
        time.sleep(1)
    GPIO.cleanup()

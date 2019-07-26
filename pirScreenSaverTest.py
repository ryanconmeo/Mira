import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)


while True:
        i=GPIO.input(11)
        if i==0: #When output from motion sensor is LOW
                print("No intruders", i)
                GPIO.output(3, 0) #Turn off LED
                time.sleep(1)
        elif i==1:
            print("Intruder detected")
            print ("Deactivating screensaver")
            os.system("xscreensaver-command -deactivate")
            GPIO.output(3, 1)


            time.sleep(1)
            
        

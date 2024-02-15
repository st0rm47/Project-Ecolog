#####Testing LEFT####
import RPI.GPIO as GPIO
import time

#Setting up GPIO
GPIO.setmode(GPIO.BCM)

#Setting up the gas sensor pin
DOUT_PIN= 26

GPIO.setup(DOUT_PIN, GPIO.IN)

#Reading the gas sensor value
try:
    while True:
        # Reading the state of the digital output pin
        digital_value = GPIO.input(DOUT_PIN)
        
        #Threshold Value
        threshold = 200

        if digital_value == GPIO.LOW or digital_value > threshold:
            print("Smoke Detected")
        else:
            print("No Smoke Detected")       
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Cleaning up")
finally:
    GPIO.cleanup()
    
    
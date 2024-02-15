#####Testing LEFT####


###Connecting gas sensor to Raspberry Pi
import RPI.GPIO as GPIO

#Setting up GPIO
GPIO.setmode(GPIO.BCM)

#Setting up the gas sensor pin
DOUT_PIN= 17
GPIO.setup(DOUT_PIN, GPIO.IN)

#Reading the gas sensor value
try:
    while True:
        print(GPIO.input(DOUT_PIN))
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()
    
    
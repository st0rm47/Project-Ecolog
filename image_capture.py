import cv2
import numpy as np
import time
import datetime
import requests
import argparse
import RPi.GPIO as GPIO
from azure.storage.blob import BlobServiceClient

def camera():
    #Set up buzzer
    GPIO.setmode(GPIO.BCM)
    buzzer = 23
    GPIO.setup(buzzer, GPIO.OUT)
    
    #Azure Storage
    

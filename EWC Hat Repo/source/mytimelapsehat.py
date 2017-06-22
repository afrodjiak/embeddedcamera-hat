import picamera
import picamera.array
import numpy as np
import time
import datetime

from time import sleep
from picamera import PiCamera

cam = picamera.PiCamera()
cam.resolution = (1024, 768)
cam.hflip = True
cam.vflip = True

cam.start_preview()
cam.stop_preview()
time.sleep(2)
for filename in cam.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print ('Captured %s' % filename)
    time.sleep(10)

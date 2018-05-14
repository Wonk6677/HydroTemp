#!/usr/bin/python
import sys
import Adafruit_DHT
import datetime
import RPi.GPIO as GPIO
from time import sleep

sleepTime = 60

while True:
    delta = datetime.timedelta(minutes=10)
    next_time = datetime.datetime.now()
    dt = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    print dt
    sleep(sleepTime)
# Save Result Every One Hour
    if dt > next_time:
        file = open("/home/pi/Desktop/temp.txt", "w")
        file.write(str(dt) + '\n')
        file.write('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        file.close()
        next_time = dt + delta

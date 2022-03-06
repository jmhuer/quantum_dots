#import matplotlib.pyplot as plt
import time
import board
import busio
#import digitalio
#import csv
#from adafruit_as726x import Adafruit_AS726x
from adafruit_as7341 import AS7341
#from tkinter import *
#import tkinter.font
import statistics


#Initialize the LED
#led = digitalio.DigitalInOut(board.D13)
#led.direction= digitalio.Direction.OUTPUT

#Initialize i2c and sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = AS7341(i2c)
#sensor.conversion_mode = sensor.MODE_2

l = 1
channel_415nm = 0
channel_445nm = 0
channel_480nm = 0
channel_515nm = 0
channel_555nm = 0
channel_590nm = 0
channel_630nm = 0
channel_680nm = 0
    
channel_415nmList = []
channel_445nmList = []
channel_480nmList = []
channel_515nmList = []
channel_555nmList = []
channel_590nmList = []
channel_630nmList = []
channel_680nmList = []
    
#time.sleep(0.2)

while l <= 5:
    channel_415nm = int(sensor.channel_415nm)
    channel_415nmList.insert(0,channel_415nm)
        
    channel_445nm = int(sensor.channel_445nm)
    channel_445nmList.insert(0,channel_445nm)
        
    channel_480nm = int(sensor.channel_480nm)
    channel_480nmList.insert(0,channel_480nm)
        
    channel_515nm = int(sensor.channel_515nm)
    channel_515nmList.insert(0,channel_515nm)
        
    channel_555nm = int(sensor.channel_555nm)
    channel_555nmList.insert(0,channel_555nm)
        
    channel_590nm = int(sensor.channel_590nm)
    channel_590nmList.insert(0,channel_590nm)
        
    channel_630nm = int(sensor.channel_630nm)
    channel_630nmList.insert(0,channel_630nm)
        
    channel_680nm = int(sensor.channel_680nm)
    channel_680nmList.insert(0,channel_680nm)
        
    #time.sleep(.2)
    l+=1
        
avgchannel_415nm = statistics.mean(channel_415nmList)
avgchannel_445nm = statistics.mean(channel_445nmList)
avgchannel_480nm = statistics.mean(channel_480nmList)
avgchannel_515nm = statistics.mean(channel_515nmList)
avgchannel_555nm = statistics.mean(channel_555nmList)
avgchannel_590nm = statistics.mean(channel_590nmList)
avgchannel_630nm = statistics.mean(channel_630nmList)
avgchannel_680nm = statistics.mean(channel_680nmList)

print("Light on, 27.20mA, 8/15 cuvette 15 30nM 620 + 30nM 560 5min")
print("415 = %s" % avgchannel_415nm)
print("445 = %s" % avgchannel_445nm)
print("480 = %s" % avgchannel_480nm)
print("515 = %s" % avgchannel_515nm)
print("555 = %s" % avgchannel_555nm)
print("590 = %s" % avgchannel_590nm)
print("630 = %s" % avgchannel_630nm)
print("680 = %s" % avgchannel_680nm)


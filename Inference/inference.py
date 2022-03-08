# #import matplotlib.pyplot as plt
import time
import board
import busio
# #import digitalio
# #import csv
# #from adafruit_as726x import Adafruit_AS726x
from adafruit_as7341 import AS7341
# #from tkinter import *
# #import tkinter.font
# import statistics
from utils import Data
# load the model from disk
import pickle
import numpy as np
#Initialize the LED
# #led = digitalio.DigitalInOut(board.D13)
# #led.direction= digitalio.Direction.OUTPUT
#
# #Initialize i2c and sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = AS7341(i2c)
# #sensor.conversion_mode = sensor.MODE_2
#


import warnings
warnings.filterwarnings('ignore')

from models import lr_reg 


def load_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model


def inference(model, X):
    '''
    This function wraps the sklearn inference since we need slighly different steps for some models
    :param model:
    :param X:
    :return: results
    '''
    result = model.predict(X.reshape(-1,1).T)
    return result

d = Data()

model = load_model("finalized_model.sav")
print(model)
while True:
    _ = input("Press Enter to collect datapoint")
    for i in range(5):
        datapoint = {"415nm": int(sensor.channel_415nm),
                     "445nm": int(sensor.channel_445nm),
                     "480nm": int(sensor.channel_480nm),
                     "515nm": int(sensor.channel_515nm),
                     "555nm": int(sensor.channel_555nm),
                     "590nm": int(sensor.channel_590nm),
                     "630nm": int(sensor.channel_630nm),
                     "680nm": int(sensor.channel_680nm)
                     }
        d.add(datapoint)
    latest_running_mean = d.make_smooth_dataset()[0:,-1]
    print(latest_running_mean)
    #model inference
    Y = inference(model,latest_running_mean)
    print(Y)

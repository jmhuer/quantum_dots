# #import matplotlib.pyplot as plt
# import time
# import board
# import busio
# #import digitalio
# #import csv
# #from adafruit_as726x import Adafruit_AS726x
# from adafruit_as7341 import AS7341
# #from tkinter import *
# #import tkinter.font
# import statistics
from Inference.utils import Data
# load the model from disk
import pickle

#Initialize the LED
# #led = digitalio.DigitalInOut(board.D13)
# #led.direction= digitalio.Direction.OUTPUT
#
# #Initialize i2c and sensor
# i2c = busio.I2C(board.SCL, board.SDA)
# sensor = AS7341(i2c)
# #sensor.conversion_mode = sensor.MODE_2
#
from .models import lr_reg ,rf_reg ,svr, gp


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
    result = model.predict(X)
    return result

d = Data()

model = load_model("finalized_model.sav")
while True:
    _ = input("Press Enter to collect datapoint")
    datapoint = {"415nm": 1,
                 "445nm": 2,
                 "480nm": 3,
                 "515nm": 4,
                 "555nm": 5,
                 "590nm": 6,
                 "630nm": 7,
                 "680nm": 8
                 }
    d.add(datapoint)
    latest_running_mean = d.make_smooth_dataset()[0:,-1]
    print(latest_running_mean)
    #model inference
    Y = inference(model,latest_running_mean)
    print(Y)

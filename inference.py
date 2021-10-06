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
import numpy as np
from numpy.lib.stride_tricks import as_strided

#Initialize the LED
#led = digitalio.DigitalInOut(board.D13)
#led.direction= digitalio.Direction.OUTPUT

#Initialize i2c and sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = AS7341(i2c)
#sensor.conversion_mode = sensor.MODE_2



class Data:
    '''
    this class takes predictions and outputs running majority prediction
    '''
    def __init__(self, num_channels=8):
        self.history = {"415nm": [],
                        "445nm": [],
                        "480nm": [],
                        "515nm": [],
                        "555nm": [],
                        "590nm": [],
                        "630nm": [],
                        "680nm": []
                        }
        self.timesteps = 0
    def add(self, datapoint: dict):
        for name in datapoint.keys():
            self.history[name].append(datapoint[name])
        self.timesteps+=1
    def running_mean(self, image, kernel_size, stride):
        weight = np.ones((1, kernel_size))
        im_h, im_w = image.shape
        f_h, f_w = weight.shape
        out_shape = (1 + (im_h - f_h) // stride, 1 + (im_w - f_w) // stride, f_h, f_w)
        out_strides = (image.strides[0] * stride, image.strides[1] * stride, image.strides[0], image.strides[1])
        windows = as_strided(image, shape=out_shape, strides=out_strides)
        return np.tensordot(windows, weight, axes=((2, 3), (0, 1))) / kernel_size
    def get_smooth_data(self):
        num_channels = len(self.history.keys())
        data = np.array(self.timesteps, num_channels)
        for i, name in enumerate(self.history.keys()):
            data[i, :] = self.running_mean(np.array([self.history[name]]), kernel_size=5,stride=5)
        return data
    def print_lastpoint(self):
        data = self.get_smooth_data()
        print("415nm \n {}",
              "445nm: sensor.channel_445nm,
              "480nm": sensor.channel_480nm,
              "515nm": sensor.hannel_515nm,
              "555nm": sensor.channel_555nm,
              "590nm": sensor.channel_590nm,
              "630nm": sensor.channel_630nm,
              "680nm":")





while True:
    datapoint = {"415nm": sensor.channel_415nm,
                 "445nm": sensor.channel_445nm,
                 "480nm": sensor.channel_480nm,
                 "515nm": sensor.hannel_515nm,
                 "555nm": sensor.channel_555nm,
                 "590nm": sensor.channel_590nm,
                 "630nm": sensor.channel_630nm,
                 "680nm": sensor.channel_680nm
                 }





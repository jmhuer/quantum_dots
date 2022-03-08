import numpy as np
from numpy.lib.stride_tricks import as_strided
from scipy import signal

class Data:
    '''
    this class takes predictions and outputs running majority prediction
    '''
    def __init__(self):
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
        self.dataset = None
    def add(self, datapoint):
        for name in datapoint.keys():
            self.history[name].append(datapoint[name])
        self.timesteps+=1
    def running_mean(self, image, kernel_size=5, stride=5):
        weight = np.ones((1, kernel_size))
        im_h, im_w = image.shape
        if im_w < kernel_size:
            return np.array([image.mean()])[None]
        f_h, f_w = weight.shape
        out_shape = (1 + (im_h - f_h) // stride, 1 + (im_w - f_w) // stride, f_h, f_w)
        out_strides = (image.strides[0] * stride, image.strides[1] * stride, image.strides[0], image.strides[1])
        windows = as_strided(image, shape=out_shape, strides=out_strides)
        return np.tensordot(windows, weight, axes=((2, 3), (0, 1))) / kernel_size
    def get_smooth_data(self, kernel_size=3, stride=3):
        data = []
        for i, name in enumerate(self.history.keys()):
            a = np.array(self.history[name])[None]
            b =  self.running_mean(a, kernel_size=kernel_size,stride=stride)[0]
            data.append(b)
        self.dataset = np.array(data)
        return self.dataset
    def make_smooth_dataset(self):
        self.get_smooth_data()
        return self.dataset
    def print_lastpoint(self):
        s = " \n 415nm {} \n 445nm {} \n 480nm {} \n 515nm {} \n 555nm {} \n 590nm {} \n 630nm {} \n 680nm {} \n"
        print(s.format(*self.get_smooth_data()[:,-1]))






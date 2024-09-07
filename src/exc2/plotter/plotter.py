#Tobefinished

import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, startTime = 0, endTime = 100, step = 0.02):
        self.startTime = startTime
        self.endTime = endTime
        self.step = step
        self.t = np.arange(self.startTime, self.endTime, self.step)
        self.y = self.drawing(self.t)

        self.fig = plt.subplots()

    def drawing(self, t):
        lambda_t = 5*np.sin(2*np.pi*t)
        lambda_y = 3*np.pi*np.exp(-lambda_t)
        return lambda_y
    
class PlotterGUI


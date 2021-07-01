import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0, 3336)
y1= [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.8, 0.0, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.9, 0.9, 0.9, 0.8, 0.8, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.0, 0.0, 0.0, 0.8, 0.0, 0.8, 0.8, 0.0, 0.8, 0.8, 0.8, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.8, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.1, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
y2 = [0.725, 0.637, 0.657, 0.674, 0.674, 0.69, 0.69, 0.673, 0.673, 0.688, 0.673, 0.672, 0.673, 0.688, 0.674, 0.672, 0.657, 0.672, 0.657, 0.658, 0.657, 0.659, 0.648, 0.656, 0.638, 0.629, 0.657, 0.663, 0.657, 0.687, 0.653, 0.687, 0.664, 0.639, 0.674, 0.674, 0.672, 0.673, 0.668, 0.638, 0.69, 0.688, 0.687, 0.687, 0.671, 0.687, 0.687, 0.687, 0.687, 0.672, 0.672, 0.672, 0.664, 0.664, 0.669, 0.669, 0.669, 0.68, 0.68, 0.673, 0.69, 0.673, 0.658, 0.673, 0.657, 0.656, 0.656, 0.663, 0.663, 0.673, 0.688, 0.674, 0.653, 0.653, 0.673, 0.653, 0.653, 0.689, 0.689, 0.664, 0.689, 0.658, 0.658, 0.658, 0.674, 0.647, 0.657, 0.657, 0.648, 0.673, 0.669, 0.653, 0.669, 0.653, 0.652, 0.664, 0.654, 0.689, 0.689, 0.689, 0.69, 0.678, 0.688, 0.666, 0.672, 0.664, 0.673, 0.648, 0.655, 0.648, 0.656, 0.656, 0.656, 0.656, 0.656, 0.657, 0.657, 0.657, 0.657, 0.649, 0.673, 0.674, 0.673, 0.673, 0.689, 0.708, 0.709, 0.709, 0.709, 0.691, 0.709, 0.69, 0.709, 0.709, 0.692, 0.692, 0.672, 0.691, 0.683, 0.692, 0.684, 0.684, 0.689, 0.724, 0.688, 0.724, 0.673, 0.568, 0.504, 0.507, 0.484, 0.606, 0.653, 0.688, 0.658, 0.69, 0.674, 0.687, 0.674, 0.673, 0.673, 0.672, 0.689, 0.678, 0.688, 0.655, 0.674, 0.69, 0.709, 0.674, 0.674, 0.674, 0.674, 0.69, 0.653, 0.678, 0.674, 0.693, 0.709, 0.709, 0.674, 0.708, 0.708, 0.735, 0.7, 0.7, 0.681, 0.71, 0.69, 0.708, 0.708, 0.692, 0.692, 0.692, 0.698, 0.709, 0.666, 0.666, 0.666, 0.666, 0.675, 0.666, 0.666, 0.665, 0.666, 0.689, 0.688, 0.673, 0.674, 0.664, 0.674, 0.663, 0.644, 0.665, 0.645, 0.665, 0.646, 0.666, 0.666, 0.685, 0.685, 0.685, 0.685, 0.685, 0.688, 0.672, 0.672, 0.672, 0.663, 0.689, 0.673, 0.674, 0.689, 0.654, 0.708, 0.673, 0.673, 0.672, 0.664, 0.674, 0.664, 0.674, 0.674, 0.675, 0.674, 0.675, 0.684, 0.654, 0.551, 0.529, 0.544, 0.576, 0.56, 0.555, 0.517, 0.549, 0.556, 0.568, 0.558, 0.542, 0.521, 0.512, 0.492, 0.467, 0.486, 0.46, 0.484, 0.516, 0.502, 0.509, 0.499, 0.509, 0.483, 0.468, 0.484, 0.494, 0.485, 0.491, 0.492, 0.461, 0.486, 0.485, 0.505, 0.48, 0.521, 0.492, 0.497, 0.535, 0.521, 0.526, 0.525, 0.514, 0.504, 0.509, 0.498, 0.512, 0.521, 0.509, 0.502, 0.501, 0.48, 0.488, 0.514, 0.479, 0.497, 0.521, 0.477, 0.474, 0.516, 0.526, 0.481, 0.551, 0.507, 0.536, 0.501, 0.526, 0.51, 0.519, 0.514, 0.539, 0.502, 0.54, 0.55, 0.554, 0.509, 0.528, 0.508, 0.527, 0.526, 0.504, 0.521, 0.526, 0.527, 0.537, 0.554, 0.516, 0.546, 0.516, 0.54, 0.531, 0.553, 0.53, 0.556, 0.519, 0.573, 0.529, 0.552, 0.528, 0.551, 0.551, 0.552, 0.516, 0.551, 0.51, 0.537, 0.496, 0.538, 0.51, 0.561, 0.534, 0.527, 0.539, 0.525, 0.515, 0.553, 0.508, 0.542, 0.523, 0.558, 0.521, 0.54, 0.497, 0.55, 0.508, 0.535, 0.516, 0.539, 0.519, 0.58, 0.552, 0.544, 0.557, 0.583, 0.615, 0.659, 0.671, 0.687, 0.672, 0.726, 0.716, 0.764, 0.783, 0.766, 0.794, 0.763, 0.743, 0.749, 0.745, 0.773, 0.764, 0.766, 0.756, 0.731, 0.716, 0.7, 0.691, 0.691, 0.663, 0.666, 0.698, 0.709, 0.696, 0.688, 0.691, 0.686, 0.679, 0.678, 0.683, 0.696, 0.697, 0.695, 0.697, 0.68, 0.709, 0.709, 0.711, 0.715, 0.711, 0.695, 0.677, 0.697, 0.688, 0.682, 0.676, 0.684, 0.688, 0.676, 0.709, 0.657, 0.673, 0.645, 0.642, 0.663, 0.642, 0.702, 0.691, 0.65, 0.727, 0.618, 0.639, 0.686, 0.7, 0.717, 0.705, 0.687, 0.679, 0.727, 0.689, 0.701, 0.724, 0.8, 0.783, 0.686, 0.827, 0.872, 0.873, 0.878, 0.832, 0.881, 0.875, 0.892, 0.913, 0.921, 0.895, 0.82, 0.832, 0.79, 0.785, 0.713, 0.745, 0.731, 0.711, 0.757, 0.758, 0.76, 0.721, 0.722, 0.782, 0.794, 0.809, 0.803, 0.78, 0.834, 0.793, 0.817, 0.828, 0.64, 0.593, 0.595, 0.659, 0.721, 0.756, 0.786, 0.829, 0.795, 0.755, 0.779, 0.796, 0.796, 0.77, 0.772, 0.805, 0.791, 0.774, 0.781, 0.783, 0.758, 0.765, 0.751, 0.763, 0.736, 0.774, 0.752, 0.726, 0.65, 0.679, 0.741, 0.758, 0.705, 0.722, 0.734, 0.75, 0.738, 0.749, 0.764, 0.741, 0.727, 0.773, 0.758, 0.704, 0.733, 0.734, 0.699, 0.702, 0.683, 0.683, 0.709, 0.694, 0.713, 0.708, 0.7, 0.704, 0.784, 0.784, 0.724, 0.705, 0.761, 0.747, 0.709, 0.704, 0.708, 0.701, 0.673, 0.718, 0.732, 0.719, 0.607, 0.545, 0.528, 0.558, 0.629, 0.608, 0.641, 0.641, 0.655, 0.648, 0.654, 0.633, 0.644, 0.652, 0.667, 0.677, 0.682, 0.701, 0.669, 0.675, 0.649, 0.655, 0.674, 0.69, 0.68, 0.641, 0.683, 0.65, 0.653, 0.662, 0.671, 0.681, 0.673, 0.663, 0.686, 0.648, 0.61, 0.617, 0.645, 0.641, 0.631, 0.617, 0.602, 0.631, 0.621, 0.654, 0.621, 0.64, 0.654, 0.631, 0.659, 0.597, 0.602, 0.546, 0.506, 0.456, 0.434, 0.388, 0.406, 0.423, 0.479, 0.508, 0.534, 0.53, 0.497, 0.508, 0.52, 0.5, 0.533, 0.533, 0.564, 0.568, 0.572, 0.576, 0.593, 0.583, 0.589, 0.602, 0.623, 0.602, 0.641, 0.621, 0.59, 0.576, 0.591, 0.568, 0.608, 0.584, 0.541, 0.542, 0.568, 0.505, 0.546, 0.566, 0.562, 0.538, 0.495, 0.553, 0.577, 0.593, 0.592, 0.593, 0.593, 0.643, 0.625, 0.582, 0.623, 0.633, 0.612, 0.643, 0.61, 0.623, 0.624, 0.614, 0.648, 0.664, 0.717, 0.649, 0.684, 0.674, 0.669, 0.731, 0.682, 0.686, 0.71, 0.686, 0.698, 0.709, 0.695, 0.658, 0.671, 0.696, 0.685, 0.72, 0.671, 0.671, 0.653, 0.664, 0.639, 0.659, 0.626, 0.635, 0.672, 0.674, 0.667, 0.693, 0.674, 0.675, 0.674, 0.704, 0.659, 0.621, 0.672, 0.72, 0.868, 0.895, 0.944, 0.929, 0.883, 0.849, 0.828, 0.837, 0.804, 0.835, 0.785, 0.795, 0.787, 0.767, 0.796, 0.803, 0.782, 0.786, 0.723, 0.692, 0.673, 0.704, 0.713, 0.702, 0.738, 0.721, 0.718, 0.64, 0.681, 0.677, 0.644, 0.633, 0.641, 0.664, 0.652, 0.695, 0.668, 0.621, 0.62, 0.651, 0.675, 0.661, 0.677, 0.694, 0.708, 0.719, 0.702, 0.703, 0.688, 0.678, 0.549, 0.454, 0.397, 0.478, 0.589, 0.632, 0.648, 0.671, 0.665, 0.682, 0.68, 0.686, 0.68, 0.702, 0.687, 0.712, 0.718, 0.687, 0.687, 0.655, 0.686, 0.655, 0.68, 0.68, 0.672, 0.631, 0.617, 0.664, 0.656, 0.656, 0.666, 0.617, 0.649, 0.68, 0.649, 0.621, 0.644, 0.683, 0.683, 0.693, 0.7, 0.706, 0.708, 0.707, 0.684, 0.68, 0.679, 0.673, 0.583, 0.407, 0.396, 0.412, 0.457, 0.551, 0.652, 0.721, 0.706, 0.706, 0.696, 0.697, 0.725, 0.738, 0.722, 0.582, 0.395, 0.368, 0.351, 0.377, 0.47, 0.514, 0.599, 0.636, 0.651, 0.638, 0.67, 0.639, 0.656, 0.672, 0.704, 0.641, 0.624, 0.657, 0.636, 0.623, 0.651, 0.638, 0.568, 0.601, 0.567, 0.57, 0.567, 0.557, 0.586, 0.571, 0.556, 0.601, 0.604, 0.559, 0.559, 0.601, 0.556, 0.549, 0.548, 0.548, 0.552, 0.537, 0.538, 0.553, 0.532, 0.549, 0.52, 0.501, 0.477, 0.464, 0.456, 0.485, 0.477, 0.468, 0.451, 0.451, 0.451, 0.447, 0.448, 0.446, 0.446, 0.452, 0.455, 0.445, 0.452, 0.454, 0.449, 0.446, 0.446, 0.447, 0.424, 0.434, 0.452, 0.443, 0.434, 0.437, 0.443, 0.449, 0.449, 0.449, 0.444, 0.435, 0.417, 0.437, 0.456, 0.423, 0.437, 0.459, 0.452, 0.434, 0.411, 0.428, 0.437, 0.446, 0.429, 0.43, 0.462, 0.499, 0.481, 0.511, 0.511, 0.477, 0.504, 0.498, 0.5, 0.483, 0.451, 0.469, 0.453, 0.468, 0.461, 0.434, 0.436, 0.428, 0.429, 0.437, 0.384, 0.384, 0.423, 0.382, 0.379, 0.325, 0.439, 0.572, 0.654, 0.642, 0.677, 0.68, 0.677, 0.695, 0.668, 0.692, 0.706, 0.661, 0.693, 0.66, 0.679, 0.696, 0.677, 0.672, 0.702, 0.658, 0.679, 0.703, 0.693, 0.662, 0.685, 0.697, 0.694, 0.657, 0.691, 0.665, 0.679, 0.701, 0.682, 0.653, 0.687, 0.684, 0.696, 0.699, 0.737, 0.719, 0.703, 0.714, 0.708, 0.72, 0.719, 0.736, 0.746, 0.727, 0.725, 0.733, 0.75, 0.778, 0.75, 0.792, 0.723, 0.759, 0.718, 0.708, 0.763, 0.777, 0.777, 0.764, 0.755, 0.76, 0.757, 0.764, 0.727, 0.736, 0.742, 0.742, 0.605, 0.532, 0.531, 0.612, 0.704, 0.74, 0.727, 0.754, 0.736, 0.716, 0.686, 0.667, 0.666, 0.663, 0.663, 0.659, 0.665, 0.67, 0.665, 0.679, 0.694, 0.786, 0.782, 0.801, 0.753, 0.764, 0.746, 0.766, 0.764, 0.746, 0.715, 0.728, 0.715, 0.708, 0.683, 0.721, 0.706, 0.683, 0.672, 0.659, 0.678, 0.659, 0.666, 0.663, 0.66, 0.659, 0.692, 0.63, 0.628, 0.627, 0.614, 0.612, 0.612, 0.61, 0.525, 0.392, 0.378, 0.477, 0.558, 0.606, 0.618, 0.638, 0.655, 0.642, 0.631, 0.672, 0.673, 0.672, 0.65, 0.663, 0.69, 0.662, 0.675, 0.706, 0.69, 0.691, 0.672, 0.672, 0.671, 0.672, 0.662, 0.63, 0.647, 0.648, 0.663, 0.68, 0.678, 0.663, 0.678, 0.662, 0.649, 0.704, 0.677, 0.679, 0.705, 0.672, 0.654, 0.676, 0.664, 0.629, 0.67, 0.667, 0.685, 0.676, 0.651, 0.652, 0.643, 0.655, 0.664, 0.649, 0.618, 0.629, 0.665, 0.643, 0.643, 0.618, 0.634, 0.634, 0.665, 0.663, 0.652, 0.652, 0.643, 0.664, 0.675, 0.667, 0.664, 0.7, 0.655, 0.667, 0.685, 0.68, 0.682, 0.667, 0.546, 0.494, 0.561, 0.631, 0.643, 0.63, 0.646, 0.664, 0.663, 0.665, 0.667, 0.685, 0.68, 0.667, 0.668, 0.667, 0.67, 0.68, 0.667, 0.664, 0.652, 0.652, 0.643, 0.664, 0.652, 0.652, 0.667, 0.652, 0.667, 0.649, 0.664, 0.651, 0.68, 0.65, 0.702, 0.667, 0.62, 0.635, 0.633, 0.651, 0.63, 0.614, 0.614, 0.599, 0.63, 0.611, 0.651, 0.633, 0.665, 0.642, 0.658, 0.605, 0.652, 0.645, 0.635, 0.661, 0.642, 0.644, 0.603, 0.602, 0.541, 0.53, 0.56, 0.556, 0.568, 0.604, 0.615, 0.607, 0.532, 0.569, 0.585, 0.566, 0.584, 0.591, 0.508, 0.452, 0.458, 0.466, 0.343, 0.371, 0.38, 0.466, 0.456, 0.542, 0.544, 0.582, 0.544, 0.472, 0.477, 0.476, 0.512, 0.501, 0.421, 0.442, 0.458, 0.424, 0.418, 0.516, 0.548, 0.509, 0.568, 0.612, 0.679, 0.683, 0.759, 0.831, 0.915, 0.857, 0.876, 0.81, 0.812, 0.795, 0.688, 0.492, 0.425, 0.364, 0.396, 0.398, 0.461, 0.524, 0.479, 0.515, 0.498, 0.47, 0.506, 0.513, 0.513, 0.507, 0.515, 0.503, 0.548, 0.565, 0.523, 0.529, 0.554, 0.551, 0.548, 0.56, 0.527, 0.525, 0.528, 0.496, 0.531, 0.516, 0.505, 0.478, 0.472, 0.46, 0.424, 0.418, 0.46, 0.462, 0.609, 0.595, 0.579, 0.612, 0.608, 0.645, 0.624, 0.595, 0.573, 0.588, 0.602, 0.608, 0.627, 0.623, 0.612, 0.6, 0.615, 0.627, 0.65, 0.669, 0.682, 0.689, 0.667, 0.678, 0.665, 0.666, 0.685, 0.667, 0.684, 0.685, 0.675, 0.678, 0.679, 0.679, 0.681, 0.699, 0.683, 0.654, 0.696, 0.671, 0.658, 0.698, 0.665, 0.647, 0.641, 0.551, 0.531, 0.621, 0.723, 0.716, 0.71, 0.766, 0.72, 0.757, 0.745, 0.757, 0.736, 0.686, 0.69, 0.644, 0.676, 0.408, 0.463, 0.592, 0.664, 0.664, 0.665, 0.681, 0.698, 0.673, 0.717, 0.689, 0.705, 0.683, 0.671, 0.686, 0.667, 0.664, 0.655, 0.652, 0.666, 0.687, 0.655, 0.672, 0.673, 0.672, 0.686, 0.664, 0.685, 0.666, 0.666, 0.669, 0.669, 0.685, 0.675, 0.654, 0.657, 0.657, 0.688, 0.686, 0.686, 0.667, 0.67, 0.654, 0.641, 0.67, 0.669, 0.652, 0.639, 0.66, 0.658, 0.639, 0.675, 0.642, 0.69, 0.66, 0.67, 0.668, 0.634, 0.514, 0.459, 0.467, 0.465, 0.544, 0.528, 0.584, 0.612, 0.589, 0.625, 0.621, 0.65, 0.619, 0.635, 0.648, 0.671, 0.671, 0.626, 0.635, 0.634, 0.618, 0.651, 0.628, 0.654, 0.666, 0.634, 0.651, 0.648, 0.659, 0.653, 0.666, 0.636, 0.633, 0.634, 0.576, 0.514, 0.505, 0.498, 0.514, 0.569, 0.614, 0.63, 0.624, 0.624, 0.651, 0.647, 0.673, 0.655, 0.655, 0.673, 0.645, 0.659, 0.67, 0.654, 0.664, 0.644, 0.644, 0.664, 0.667, 0.67, 0.67, 0.671, 0.72, 0.684, 0.702, 0.686, 0.671, 0.714, 0.707, 0.701, 0.702, 0.718, 0.698, 0.728, 0.682, 0.683, 0.692, 0.683, 0.701, 0.683, 0.697, 0.669, 0.679, 0.682, 0.68, 0.682, 0.683, 0.682, 0.683, 0.718, 0.7, 0.679, 0.685, 0.698, 0.698, 0.705, 0.703, 0.683, 0.631, 0.578, 0.558, 0.583, 0.597, 0.641, 0.628, 0.686, 0.67, 0.668, 0.705, 0.684, 0.685, 0.685, 0.682, 0.683, 0.662, 0.657, 0.647, 0.646, 0.649, 0.665, 0.672, 0.663, 0.685, 0.666, 0.685, 0.686, 0.702, 0.697, 0.693, 0.686, 0.691, 0.686, 0.702, 0.717, 0.697, 0.698, 0.698, 0.701, 0.698, 0.685, 0.685, 0.683, 0.683, 0.685, 0.685, 0.686, 0.647, 0.667, 0.668, 0.674, 0.671, 0.674, 0.671, 0.652, 0.705, 0.682, 0.687, 0.718, 0.703, 0.703, 0.701, 0.682, 0.693, 0.668, 0.668, 0.671, 0.673, 0.673, 0.673, 0.672, 0.672, 0.685, 0.684, 0.672, 0.681, 0.682, 0.701, 0.719, 0.688, 0.683, 0.65, 0.677, 0.703, 0.686, 0.682, 0.703, 0.721, 0.669, 0.718, 0.685, 0.664, 0.684, 0.686, 0.687, 0.7, 0.702, 0.696, 0.68, 0.597, 0.546, 0.498, 0.475, 0.51, 0.544, 0.637, 0.653, 0.636, 0.63, 0.653, 0.666, 0.646, 0.666, 0.656, 0.716, 0.681, 0.684, 0.685, 0.682, 0.683, 0.683, 0.696, 0.681, 0.696, 0.68, 0.68, 0.683, 0.666, 0.656, 0.646, 0.666, 0.666, 0.666, 0.68, 0.656, 0.687, 0.667, 0.653, 0.68, 0.667, 0.682, 0.667, 0.682, 0.667, 0.66, 0.7, 0.683, 0.684, 0.689, 0.67, 0.671, 0.668, 0.702, 0.702, 0.668, 0.668, 0.666, 0.667, 0.682, 0.665, 0.667, 0.668, 0.647, 0.663, 0.645, 0.645, 0.645, 0.645, 0.645, 0.645, 0.645, 0.625, 0.625, 0.645, 0.645, 0.664, 0.664, 0.663, 0.663, 0.665, 0.649, 0.664, 0.649, 0.63, 0.643, 0.648, 0.65, 0.646, 0.644, 0.624, 0.644, 0.648, 0.644, 0.625, 0.645, 0.673, 0.645, 0.664, 0.679, 0.679, 0.672, 0.649, 0.673, 0.623, 0.624, 0.644, 0.624, 0.67, 0.674, 0.66, 0.643, 0.679, 0.668, 0.679, 0.679, 0.679, 0.702, 0.665, 0.679, 0.65, 0.65, 0.662, 0.651, 0.666, 0.683, 0.679, 0.68, 0.69, 0.666, 0.649, 0.684, 0.699, 0.689, 0.652, 0.665, 0.685, 0.722, 0.685, 0.701, 0.686, 0.7, 0.683, 0.683, 0.686, 0.686, 0.668, 0.681, 0.665, 0.668, 0.667, 0.693, 0.67, 0.623, 0.683, 0.666, 0.658, 0.633, 0.666, 0.666, 0.683, 0.659, 0.657, 0.633, 0.567, 0.524, 0.514, 0.636, 0.657, 0.646, 0.62, 0.691, 0.718, 0.759, 0.843, 0.796, 0.789, 0.782, 0.708, 0.631, 0.656, 0.685, 0.676, 0.755, 0.791, 0.768, 0.778, 0.749, 0.751, 0.785, 0.783, 0.797, 0.811, 0.839, 0.768, 0.778, 0.759, 0.694, 0.568, 0.585, 0.69, 0.796, 0.835, 0.929, 0.855, 0.837, 0.829, 0.783, 0.661, 0.663, 0.677, 0.649, 0.652, 0.657, 0.663, 0.664, 0.685, 0.682, 0.678, 0.637, 0.733, 0.723, 0.665, 0.711, 0.704, 0.699, 0.7, 0.682, 0.691, 0.695, 0.677, 0.668, 0.661, 0.657, 0.651, 0.673, 0.65, 0.677, 0.652, 0.651, 0.665, 0.667, 0.683, 0.683, 0.606, 0.424, 0.404, 0.506, 0.61, 0.67, 0.68, 0.689, 0.678, 0.665, 0.66, 0.661, 0.694, 0.656, 0.694, 0.694, 0.643, 0.642, 0.657, 0.658, 0.688, 0.714, 0.705, 0.657, 0.67, 0.664, 0.658, 0.649, 0.64, 0.67, 0.679, 0.66, 0.66, 0.65, 0.645, 0.646, 0.607, 0.608, 0.607, 0.619, 0.628, 0.614, 0.638, 0.625, 0.609, 0.6, 0.625, 0.639, 0.513, 0.501, 0.578, 0.638, 0.494, 0.547, 0.637, 0.666, 0.676, 0.675, 0.667, 0.705, 0.707, 0.705, 0.688, 0.685, 0.684, 0.712, 0.638, 0.638, 0.673, 0.637, 0.638, 0.638, 0.622, 0.638, 0.524, 0.637, 0.629, 0.629, 0.685, 0.695, 0.678, 0.678, 0.685, 0.666, 0.645, 0.639, 0.678, 0.662, 0.694, 0.659, 0.638, 0.665, 0.638, 0.658, 0.638, 0.652, 0.643, 0.68, 0.695, 0.695, 0.674, 0.675, 0.686, 0.695, 0.652, 0.644, 0.637, 0.622, 0.674, 0.678, 0.657, 0.622, 0.623, 0.637, 0.623, 0.64, 0.625, 0.614, 0.637, 0.65, 0.65, 0.651, 0.65, 0.654, 0.677, 0.668, 0.669, 0.648, 0.678, 0.657, 0.657, 0.641, 0.654, 0.65, 0.632, 0.497, 0.489, 0.578, 0.615, 0.604, 0.65, 0.624, 0.674, 0.673, 0.655, 0.639, 0.638, 0.658, 0.637, 0.658, 0.638, 0.637, 0.638, 0.642, 0.664, 0.649, 0.658, 0.637, 0.623, 0.625, 0.655, 0.641, 0.656, 0.626, 0.614, 0.638, 0.638, 0.631, 0.672, 0.673, 0.65, 0.659, 0.678, 0.678, 0.664, 0.662, 0.662, 0.678, 0.654, 0.654, 0.635, 0.643, 0.672, 0.654, 0.695, 0.662, 0.662, 0.663, 0.679, 0.647, 0.663, 0.643, 0.658, 0.661, 0.638, 0.637, 0.639, 0.677, 0.638, 0.638, 0.639, 0.639, 0.639, 0.639, 0.639, 0.639, 0.639, 0.639, 0.639, 0.66, 0.654, 0.638, 0.654, 0.638, 0.655, 0.655, 0.638, 0.659, 0.559, 0.489, 0.501, 0.475, 0.547, 0.578, 0.608, 0.662, 0.63, 0.646, 0.641, 0.642, 0.642, 0.656, 0.642, 0.626, 0.621, 0.61, 0.61, 0.621, 0.616, 0.613, 0.622, 0.638, 0.638, 0.642, 0.66, 0.563, 0.503, 0.517, 0.554, 0.578, 0.621, 0.622, 0.631, 0.63, 0.679, 0.642, 0.693, 0.638, 0.621, 0.638, 0.638, 0.652, 0.638, 0.626, 0.633, 0.658, 0.659, 0.686, 0.655, 0.639, 0.639, 0.639, 0.638, 0.638, 0.659, 0.642, 0.653, 0.658, 0.639, 0.659, 0.67, 0.653, 0.643, 0.637, 0.643, 0.631, 0.66, 0.652, 0.637, 0.655, 0.644, 0.678, 0.695, 0.644, 0.675, 0.672, 0.695, 0.68, 0.678, 0.659, 0.661, 0.652, 0.665, 0.624, 0.637, 0.639, 0.641, 0.638, 0.642, 0.616, 0.644, 0.625, 0.616, 0.635, 0.662, 0.628, 0.655, 0.68, 0.672, 0.643, 0.654, 0.658, 0.653, 0.673, 0.67, 0.639, 0.673, 0.674, 0.673, 0.672, 0.693, 0.673, 0.718, 0.674, 0.658, 0.658, 0.667, 0.659, 0.682, 0.672, 0.655, 0.66, 0.657, 0.652, 0.674, 0.663, 0.705, 0.679, 0.655, 0.651, 0.659, 0.663, 0.647, 0.647, 0.659, 0.635, 0.622, 0.633, 0.632, 0.646, 0.646, 0.631, 0.63, 0.646, 0.629, 0.648, 0.656, 0.585, 0.524, 0.515, 0.465, 0.487, 0.454, 0.474, 0.516, 0.523, 0.536, 0.522, 0.5, 0.546, 0.528, 0.568, 0.56, 0.598, 0.638, 0.607, 0.624, 0.643, 0.68, 0.647, 0.762, 0.855, 0.892, 0.896, 0.87, 0.807, 0.718, 0.712, 0.853, 0.715, 0.817, 0.817, 0.828, 0.814, 0.762, 0.863, 0.905, 0.932, 0.98, 1.017, 1.103, 1.105, 0.979, 1.226, 1.158, 1.114, 1.083, 1.061, 1.084, 1.111, 0.998, 0.951, 0.933, 1.018, 1.013, 1.027, 1.027, 1.16, 1.1, 1.259, 1.113, 0.941, 1.038, 0.963, 0.892, 0.863, 0.799, 0.829, 0.792, 0.806, 0.786, 0.778, 0.808, 0.759, 0.804, 0.779, 0.801, 0.75, 0.771, 0.731, 0.76, 0.752, 0.783, 0.749, 0.825, 0.757, 0.764, 0.762, 0.757, 0.764, 0.74, 0.784, 0.757, 0.74, 0.74, 0.749, 0.784, 0.754, 0.757, 0.75, 0.787, 0.805, 0.753, 0.771, 0.729, 0.758, 0.787, 0.808, 0.775, 0.821, 0.791, 0.777, 0.795, 0.797, 0.807, 0.804, 0.772, 0.797, 0.757, 0.804, 0.814, 0.788, 0.816, 0.789, 0.789, 0.81, 0.814, 0.821, 0.845, 0.802, 0.834, 0.844, 0.831, 0.826, 0.82, 0.83, 0.768, 0.705, 0.547, 0.457, 0.44, 0.451, 0.446, 0.435, 0.502, 0.462, 0.529, 0.537, 0.605, 0.641, 0.648, 0.777, 0.86, 0.916, 0.967, 0.903, 0.918, 0.789, 0.732, 0.883, 0.811, 0.864, 0.939, 0.953, 0.906, 0.799, 0.899, 0.871, 0.842, 0.814, 0.774, 0.909, 0.927, 0.869, 0.967, 0.905, 0.959, 0.809, 0.902, 0.849, 0.938, 1.156, 1.077, 1.054, 1.056, 1.194, 1.16, 1.113, 1.025, 1.007, 0.95, 0.903, 0.889, 0.819, 0.867, 0.837, 0.81, 0.769, 0.768, 0.652, 0.748, 0.712, 0.744, 0.729, 0.695, 0.727, 0.719, 0.728, 0.725, 0.722, 0.708, 0.688, 0.688, 0.709, 0.71, 0.688, 0.689, 0.711, 0.726, 0.688, 0.676, 0.693, 0.695, 0.676, 0.683, 0.688, 0.705, 0.703, 0.67, 0.658, 0.658, 0.643, 0.662, 0.664, 0.655, 0.645, 0.661, 0.664, 0.645, 0.679, 0.679, 0.676, 0.667, 0.679, 0.661, 0.643, 0.67, 0.678, 0.646, 0.645, 0.648, 0.654, 0.63, 0.628, 0.659, 0.645, 0.646, 0.645, 0.643, 0.646, 0.659, 0.643, 0.644, 0.662, 0.643, 0.659, 0.679, 0.628, 0.643, 0.644, 0.645, 0.645, 0.645, 0.644, 0.645, 0.662, 0.645, 0.625, 0.612, 0.631, 0.609, 0.637, 0.645, 0.635, 0.645, 0.651, 0.663, 0.664, 0.647, 0.68, 0.627, 0.552, 0.546, 0.501, 0.526, 0.497, 0.52, 0.538, 0.509, 0.503, 0.532, 0.549, 0.533, 0.558, 0.543, 0.545, 0.5, 0.531, 0.531, 0.518, 0.508, 0.503, 0.51, 0.52, 0.517, 0.482, 0.565, 0.539, 0.517, 0.57, 0.557, 0.558, 0.549, 0.604, 0.635, 0.681, 0.663, 0.716, 0.654, 0.572, 0.578, 0.549, 0.534, 0.533, 0.511, 0.528, 0.535, 0.562, 0.605, 0.598, 0.621, 0.624, 0.648, 0.675, 0.579, 0.642, 0.585, 0.571, 0.552, 0.585, 0.64, 0.613, 0.668, 0.589, 0.586, 0.6, 0.632, 0.653, 0.645, 0.645, 0.684, 0.653, 0.697, 0.67, 0.657, 0.685, 0.661, 0.69, 0.718, 0.679, 0.693, 0.684, 0.688, 0.667, 0.676, 0.67, 0.685, 0.656, 0.673, 0.693, 0.663, 0.673, 0.701, 0.728, 0.73, 0.718, 0.762, 0.749, 0.736, 0.728, 0.69, 0.707, 0.707, 0.712, 0.707, 0.712, 0.717, 0.731, 0.717, 0.712, 0.731, 0.705, 0.771, 0.693, 0.688, 0.735, 0.735, 0.712, 0.706, 0.713, 0.711, 0.684, 0.681, 0.671, 0.695, 0.693, 0.652, 0.69, 0.65, 0.671, 0.719, 0.679, 0.695, 0.656, 0.692, 0.7, 0.736, 0.708, 0.705, 0.704, 0.699, 0.665, 0.69, 0.717, 0.72, 0.688, 0.728, 0.697, 0.703, 0.728, 0.711, 0.712, 0.699, 0.688, 0.706, 0.667, 0.651, 0.586, 0.628, 0.648, 0.598, 0.591, 0.598, 0.624, 0.601, 0.606, 0.666, 0.608, 0.583, 0.588, 0.545, 0.554, 0.642, 0.582, 0.533, 0.505, 0.528, 0.575, 0.578, 0.513, 0.5, 0.525, 0.482, 0.477, 0.475, 0.531, 0.51, 0.502, 0.464, 0.473, 0.466, 0.457, 0.441, 0.465, 0.487, 0.433, 0.405, 0.403, 0.433, 0.44, 0.419, 0.375, 0.388, 0.393, 0.397, 0.403, 0.426, 0.384, 0.351, 0.419, 0.367, 0.361, 0.391, 0.356, 0.385, 0.37, 0.346, 0.353, 0.365, 0.38, 0.383, 0.377, 0.396, 0.383, 0.393, 0.394, 0.397, 0.357, 0.392, 0.397, 0.402, 0.38, 0.408, 0.394, 0.397, 0.396, 0.392, 0.5, 0.586, 0.636, 0.645, 0.665, 0.647, 0.655, 0.659, 0.705, 0.703, 0.677, 0.697, 0.693, 0.689, 0.655, 0.681, 0.687, 0.673, 0.7, 0.676, 0.699, 0.691, 0.666, 0.695, 0.653, 0.654, 0.684, 0.704, 0.632, 0.55, 0.484, 0.497, 0.556, 0.602, 0.632, 0.624, 0.635, 0.646, 0.646, 0.631, 0.613, 0.639, 0.604, 0.63, 0.661, 0.646, 0.639, 0.64, 0.663, 0.66, 0.653, 0.627, 0.639, 0.625, 0.664, 0.644, 0.664, 0.659, 0.64, 0.68, 0.68, 0.665, 0.664, 0.68, 0.645, 0.656, 0.656, 0.678, 0.678, 0.658, 0.678, 0.678, 0.658, 0.674, 0.675, 0.675, 0.669, 0.668, 0.653, 0.669, 0.649, 0.644, 0.657, 0.668, 0.672, 0.64, 0.66, 0.663, 0.664, 0.658, 0.677, 0.677, 0.693, 0.702, 0.702, 0.702, 0.682, 0.681, 0.693, 0.697, 0.689, 0.69, 0.664, 0.647, 0.648, 0.652, 0.7, 0.702, 0.677, 0.708, 0.728, 0.714, 0.69, 0.744, 0.729, 0.695, 0.705, 0.73, 0.726, 0.727, 0.72, 0.722, 0.706, 0.691, 0.667, 0.718, 0.683, 0.716, 0.737, 0.72, 0.755, 0.712, 0.712, 0.697, 0.683, 0.756, 0.74, 0.74, 0.723, 0.712, 0.706, 0.673, 0.692, 0.677, 0.692, 0.71, 0.707, 0.69, 0.689, 0.68, 0.68, 0.692, 0.677, 0.693, 0.726, 0.724, 0.683, 0.724, 0.707, 0.69, 0.698, 0.713, 0.722, 0.706, 0.705, 0.723, 0.682, 0.724, 0.724, 0.695, 0.673, 0.707, 0.677, 0.677, 0.661, 0.673, 0.679, 0.664, 0.679, 0.682, 0.661, 0.681, 0.697, 0.689, 0.677, 0.677, 0.678, 0.671, 0.678, 0.692, 0.686, 0.557, 0.483, 0.454, 0.474, 0.53, 0.564, 0.63, 0.653, 0.643, 0.684, 0.681, 0.676, 0.686, 0.692, 0.687, 0.655, 0.666, 0.703, 0.67, 0.671, 0.684, 0.688, 0.667, 0.667, 0.653, 0.668, 0.652, 0.683, 0.642, 0.659, 0.649, 0.702, 0.668, 0.658, 0.662, 0.652, 0.647, 0.665, 0.666, 0.666, 0.687, 0.687, 0.687, 0.682, 0.665, 0.697, 0.683, 0.682, 0.667, 0.698, 0.667, 0.717, 0.697, 0.685, 0.682, 0.701, 0.684, 0.674, 0.674, 0.657, 0.691, 0.659, 0.666, 0.676, 0.657, 0.687, 0.659, 0.656, 0.656, 0.674, 0.672, 0.674, 0.693, 0.681, 0.693, 0.684, 0.693, 0.674, 0.674, 0.674, 0.688, 0.674, 0.686, 0.698, 0.698, 0.698, 0.698, 0.698, 0.718, 0.696, 0.698, 0.696, 0.716, 0.698, 0.696, 0.663, 0.663, 0.683, 0.663, 0.683, 0.698, 0.698, 0.646, 0.611, 0.559, 0.514, 0.51, 0.556, 0.58, 0.632, 0.679, 0.683, 0.683, 0.693, 0.718, 0.673, 0.683, 0.681, 0.647, 0.667, 0.667, 0.673, 0.674, 0.699, 0.701, 0.682, 0.682, 0.702, 0.684, 0.683, 0.684, 0.701, 0.694, 0.674, 0.674, 0.643, 0.684, 0.666, 0.659, 0.668, 0.686, 0.686, 0.686, 0.667, 0.702, 0.683, 0.684, 0.676, 0.667, 0.705, 0.693, 0.666, 0.667, 0.677, 0.67, 0.668, 0.644, 0.644, 0.644, 0.658, 0.703, 0.692, 0.692, 0.692, 0.693, 0.693, 0.683, 0.709, 0.703, 0.703, 0.683, 0.683, 0.703, 0.683, 0.718, 0.701, 0.694, 0.696, 0.709, 0.709, 0.709, 0.694, 0.694, 0.674, 0.709, 0.709, 0.684, 0.686, 0.701, 0.682, 0.686, 0.683, 0.594, 0.604, 0.485, 0.535, 0.564, 0.614, 0.606, 0.634, 0.634, 0.67, 0.657, 0.699, 0.657, 0.704, 0.688, 0.667, 0.693, 0.693, 0.709, 0.674, 0.671, 0.669, 0.688, 0.686, 0.667, 0.687, 0.684, 0.668, 0.683, 0.683, 0.645, 0.669, 0.666, 0.667, 0.659, 0.659, 0.669, 0.688, 0.667, 0.683, 0.657, 0.688, 0.667, 0.693, 0.694, 0.69, 0.669, 0.659, 0.657, 0.689, 0.686, 0.679, 0.679, 0.688, 0.688, 0.669, 0.657, 0.679, 0.666, 0.642, 0.673, 0.678, 0.663, 0.675, 0.678, 0.692, 0.662, 0.666, 0.696, 0.662, 0.662, 0.663, 0.674, 0.682, 0.677, 0.662, 0.663, 0.663, 0.664, 0.66, 0.641, 0.633, 0.648, 0.648, 0.664, 0.644, 0.636, 0.628, 0.663, 0.637, 0.669, 0.66, 0.662, 0.672, 0.668, 0.663, 0.645, 0.662, 0.663, 0.648, 0.653, 0.573, 0.498, 0.503, 0.53, 0.603, 0.653, 0.671, 0.632, 0.682, 0.663, 0.7, 0.682, 0.73, 0.712, 0.696, 0.701, 0.701, 0.688, 0.669, 0.702, 0.663, 0.67, 0.673, 0.683, 0.698, 0.718, 0.696, 0.669, 0.668, 0.662, 0.681, 0.669, 0.659, 0.673, 0.659, 0.662, 0.662, 0.647, 0.648, 0.658, 0.643, 0.647, 0.632, 0.643, 0.657, 0.65, 0.634, 0.647, 0.632, 0.665, 0.695, 0.655, 0.692, 0.756, 0.716, 0.707, 0.71, 0.722, 0.708, 0.704, 0.722, 0.734, 0.741, 0.72, 0.708, 0.717, 0.693, 0.723, 0.713, 0.568, 0.474, 0.56, 0.674, 0.621, 0.796, 0.845, 0.8, 0.92, 0.747, 0.798, 0.705, 0.718]
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
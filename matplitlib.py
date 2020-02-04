import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.style as mplstyle
mplstyle.use(['dark_background', 'ggplot', 'fast'])


def my_plotter(ax, x, y, param_dict):
    out = ax.plot(x, y, **param_dict)
    return out

if __name__ == '__main__':
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, ax = plt.subplots(1, 1)
    my_plotter(ax, data1, data2, {'marker': 'x'})

    fig, (ax1, ax2) = plt.subplots(1, 2)
    my_plotter(ax1, data1, data2, {'marker': 'x'})
    my_plotter(ax2, data3, data4, {'marker': 'o'})

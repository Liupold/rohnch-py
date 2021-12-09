from numpy import *
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator

A4_L = (11.69,8.27)
A4_P = (8.27, 11.69)

def DT(head, data):
    n = len(head)
    df = pd.DataFrame(dict(zip(head,
                      [data[s::n] for s in range(n)]
        )))
    df.index += 1
    return df

def FIT(eqn, x, y, **kwargs):
    popt, pcov = curve_fit(eqn, x, y, **kwargs)
    f = lambda x: eqn(x, *popt)
    print("fit_params:", popt)
    return f, popt

def PLOT(file, **kwargs):
    fig, ax = plt.subplots()
    if 'figsize' in kwargs.keys():
        fig, ax =  plt.subplots(figsize=kwargs.pop('figsize'))
    elif file[-4::] == '.pdf':
        fig, ax = plt.subplots(figsize=A4_P)
    else:
        fig, ax = plt.subplots()

    if 'xlabel' in kwargs.keys():
        plt.xlabel(kwargs.pop('xlabel'))
    if 'ylabel' in kwargs.keys():
        plt.xlabel(kwargs.pop('ylabel'))
    if 'title' in kwargs.keys():
        plt.title(kwargs.pop('title'))
    for k, v in kwargs.items():
        if callable(v[0]):
            x_data = linspace(*v[1])
            y_data = v[0](x_data)
        else:
            x_data = v[0]
            y_data = v[1]
        plt.plot(x_data, y_data, *v[2:])
    plt.legend(kwargs.keys())
    plt.grid()
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.grid(which='major', color='#BBBBBB', linestyle='-')
    ax.grid(which='minor', color='#CCCCCC', linestyle=':')
    if file == 'show':
        plt.show()
    else:
        fig.savefig(file)

def sp(*args, **kargs):
    nargs = [];
    for i, item in enumerate(args):
        if isinstance(item, (float, int)):
            nargs.append("{:e}".format(item))
        else:
            nargs.append(item)
    print(*nargs, **kargs)



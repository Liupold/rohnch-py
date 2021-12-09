from numpy import *
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

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
    if file == 'show':
        plt.show()
    else:
        plt.savefig(file)

def sp(*args, **kargs):
    nargs = [];
    for i, item in enumerate(args):
        if isinstance(item, (float, int)):
            nargs.append("{:e}".format(item))
        else:
            nargs.append(item)
    print(*nargs, **kargs)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def file_name( name ,degree):
    fitdegree = degree

    dataset = pd.read_csv(name, keep_default_na=False) 

    time = dataset['0']
    cpu = dataset['1']
    memory = dataset['2']
    power = dataset['3']

    cpu = type_transfer(cpu)
    power = type_transfer(power)
    memory = type_transfer(memory)

    Length = len(cpu)
    x = np.linspace(0, Length, Length)

    ax = plt.subplot()
    p1 = ax.scatter(x, cpu, c='red', marker='x', alpha=0.6, linewidth=1)
    p2 = ax.scatter(x, memory, c='black', marker='v', alpha=0.6, linewidth=1)
    p3 = ax.scatter(x, power, c='blue', marker='p', alpha=0.6, linewidth=1)

    plt.legend([p1, p2, p3], ['cpu usage', 'memory usage', 'powerusage'], loc='upper left')
    plt.figure()   

    if (name == 'cpu.csv'):
        useful = cpu
        lable = 'cpu usage %'
    else:
        useful = memory
        lable = 'memory usage %'

    plt.scatter(useful, power, s=75, color='r', alpha=.5)
    plt.ylabel('power usage')
    plt.xlabel(lable)
    plt.show()
    plt.tight_layout()

    plt.figure()
    plt.scatter(useful, power, s=75, color='r', alpha=.5)
    z= polynomial_fitfunction(useful,power,fitdegree)
    plt.plot(useful, z, linewidth=4, color='g')
    plt.ylabel('power usage')
    plt.xlabel(lable)
    plt.show()

def type_transfer(data):
    a = data.to_list()
    a.pop() 
    a = [float(i) for i in a]
    return a

def polynomial_fitfunction(data_X,data_Y,degree):
    fit = np.polyfit(data_X, data_Y, deg=degree)  
    fit_show = np.poly1d(fit)  
    print("The fit founction is : \n", fit_show)
    z = np.polyval(fit, data_X)
    return z

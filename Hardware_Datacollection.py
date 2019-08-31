import csv
import pandas as pd
import psutil
import threading
import time

class A():
    aa = ""

class myThread(threading.Thread):    #Inherit the parent class,threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):     #Write the code to execute into the run function and the thread will run the run function directly after it is created
        while True:
            a.aa = input('enter Q to exist:')
            if a.aa == 'Q':
                break

a = A()
i = 0

def run(csvname):
    name = ['timestamp', 'cpu usage', 'memory usage']
    test1 = pd.DataFrame(columns=name)
    test1.to_csv(csvname, encoding='gbk')
    my_t = myThread()   # Create a new thread
    my_t.start()
    global i #Global variables are used for declarations
    while True:
        if a.aa == "Q":
            break
        else:
            if (i <7200):
                tim=time.strftime("%H:%M:%S")
                cpu_usage = psutil.cpu_percent(interval=1)
                memory_usage = psutil.virtual_memory().percent
                print("--------------", i, "----------------")
                print("timestamp : ", tim)
                print("cpu usage : ", cpu_usage)
                print("memory usage : ", memory_usage)
                list_c = list()
                list_c.append(i)
                list_c.append(tim)
                list_c.append(cpu_usage)
                list_c.append(memory_usage)
                i=i+1
                with open(csvname, 'a+') as f:
                    csv_write = csv.writer(f)
                    data_row = list_c
                    csv_write.writerow(data_row)
            else:
                break

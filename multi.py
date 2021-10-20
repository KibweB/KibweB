""" A process is an instance of a program.
Theads are an entity within a process that can be sceduled/lightweight process. A process can spawn muliple threads 
Gil= Global Interpreter Lock, one that allows only obe thread at a time to execute in Python """
from multiprocessing import Process
import os
import time

def squareNum():
    for d in range(100):
        d*d
        time.sleep(0.1)
processes=[]
num_pro= os.cpu_count()
#create processes
for i in range(num_pro):
    p =Process(target=squareNum)
    processes.append(p)
#start
for p in processes:
    p.start()
#join
for p in processes:
    p.join()

print('end main')
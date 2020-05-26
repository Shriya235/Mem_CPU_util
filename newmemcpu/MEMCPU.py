import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import statistics
import re
import datetime as dt
import itertools
from  datetime import datetime

def mem(sub,logfile):
    mem = []
    newlistmem = []
    memtime=[]
    tim=[]
    substr = sub                                              
    with open (logfile, 'rt') as myfile:
        for line in myfile:
            if line.find(substr) != -1:          
                mem.extend(re.split(r'[|\s]\s*', line))                                      
    for (value,total) in zip(mem[2::10],mem[1::10]):
        new_elem = int(value)/int(total)                                
        newlistmem.append(new_elem*100)
    for d,t in zip(mem[7::10],mem[8::10]):
       tim.append(d+" "+t)
    date_obj = []
    for temp in tim:
        date_obj.append(datetime.strptime(temp, '%Y-%m-%d %H:%M:%S.%f'))
    dates = md.date2num(date_obj)
    Data_Printing(newlistmem,substr)
    Data_Plotting(dates,newlistmem,"Memory Utilisation")
    
def cpu(str1,logfile):
    cpu=[]
    newlistcpu=[]
    cputime=[]
    substr1= str1
    valu=substr1.split()
    with open (logfile, 'rt') as myfile:
        for line in myfile:
            if line.find(substr1)!= -1:
                cpu.extend(re.split(r'[|\s]\s*', line))
    for value in cpu[7::11]:
        newlistcpu.append(100-float(value))
    for d,t in zip(cpu[8::11],cpu[9::11]):
        cputime.append(d+" "+t)
    date_obj = []
    for temp in cputime:
        date_obj.append(datetime.strptime(temp, '%Y-%m-%d %H:%M:%S.%f'))
    dates = md.date2num(date_obj)
    Data_Printing(newlistcpu,str1)
    Data_Plotting(dates,newlistcpu,"CPU Utilisation for Avg "+valu[1])
  
def Data_Printing(value,string1):
    if string1 == "Mem:      ":
       print("Maximum memory utilisation: ",max(value),"%")
       print("Minimum memory utilisation: ",min(value),"%")
       print("Average memory utilisation : ",statistics.mean(value),"%")
    else:
       val=string1.split()
       print("Maximum CPU utilisation for Average "+val[1]+": ",max(value),"%")
       print("Minimum CPU utilisation for Average "+val[1]+": ",min(value),"%")
       print("Average CPU utilisation for Average "+val[1]+": ",statistics.mean(value),"%")

def Data_Plotting(x,y,title):
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.xticks( rotation=30, horizontalalignment='right' )
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel('Duration')
    plt.ylabel(title)
    plt.show()                                                             
    plt.savefig('utilisation.png')
    
def Data_preparation(fname,avg,memory):
    mem(memory,fname)    
    for i in avg:
        cpu(i,fname)


    

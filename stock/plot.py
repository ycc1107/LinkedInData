import matplotlib.pyplot as plt
import numpy as np
import csv
lst = []
with open('MeanStdData.txt','r') as f:
    reader = csv.reader(f)
    for line in reader:
        a,b,c = line
        a = a.strip(' ')[2:-1]
        b = b.strip(' ')[1:]
        c = c.strip(' ')[:-3]
        lst.append([a,float(b),float(c)])

x,y, name =[],[],[]
for line in lst:
    if isinstance(line[1],float) and isinstance(line[2],float):
        if 1 > line[1] > 0 and 5 >line[2] > 0:
            x.append(line[1])
            y.append(line[2])
            name.append(line[0])
        
plt.scatter(x,y)
plt.show()

import os
from collections import Counter

path = r'C:\Users\lenovo\Desktop\iTunes Crash Logs'
nameList = os.listdir(path)
for name in nameList:
    L = []
    new_path = os.path.join(path,name)
    with open(new_path,'r')as f:
        for line in f.readlines():
            for i in line.split():
                L.append(i)
        #print(L)
        c = Counter()
        for ch in L:
            c[ch] = c[ch] + 1
        print(c.most_common())
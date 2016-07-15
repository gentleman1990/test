import requests
import shutil
import time
import os
import re
import csv

timestr = time.strftime("%Y%m%d")
print timestr

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

listFile = os.listdir("graphanaLogsFresh/")
listFile.sort(key=natural_keys)

valueList = []
fiveMinutesAgo = []
tenMinutesAgo = []
fiveteenMinutesAgo = []

fiveMinutesAgo.append("Undefined")
fiveMinutesAgo.append(timestr)
tenMinutesAgo.append("Undefined")
tenMinutesAgo.append(timestr)
fiveteenMinutesAgo.append("Undefined")
fiveteenMinutesAgo.append(timestr)

for i in listFile:
    if i.endswith(".csv") or i.endswith(".py"):
        with open("graphanaLogsFresh/"+i, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                valueList.append(row[2])
        fiveMinutesAgo.append((valueList[(len(valueList)-2)]))
        tenMinutesAgo.append(valueList[(len(valueList)-3)])
        fiveteenMinutesAgo.append(valueList[(len(valueList)-4)])
        valueList = []
        print i
        continue
    else:
        continue

with open("grafanaData15Minutes.csv", 'ab') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(fiveteenMinutesAgo)
    spamwriter.writerow(tenMinutesAgo)
    spamwriter.writerow(fiveMinutesAgo)
csvfile.close()

from plot import ploting
import os
import glob

trgg_num = 0
events = 0
dir = '../data/'
file_pattern = os.path.join(dir, '*.csv')
files = glob.glob(file_pattern)
Is_Triggered = False
for file in files:
    events += 1
    Is_Triggered = ploting(file)
    if Is_Triggered:
        trgg_num += 1
        #  print(events)
print('number of triggered events: ', trgg_num)
print('total events: ', events)
print('efficiency: ', float(trgg_num)/float(events))

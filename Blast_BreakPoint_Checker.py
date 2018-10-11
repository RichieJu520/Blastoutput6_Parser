# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 15:10:38 2018

@author: jufeng
"""

a = {}
b = []

filename1 = 'example.ublast'
filename2 = 'example.faa'


for line in open(filename ,'r'):
    lis = line.strip().split('\t')
    try:
        a[lis[0]] = a[lis[0]] + line
    except KeyError:
        a[lis[0]] =  line
        b.append(lis[0])
print len(a)

print 'The blast job breaks at ID: ' + b[-2]
c = b[:(-2)]   ## discard the last ids

f1 = open(filename1.replace('.ublast','')+'-1.ublast','w')

for item in c:
    f1.write(a[item])
    
f1.close()

print 'Extracting unifnished DNA sequences from ID: ' +  b[-2]

i, j, k = 0, 0, 0
f2 = open(filename2.replace('.faa','')+'-2.faa','w')

for line in open(filename2,'r'):
    j += 1
    ID = line[1:].rstrip()
    if ID == b[-2]:
        f2.write(line)
        i+=1
        k+=1
    else:
        if i==1:
            f2.write(line)
            k+=1
        else:
            continue
print j/2, 'sequences in total'
print k/2, 'sequences has NOT YET been blasted!'
print round(float(k)/j, 2)*100, '% unfinished sequences to be continued!'
f2.close()

print 'DONE!'

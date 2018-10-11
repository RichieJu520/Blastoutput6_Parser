# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 15:10:38 2018

@author: jufeng
"""

import os
import shutil

BlastPath = "Blast_unfinished"
FaaPath = "Fasta"
SampleList = "SampleID.txt"

if os.path.exists(SampleList + '_BlastBreakPoints'):
    shutil.rmtree(SampleList+ '_BlastBreakPoints')
os.makedirs(SampleList + '_BlastBreakPoints')


DIC = {}
i = 0
for line in open(SampleList,'r'):
    i += 1
    DIC[line.strip()] = i
    
LIST = DIC.keys()
if i - len(LIST) != 0:
    print (i-len(LIST)), 'redundant IDs ignored!'


for SampleID in LIST:
    
    print "------------------", SampleID, "---------------------"
    
    a = {}
    b = []
    
    filename1 = BlastPath + '/'+ SampleID + '.uniref90.20180926.ublast' ## Blast file
    
    for line in open(filename1,'r'):
        lis = line.strip().split('\t')
        try:
            a[lis[0]] = a[lis[0]] + line
        except KeyError:
            a[lis[0]] =  line
            b.append(lis[0])
    print len(a)
    
    print 'The blast job breaks at ID: ' + b[-2]
    c = b[:(-2)]   ## discard the last ids
    
    f1 = open(SampleList + '_BlastBreakPoints' + '/' + SampleID + '-1.ublast','w')
    
    for item in c:
        f1.write(a[item])
        
    f1.close()
    
    filename2 = FaaPath + '/'+ SampleID + '.faa' ## Fasta file
    print 'Extracting unifnished DNA sequences from ID: ' +  b[-2]
    
    i, j, k = 0, 0, 0
    f2 = open(SampleList + '_BlastBreakPoints' + '/' + SampleID+'-2.faa','w')
    
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
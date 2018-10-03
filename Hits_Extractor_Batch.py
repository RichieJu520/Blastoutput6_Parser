print 'This script is written for extracting top [Num] hits from a folder containing blast outputfiles!'

# -*- coding: utf-8 -*-

"""
@author: jufeng
@email:   jufeng@westlake.edu.cn
"""
import os
import time, sys

Parameters=raw_input('Enter two parameters: [foldername],[Num] separated by SPACE: ')

while True:
    try:
        foldername=Parameters.split(' ')[0]
        Number=Parameters.split(' ')[1]
        if not os.path.exists(foldername):
            foldername=raw_input("Tips: invalid [foldername],pls re-enter [file]: ")    
        break
    except:
        Parameters=raw_input('Enter two parameters: [foldername],[line_number]')


if os.path.exists('T'+Number+'_'+foldername):
    for root, dirs, files in os.walk('T'+Number+'_'+foldername):
        for name in files:
            os.remove(os.path.join(root,name))
else:
    os.mkdir('T'+Number+'_'+foldername)

for root,dirs,files in os.walk(foldername):
    for file in files:
        print '------','Processing',file,'in prograss','------'
    
        f1=open(os.path.join(root, file),'r')
        f2=open('T'+Number+'_'+foldername+'/'+'T'+Number+'_'+file,'w')

        a=[]
        start=time.time()
        wrerr=sys.stderr.write

        i=0
        for line in f1:
            i+=1
            if i%100000==0:
                print i,'blast results have been processed!'
            a.append(line.split('\t')[0].strip())
            
            if a.count(line.split('\t')[0].strip()) > int(Number):
                continue
            else:
                f2.write(line)

            if len(set(a))==10:
                a=a[-(int(Number)+1):]
            
        end=time.time()
        wrerr("OK, worked finished in %3.2f secs\n" % (end-start))  


print 'DONE!'





# -*- coding: utf-8 -*-

"""
@author: jufeng
@email:   jufeng@westlake.edu.cn
"""
import os
import time, sys

print 'Function: this python shell is designed for filter blast output formt 6 at a given cutoffs!'
while True:
    Parameters=raw_input("Enter parameters: [foldername](fasta files),[min_identity]%,[min_align_len],[evalue] and [min_bitscore] cutoff sepeated by Space: ")
    try:
        foldername=Parameters.split(' ')[0]
        similarity=Parameters.split(' ')[1]
        align_num=Parameters.split(' ')[2]
        evalue=Parameters.split(' ')[3]
	bitscore=Parameters.split(' ')[4]
        if not os.path.exists(foldername):
            print 'errors: [foldername] not found in the working directory!'
            continue
        break
    
    except:
        print 'errors: invalid input format or not enough input !'
        continue
    
#(1)Filtering

if os.path.exists(foldername+'_'+similarity+'_'+align_num+'_'+evalue+'_'+bitscore):
    for root, dirs, files in os.walk(foldername+'_'+similarity+'_'+align_num+'_'+evalue+'_'+bitscore):
        for name in files:
            os.remove(os.path.join(root,name))        
else:
    os.mkdir(foldername+'_'+similarity+'_'+align_num+'_'+evalue+'_'+bitscore) 

for root,dirs,files in os.walk(foldername):
    for file in files:
               
        start=time.time()
        wrerr=sys.stderr.write

        print '------','Processing',file,'in prograss','------'
        count, seq = 0, 0

        output=open(foldername+'_'+similarity+'_'+align_num+'_'+evalue+'_'+bitscore+'/'+file+'.filtered.blast', 'w')
        
        for line in open(os.path.join(root, file), 'r'):

            seq+=1
            lis = line.strip().split('\t')

            A, B, C, D = float(lis[2]), float(lis[3]), float(lis[10]), float(lis[11])
            
            if A>= float(similarity) and B>= float(align_num) and C<=float(evalue) and D >= float(bitscore) :
                output.write(line.strip()+'\n')
                count+=1

            if seq%100000==0:
                print 'More than'+' '+str(seq)+' '+'hits have been Filtered in '+foldername

        print seq,'hits in total!'
        print str(count)+' '+'query ids left after filtering at given cutoffs'
        end=time.time()
        wrerr("OK, (1)Filtering finished finished in %3.2f secs\n" % (end-start))

print 'DONE!'




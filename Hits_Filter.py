print 'This script is written for extracting filtering blast hits using reads length and alignment_length coverage!'
import os

while True:
    Parameters=raw_input("Enter parameters 1.[.blast], 2.[fasta], 3.[Min_Identity], 4.[Min_len_cov] and 5.[Max_e-value] sepeated by Space: ")
    try:
        X1=Parameters.strip().split(' ')[0]
        X2=Parameters.strip().split(' ')[1]
        X3=float(Parameters.strip().split(' ')[2])
        X4=float(Parameters.strip().split(' ')[3])
        X5=float(Parameters.strip().split(' ')[4])
    
        break
    except:
         print 'Errors: invalid input format or not enough input !'
         continue

f=open(str(X1)+'_ID'+str(X3)+'_FR'+str(X4)+'_EV'+str(X5)+'.blast','w')

i, j = 0, 0
a = {}
for line in open(X2,'r'):
    i+=1
    
    if i ==1 and line.startswith('>'):
        ID = line.strip()[1:]
        continue
    
    if line.startswith('>'):
        a[ID] = j
        ID = line.strip()[1:]
        j = 0
    else:
        j+=len(line.strip())
a[ID] = j
        
print len(a), 'sequences in the fasta file!'
print float(sum(a.values()))/len(a), ' average read length'


j,k=0,0
for line in open(X1,'r'):
    k+=1
    if k%100000==0:
        print k,'hits have been processed!'
    lis=line.split('\t')
    
    print lis[0]
    identity = float(lis[2])
    align_num = float(lis[3])
    try:
        fraction = float(lis[3])/a[lis[0]]
    except KeyError:
        continue
    evalue = float(lis[10])
    bitscore = float(lis[11])
    
    if identity >=X3 and fraction >=X4 and evalue <= X5:
        f.write(line)
    else:
        j+=1

print j,'out of',k,'hits were discarded by filtering!'
    
print 'OK, Finished!'
f.close()
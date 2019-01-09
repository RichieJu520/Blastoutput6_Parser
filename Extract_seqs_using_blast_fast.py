file_name1= "ID.txt" ###Enter the full name of .blast file
file_name2= "abc.fa" ###Enter the full name of the fasta contains the query sequences

fileinput =open(file_name1,'r')
fileoutput=open(file_name1.replace('.txt','')+'.extracted.fa','w')

print('The Python script is running... Pls wait!')

a={}
m=0
for line in open(file_name1,'r'):
    m+=1
    a[str(line).strip().split('\t')[0]]=m   
print(len(a),'unique ids in '+file_name1)


Num, b = 0, []

for line in open(file_name2,'r'):
    
    Num+=1
    if Num%1==0:
        print(Num, 'sequences have been searched!')
        
    if line.startswith('>'):
        ID = str(line.rstrip().split(' ')[0][1:])
        n = 0
        try:
            j = a[ID]
            fileoutput.write(line)
            print(ID)
            n += 1
        except KeyError:
            continue
    else:
        if n == 1:
            fileoutput.write(line)
        else:
            continue

fileinput.close()
print('OK, Finished!')

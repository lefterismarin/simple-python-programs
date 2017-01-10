list=[]
infile=open("3.txt", 'r')
list=[eval(line) for line in infile]
infile.close()

nzeros=[x for x in list if x<0 or x>0]
zeros=[x for x in list if x==0]
print(nzeros+zeros)


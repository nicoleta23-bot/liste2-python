nume=[]
with open('input.txt','r') as f:
    x=f.readlines()
for i in x:
    nume.append(i) 
nume=sorted(nume)
with open('crescator.txt','w') as f:
    f.writelines(nume)
nume.sort(reverse=True) 
with open('descrescator.txt','w') as f:
    f.writelines(nume)  
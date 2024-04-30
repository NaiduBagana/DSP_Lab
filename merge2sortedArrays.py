a=[1,5,6,7]
b=[2,7,8,9]
i=0
j=0

l=[]
while i<len(a) and j<len(b):
    if(a[i]<b[j]):
        l.append(a[i])
        i=i+1
    else:
        l.append(b[j])
        j=j+1

while i<len(a):
    l.append(a[i])
    i=i+1

while j<len(b):
    l.append(b[j])
    j=j+1

print(l)

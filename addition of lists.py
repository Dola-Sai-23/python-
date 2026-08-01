l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
print(l3)
for i in range(len(l3)):
    for j in range(i,len(l3)):
        if(l3[i]>l3[j]):
            l3[i],l3[j]=l3[j],l3[i]
        else:
            l3[i],l3[j]=l3[i],l3[j]
    print(l3)
print(l3)
print("-------------------------------------------")
#BY USING MERGE SORT ALG:-
"""
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
i=0
j=0
m=len(a)
n=len(b)
while i<m and i<n :
    if a[i] <b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j+=1
while i<m:
    c.append(a[i])
    i+=1
while j<n:
    c.append(b[j])
    j+=1
print(c)
    """







        

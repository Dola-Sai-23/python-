l=[1,2,3,4,5]
k=int(input())
t=int(input())
r=[]
for i in range(len(l)-k+1):
    total=0
    for j in range(k):
        total+=l[i+j]
    r.append(total)
    if(total<=t):
        print(total,l[:j-k+1:j+1,k])
print(r)
print("--------------------------")

    


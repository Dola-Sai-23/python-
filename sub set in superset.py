"""# for single element in the list
l1=list(map(int,input().split()))
k=int(input())
for i in range(len(l1)):
    if(l1[i]==k):
        print(i)
        break
for j in range(i,len(l1)):
    if(l1[j]<k):
        j=j+1
    elif(l1[j]>k):
        print(l1[j])
        break
    elif(j>=len(l1)):
        print("-1")
#for two sub set and super set
"""
#with high time complexity
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
for q in l2:
    for i in range(len(l1)):
        if l1[i] ==q:
            ti=i
            break
    for j in range(ti+1,len(l1)):
        if l1[j]>q:
            print(l1[j])
            break
    else:
        print("-1")
print("________________________________")
s=[]
d={}
a=[]
for i in range(len(l1)-1,-1,-1):
    while s and s[-1]<l1[i]:
        s.pop()
    if s and s[-1]>l1[i]:
        d[l1[i]]=s[-1]
        s.append(l1[i])
    else:
        d[l1[i]]=-1
        s.append(l1[i])
for j in l2:
    a.append(d[j])
print(a)

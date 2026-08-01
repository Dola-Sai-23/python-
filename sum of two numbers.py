a=list(map(int,input().split()))
t=int(input("enter target:"))
"""
flag=False
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i],a[j])
        if a[i]+a[j] ==t:
            print("index values:",i,j)
            break
    if flag:
        break
        """

d={}
"""
for i in range(len(a)):
    t=t-a[i]
    if t in d:
        print("index:",d[a[i]],i)
    else:
        z=t-a[i]
        print(a[i])
   """
i=0
j=len(a)-1
while i<j:
    print(a[i],a[j])
    p=a[i]+a[j]
    if p==t:
        print(i,j)
        break
    elif p>t:
        j-=1
    elif p<t:
        i+=1

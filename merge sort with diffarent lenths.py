a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=4
n=3
i=m-1
j=n-1
k=len(a)-1
while i>=0 and j>=0:
    if a[i] >b[j]:
        a[k]=a[i]
        i-=1
    else:
        a[k]=b[j]
        j-=1
    k-=1
print(a)
while j>=0:
    a[k]=b[j]
    j-=1
    k-=1
print(a)

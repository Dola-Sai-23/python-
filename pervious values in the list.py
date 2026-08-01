"""
l=list(map(int,input().split()))
n=len(l)
z=1
c=[1]*n
for j in range(n-1,-1,-1,):
    c[j]=z
    z=z*l[j]
print(c)
"""
a=5
b=8
a=a^b
b=a^b
a=a^b
print(a,b)

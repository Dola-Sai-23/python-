""""
s=input("enter a string")
m=0
for i in range(len(s)):
    s1=" "
    for j in range(i,len(s)):
        if(s[j] not in s1):
            s1=s1+s[j]
            
        else:
            break
    print(s1,len(s1))
    m=max(m,len(s1))

print(s1,m)
"""
i=0
d={}
z=' '
m=0
for i in range(len(s)):
    if s[i] in d and d[s[j]]>i:
        l=j-i
        i=d[s[j]]+1
        m=max(m,l)
    d[s[j]]n
            

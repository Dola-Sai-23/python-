s=input("enter string")
k=int(input())
m=0
"""
for i in range(len(s)):
    ch=' '
    z=' '
    for j in range(i,len(s)):
        if s[j] not in ch and len(ch)<k:
            ch=ch+s[j]
        if len(ch)>k:
            break
        z=z+s[j]
    print(z,len(z))
    m=max(m,len(z))
print(m)
        """
i=0
d={}                                         
for j in range(len(s)):
    d[s[j]]=d.ger(s[j],0)+1
    print("before:",d)
    while len(d)>k:
        d[s[i]]=d[s[i]]-1
        if d[s[i]]==0:
            d.pop(s[i])
        i+=1
    l=j+1
    m=max(m,l)
print(m)

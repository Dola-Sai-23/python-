s1=input()
s2=input()
d={}
e={}
for i in range(len(s1)):
    if s1[i] in d:
        z=d[s1[i]]
        z.append(i)
        d[s1[i]]=z
    else:
        z=[i]
        d[s1[i]]=z
    if s2[i] in e:
          z=e[s2[i]]
          z.append(i)
          e[s2[i]]=z
    else:
        z=[i]
        e[s2[i]]=z
a=list(d.values())
b=list(e.values())
if( len (a)==len (b)):
    for i in range( len (a)):
        if(a[i]!=b[i]):
            print("Not isomorophic")
            break
        else:
            print("Isomorphic")
            break5
       
        

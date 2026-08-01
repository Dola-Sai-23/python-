"""
VII-7
IX-9
"""
def roman(s):
    z=0
    for i in range(len(s)-1):
        if d[s[i]]>=d[s[i+1]]:
            z+=d[s[i]]
        else:
            z-=d[s[i]]
    z+=d[s[-1]]
    return z
def checkvalid(s):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range (len(s)-3):
        if s[i]==s[i+1]:
            if s[i]==s[i+2]:
                if d[s[i]]<=d[s[i+3]]:
                    return "invalid"
                else:
                    if d[s[i]]<d[s[i+2]]:
                        return "invalid"
    for i in range(len(r)-1):
        if 2*d[s[i]]==d[s[i+1]]:
            return "invalid"
    return roman(r)



                
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=input()
z=0
for i in range(len(s)-1):
    if d[s[i]]>=d[s[i+1]]:
        z+=d[s[i]]
    else:
        z-=d[s[i]]
z+=d[s[-1]]
print(z)



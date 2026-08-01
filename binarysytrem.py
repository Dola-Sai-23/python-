#binary operations
def binarysystem(s):
    if s==' ':
        return -1
    r=int(s[0])
    for i in range(1,len(s),2):
        if( s[i]=='A'):
            r=r&int(s[i+1])
        elif( s[i]=='B'):
            r=r |int(s[i+1])
        else:
            r=r^ int(s[i+1])
    return r
z=input("enter the equation:")
print(binarysystem(z))
        

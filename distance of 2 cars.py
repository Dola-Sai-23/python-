x1,v1,x2,v2=list(map(int,input().split()))
i=1
c1=0
c2=0
if x1>x2:
    fp=x1
    sp=x2
    fv=v1
    sv=v2
else:
    fp=x2
    sp=x1
    fv=v2
    sv=v1
if fv>sv:
    print("NO")
else:
    i=0
    while True:
        i+=1
        fp=fp+fv
        sp=sp+sv
        if(fp==sp):
            print("Yes Meets at minutes",i)
            break
        elif sp>fp:
            print("NO",i)
            break
z=(x2-x1)%(v1-v2)
if z==0:
    print("Yes",i)
else:
    print("NO",i)

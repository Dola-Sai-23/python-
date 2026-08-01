#find the Small Number of a given 2 Numbers?
a=int(input('enter four numbers :'))
b=int(input())
c=int(input())
d=int(input())
big= a if a>b else b and a if a>c else c and a if a>d else d
print("Big number:",big)
 

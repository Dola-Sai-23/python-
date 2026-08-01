#list slicing
L1=[10,20,30,40,50,60,70,80,90,100]
print(L1)


print('first elements:',L1[0])
print('last elements:',L1[-1])
print('2 to 5 elements:',L1[2:6])
print('from 5 to all',L1[5:])
print('reverse of a list:',L1[::-1])


print('list sum:',sum(L1))
print('length of list:',len(L1))
print('max.value',max(L1))
print('min.value',min(L1))
#inserting elements into the list
L1[2]=25
print(L1)
L1.append(5)
print(L1)
L1.insert(5,55)
print(L1)
L1.extend([25,35,45])
print(L1)
# delete the elements from the list
x=L1.pop()
print('Removed Elements:',x)
print(L1)
# remove specified Element
x=50
L1.remove(x)
print(L1)
#list copy
L2=L1*2
print(L2)
#repeated list
L3=L1+L2
print(L3)
#delete list
del L3
print(L3)

#program for  using a list
Student=[]
x=int(input('enter list size:'))
for i in range(x):
    sno=int(input('enter student roll number:'))
    sname=input('enter student name:')
    course=input('enter course:')
    Student.append((sno,sname,course))
    
print('Student Report:')
for x,y,z in Student:
    print('ROll number:',x,'name:',y,'course',z)
    
print(Student)

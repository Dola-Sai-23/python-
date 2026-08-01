def is_leap(year):
    leap =False
    
    # Write your logic here
    if(year%4!=0 and year%400!=0):
        print("False")
        if(year%100!=0):
            print("False")
    return True

year = int(input())
print(is_leap(year))

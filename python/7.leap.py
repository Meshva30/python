year=int(input("Enter the Year:"))
if(year%4==0 and year%100 or year%400==0):
    print("The Year is a Leap year!!!")
else:
    print("The Year is not Leap year!!!")
#This is my first GitHub tutorial
#Program to check number is divisible by 5 and 11
number = int(input("Enter a number: "))
if (number % 5 == 0) and (number % 11 == 0):
    print("Given Number {0} is divisible by 5 and 11".format(number))
else: 
    print("Given Number {0} is not divisible by 5 and 11".format(number))
    
    
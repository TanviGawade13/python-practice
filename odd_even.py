# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num=int(input("Enter any number : "))
check=int(input("Enter number to divide by : "))
if num%check==0:
    print(f"{num} is evenly divided by {check}")
else:
    print(f"{num} is not divided by {check}")

if num%4==0:
    print(f"{num} is a multiple of 4")
elif num%2==0:
    print(f"{num} is a even number")
elif num%2!=0:
    print(f"{num} is a odd number")
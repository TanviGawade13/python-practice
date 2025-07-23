# Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


num=int(input("Give me a number and i will give you all the divisors of that number : "))
lst=[]
for i in range(1,100):
    if num%i==0:
        lst.append(i)
        lst.sort()

print(f"List of divisors of {num} are : {lst}")


# Exercise 6 
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


new_str = input("Enter any string : ")
if new_str == new_str[::-1]:
    print("String is pallindrome")
else:
    print("String is not pallindrome")


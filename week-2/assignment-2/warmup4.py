#number = input("Enter your preferred number: ")
#plus = 10
#number_new = number + plus
#print(f"The number you entered plus 10 equals: {number_new}")

#Traceback (most recent call last):
#  File "C:\Users\Geral\Desktop\python-intro-homework\week-2\assignment-2\warmup4.py", line 3, in <module>
#    number_new = number + plus
#                 ~~~~~~~^~~~~~
#TypeError: can only concatenate str (not "int") to str

#1. Error message: TypeError.
#2. Caused by attempting to add a string variable received from the input to an integer.
#3. I solved it by assigning the integer variable to the number received from the input.

number = int(input("Enter your preferred number: "))
plus = 10
number_new = number + plus
print(f"The number you entered plus 10 equals: {number_new}")
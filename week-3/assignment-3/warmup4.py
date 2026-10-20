number1 = int(input("Enter a number: "))
if number1 < 0:
    print(f"{number1} is negative.")
elif number1 >0:
    print(f"{number1} is positive.")
else:
    print(f"{number1} is zero.")

if number1 % 2 == 0:
    print(f"{number1} is even.")
else:
    print(f"{number1} is odd.")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    try:
        result = num1 / num2
        print("Result is:", result)

    except ZeroDivisionError as e:
        print(e)
        print(" You cannot divide by zero!")

except ValueError as e:
    print(e)
    print(" Please enter valid numbers only!")

finally:
    print("Code executed successfully.")

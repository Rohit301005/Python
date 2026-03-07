# python program to create a calculator

# 1.function for operation
# 2.user input
# 3.print result

# function for addition
def add(num1,num2):
    return num1 + num2


# function for subtraction
def sub(num1,num2):
    return num1 - num2

# function for multiply
def multiply(num1,num2):
    return num1 * num2

# function for divide
def divide(num1,num2):
    return num1 / num2

# function for average
def avg(num1,num2):
    return (num1 + num2)/2


print("Please select a operation: \n" \
      "1.Addition \n" \
        "2.Subtraction \n" \
            "3.Multiply \n"\
                "4.Divide\n" \
                    "5.Average \n")


# Taking user input

select = int(input("Select a operation 1,2,3,4,5: "))

number1 = int(input("Enter the 1st number : "))
number2 = int(input("Enter the 2nd number : "))


# Result

if select == 1:
    print("Sum of two number " ,add(number1,number2))
elif select == 2:
    print("Subtraction of two number",sub(number1,number2))
elif select == 3:
    print("Multiplication of two number",multiply(number1,number2))
elif select == 4:
    print("Division of two number",divide(number1,number2))
elif select == 5:
    print("Average of two number",avg(number1,number2))
else:
    print("Select a valid reult")
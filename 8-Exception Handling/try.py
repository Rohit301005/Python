try:
    a = int(input("Enter value: "))
    b = int(input("Enter value: "))

    result = a / b
    print(result)

except Exception as e:
    print(e)
finally:
    print("Program End")
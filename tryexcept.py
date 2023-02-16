try:
    number = int(input("Enter a number only: "))
    print(number)

except ValueError as err:
    print(err)
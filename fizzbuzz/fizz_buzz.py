def fizz_buzz(number: int) -> str:
    """
    Prints out a message related to the input number
    :param number: value to be checked for divisibility by 3 and 5
    If the number is divisible by 3 only, the function prints "fizz"
    If the number is divisible by 5 only, the function prints "buzz"
    If the number is divisible by both 3 and 5, the function prints "fizz buzz"
    """
    if (number % 3 == 0) and not (number % 5 == 0):
        return "fizz"
    elif (number % 5 == 0) and not (number % 3 == 0):
        return "buzz"
    elif (number % 5 == 0) and (number % 3 == 0):
        return "fizz buzz"
    else:
        return str(number)


# Example of the function in action for the first 100 integers
for i in range(1, 101):
    print(fizz_buzz(i))

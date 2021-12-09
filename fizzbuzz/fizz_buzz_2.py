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


# Example of the function in action. The computer and the player take turns
# guessing whether the numbers are divisible by 3, by 5 or both.
# The game is over whenever 100 is reached or an incorrect answer is given
# by the player

for i in range(1, 101, 2):
    num = i
    next_num = i + 1
    print(fizz_buzz(i))
    if num == 100:
        print("The game is over.")
        break
    correct_answer = fizz_buzz(next_num)
    players_answer = (input("Your go:")).casefold()
    if players_answer == correct_answer:
        pass
    else:
        print("Game over. You lost.")
        break

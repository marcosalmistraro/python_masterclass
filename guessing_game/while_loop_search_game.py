import random as rand


def get_integer(prompt, limit) -> int:
    """
    Get an integer from standard input (stdin.)
    Keep looping until a valid entry is accepted
    :param prompt: string that is visible to the user when prompted
        to enter a value
    :param limit: defines the limit for the guess range
    :return: returns an integer value
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric() and (int(temp) in range(int(limit) + 1)):
            return int(temp)
        print("{} is not a valid entry".format(temp))


# Optionally prints the function's docstring
print(get_integer.__doc__)

# Set the upper limit for the game
highest = 1000
answer = rand.randint(1, highest)
print(f"For test purposes - the answer is: {answer}")   # TODO Remove after testing

# Starting the game
print("Please guess a number between 1 and {}: ".format(highest))
guess = get_integer(": ", highest)
count = 0
while guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = get_integer(": ", highest)
        count += 1
    elif guess > answer:
        print("Please guess lower")
        guess = get_integer(": ", highest)
        count += 1

# Outputting the results
print("Well done, you guessed it!")
print("It took you {} tries".format(count))
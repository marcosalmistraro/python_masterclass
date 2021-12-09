def guess_binary(low, high) -> int:
    """
    Guesses a number in between a given range using a binary search algorithm
    :param low: lowest end of the guessing range
    :param high: highest end of the guessing range
    :return: the amount of guesses taken to get the correct answer
    """
    guesses = 1
    while True:
        print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        user_input = input("My guess was {}. "
                           "Enter h if I should guess higher, "
                           "l for lower or c if the guess was correct".format(guess))
        if user_input == "h":
            print("I have to guess higher. "
                  "The low end of the range becomes 1 greater than the guess.")
            low = guess + 1
        elif user_input == "l":
            print("I have to guess lower.  "
                  "The high end of the range becomes 1 less than the guess.")
            high = guess - 1
        elif user_input == "c":
            return guesses
        guesses += 1


# Example of the function in action

LOW = 1
HIGH = 1000

print("Please think of a number between {} and {}".format(LOW, HIGH))
input("Press ENTER to start")

number_of_guesses = guess_binary(LOW, HIGH)
print("I got it in {} tries.".format(number_of_guesses))


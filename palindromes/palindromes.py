def palindrome(string: str) -> bool:
    """
    Checks if the entered `string` is a palindrome.
    A palindrome is a sentence that can be read backwards and forward
    with no change.
    The function accepts any alphanumeric `string` as input
    :param string: The string to be checked
    :return: Boolean vale indicating whether
    the sentence is a palindrome
    """
    # The .split method returns a list
    split_string = string.split(" ")
    # The .join method returns a string
    joined_string = "".join(split_string)
    return joined_string.casefold() == joined_string.casefold()[::-1]


def rem_blank(string: str) -> str:
    split_string = string.split(" ")
    joined_string = "".join(split_string)
    return joined_string


def rem_punctuation(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalnum():
            new_string += char
    return new_string


# Example of the function in action
sentence = input("Please enter a sentence to test. Q to quit.")
while True:
    no_blank_sentence = rem_blank(sentence)
    new_sentence = rem_punctuation(no_blank_sentence)
    if new_sentence == "q".casefold():
        break
    if new_sentence.isalnum():
        if palindrome(new_sentence):
            print("{} is a palindrome".format(sentence))
            break
        else:
            print("{} is not a palindrome".format(sentence))
            break
    else:
        sentence = input("Please enter an alphanumeric string. Q to quit.")

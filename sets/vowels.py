# This script allows the user to extrapolate all consonants
# in a given set of characters.
# This can be extracted from a .txt file or entered manually

# Initialize vowel set
vowels = {"a", "e", "i", "o", "u"}

# Take input from the user
text = input("Enter your text here. "
             "Press 0 if you want to upload a file. "
             "The file path needs to be entered accordingly")

# Add option for text input
if text == '0':
    set_output = set()
    file_path = input("Enter the file path")
    with open(file_path, "r") as file:
        for line in file:
            print("*" * 80)
            print("Line string: {}".format(line))
            line_set = set(line.casefold())
            print("Set from line string: {}".format(line_set))
            print("*" * 80)
            set_output = set_output.union(line_set)
    print("The set that was obtained from the file is : {}".format(set_output))

# Option for manually entered string
else:
    set_output = set(text.casefold())

# Compute intersection with the vowel set
result_set = set_output.difference(vowels)
result_set.discard(" ")
result_set.discard("\n")
result = sorted(list(result_set))

print("The resulting set is: {}".format(result))
print("There are {} different consonants in the set".format(len(result)))

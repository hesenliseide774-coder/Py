sentence = input("Enter a string: ")
sentence = sentence.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
pangram = True  # assume it is a pangram

for letter in alphabet:
    if letter not in sentence:  # check if the letter is missing
        pangram = False
        break  # no need to check further

if pangram:
    print("True")
else:
    print("False")

str = input("Enter a message:")
which_character = input("Enter character to count")
count_of_character = 0
index = 0

while index < len(str):
    character = str[index]
    if character == which_character:
        count_of_character = count_of_character + 1

    index = index + 1

print("count of character", count_of_character)

# Print length of a string
# name = input("What is your name? ")
# print("Your name has", len(name), "characters")

# if, elif, else
# name = input("What is your name? ")
# if len(name) > 5:
#     print("Your name has more than 5 characters")

# print("Your name is", name)

# some_number = int(input("Enter a random number: "))
# if some_number > 0:
#     print("You entered a Positive number")
# else:
#     print("You entered a Negative number")

# some_number = int(input("Enter a random number: "))
# if some_number > 0:
#     print("You entered a Positive number")
# elif some_number == 0:
#     print("Your entered Zero")
# else:
#     print("You entered a Negative number")

# Looping
# numbers = [1,2,3,4,5]
# for n in numbers:
#     print(n)

#some_word = "supercaligragilistdocious"
#for character in some_word:
#    print(character)

# colors = ["red", "green", "blue", "yellow", "cyan"]
# for color in colors:
#     print("The color is", color)

# for n in range(10):
#     print(n)

# for n in range(0, 10, 2):
#     print(n)

# for n in range(1, 10, 2):
#     print(n)

# print("Before loop")
# num = 5
# while num > 0:
#     print("Inside the loop", num)
#     num -= 1

# print("After loop")

# while True:
#     num = int(input("Enter a number: "))
#     if num == 37:
#         print("Bye...")
#         break
#     else:
#         print("You entered", num)

# spaces = 0
# line = input("Enter a sentence: ")
# for c in line:
#     if c == ' ':
#         spaces += 1
# print("Word count:", spaces + 1)

from random import randint

user_password = input("Enter your password: ")

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1',
              '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
              '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|']

guessed_password = ""

while guessed_password != user_password:
    guessed_password = ""

    for _ in range(len(user_password)):
        random_character = characters[randint(0, len(characters) - 1)]
        guessed_password = str(random_character) + str(guessed_password)
        print(guessed_password)

print("Your Password is:", guessed_password)

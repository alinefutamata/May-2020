# Ask the user to write a number and print if this number is even or odd

number = input("Write a number: ")

if int(number) % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number 1-10, and you will try to guess it.")

number = random.randint(1,10)
print("System random number = ", number)
isGuessRight = False

while(isGuessRight == False):
    guessNumber = input("Place your numbers...")
    guessNumber = int(guessNumber) # Semua inputan dari shell, itu dianggap strin. Agar sistem bekerja dengan baik, maka harus di konversi ke int
    if(guessNumber == number):
        print("You Win! Your number is correct!")
        isGuessRight = True
    else:
        print("Ohhh, please try again.")

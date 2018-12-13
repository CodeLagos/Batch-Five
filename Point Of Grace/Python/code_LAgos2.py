#ANIMASHAUN QUDUS OLAKUNLE CODE LAGOS PROJECT DECEMBER 2018

#BUILDING A GUESSING GAME
print("=> GUESSING GAME <=")
print("======================")

print("Guess the name of our instructor at CODE LAGOS(Ogolonto)... ")
#CREATING  VARIABLE TO STORE OUR SECRETE WORD
secret_word = "OLUWASEGUN"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
#SRCIPT TO EXECUTE OUR GAME
while guess != secret_word.lower() and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("sorry, you are out of guesses... YOU LOSE! ")
else:
    print("Nice, You Win!")

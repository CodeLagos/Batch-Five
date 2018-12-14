#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#hassan olaoluwa
print("This is console module")
from random import randint
score = 0
#display the instructions
print("Welcome to Rock, Paper, Scissors Game") 
print("Note: rock breaks the scissors, scissors tears the paper and paper covers the rock") 
player = input("Pick a choice \n(r) rock \n(p) paper \n(s) scissors \n")
if(player == "r" ):
     print("player: Rock")
elif(player =="p"):
     print("player: Paper")
elif(player =="s"):
     print("player: Scissor") 
chosen = randint(1,3)
if(chosen == 1):
     computer ="r"
     print("computer: Rock")
elif(chosen == 2):
     computer ="p" 
     print("computer: Papers")
elif(chosen == 3):
     computer = "s" 
     print("computer: Scissors") 
if(player == computer):
     print("DRAW!")
elif(player == "r" and computer == "s" ):
     print("Player wins")
     score =score + 1
     print(score)
elif(player == "r" and computer == "p" ):
     print("Computer wins!")
     score =score + 0
     print (score)
elif(player == "p" and computer == "r" ):
     print("Player wins!")
     score =score + 1
     print (score)
elif(player == "p" and computer == "s" ):
     print("Computer wins!")
     score =score + 0
     print (score)
elif(player == "s" and computer == "p" ):
     print(" Player wins!")
     score =score + 1
     print (score)
elif(player == "s" and computer == "r" ):
     print("Computer wins!")
     score =score + 0
     print (score)

import random

rock = 'rock'

paper = 'paper'

scissors = 'scissors'
k=input("what do you choose? type  rock, paper or scissors:- \n")
p=random.randint(0,2)
if k=="rock":
  print("You Chose",rock)
  if p==1:
    print("Computer Chose",paper)
    print("you lose")
  elif p==2:
    print("Computer Chose",scissors)
    print("you win")
  elif p==0:
    print("Computer Chose",rock)
    print("draw")
elif k=="paper":
  print("\nYou Chose",paper)
  if p==1:
    print("Computer Chose",paper)
    print("draw")
  elif p==2:
    print("Computer Chose",scissors)
    print("you lose")
  elif p==0:
    print("Computer Chose",rock)
    print("you win")
elif k=="scissors":
  print("\nYou Chose",scissors)
  if p==0:
    print("Computer Chose",rock)
    print("you lose")
  elif p==1:
    print("Computer Chose",paper)
    print("you win")
  elif p==2:
    print("Computer Chose",scissors)
    print("draw")
else:
  print("Invalid Input, Please type correctly")
  exit()
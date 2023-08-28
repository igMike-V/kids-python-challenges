import random

answers =['rock', 'paper', 'scissors']

def playturn():
    random_number = random.randint(0, 2)
    return(answers[random_number])

gameon = True

while gameon: 
  playerin = input("rock, paper, or scissors? ") 
  print("You chose: " + playerin)
  gameon = False 
  
  cpuin = playturn()
  print("CPU chose: " + cpuin) 

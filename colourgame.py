# wait for somthing happens
# then do something
import random
import time


colors = ['red', 'green', 'blue']

# set a random number between 0 and 2
def random_color():
    return random.randint(0,2)
  
gameover = False
numberRight = 0
numberWrong = 0


while gameover == False:
    # get user input
    print('______________________________\n\n')
    
    print('You have guessed ' + str(numberRight) + ' right and ' + str(numberWrong) + ' wrong.')
    userinput = input('Enter a color (RGB) or "exit" to quit : ')
    if userinput.lower() == 'exit':
        gameover = True
        break
    # get random color
    randomcolor = random_color()
    
    if userinput.lower() == 'r':
        userinput = 'red'
    elif userinput.lower() == 'g':
        userinput = 'green'
    elif userinput.lower() == 'b':
        userinput = 'blue'
    # check if input is ok
    if (userinput.lower() in colors):
        print('You entered: ' + userinput.lower())
        if(userinput.lower() == colors[randomcolor]):
            print('You guessed right!')
            numberRight += 1
            # handle the right guess
        else:
            print('You guessed wrong, the color was: ' + colors[randomcolor])
            numberWrong += 1
    else:
        print('That is not a valid colour, try again.')
        
    time.sleep(2)
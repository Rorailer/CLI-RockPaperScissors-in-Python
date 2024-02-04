import random
from os import system
from time import sleep

#Computer Selection
CS = None

#Player Selection
PS = None


def Computer_Selection():
    global CS
    
    CS = random.randint(0,2)
    
    return CS
    
def Player_Selection():
    
    global PS
    
   
    try:
        PS = int(input(f"Select...\nRock ==> 0\nPaper ==> 1\nScissors ==> 2\nQuit ==> 4\nReset Score Board ==> 5\nEnter number : "))
    
    except:
        raise ValueError("Enter an Integer Only.")
            
    return PS        
    
def add_draw():
    
    
    with open("score.txt",'r') as f:
    
        #Reads the score file, It has a format (draws,wins,loses)
        content = f.read()
    
        #stores score as a list 
        score = content.split(',')    
    
    
    with open('score.txt','w') as f:
        
        #writes the score back to the file, only increases the draws by 1.
        f.write(f"{int(score[0])+int(1)},{score[1]},{score[2]}")

def add_win():
    with open("score.txt",'r') as f:
        content = f.read()
        score = content.split(',')
    with open('score.txt','w') as f:
        f.write(f"{score[0]},{int(score[1])+int(1)},{score[2]}")

def add_lose():
    with open("score.txt",'r') as f:
        content = f.read()
        score = content.split(',')  
    with open('score.txt','w') as f:
        f.write(f"{score[0]},{score[1]},{int(score[2])+int(1)}")

def reset_score():
    with open('score.txt','w') as f:
        f.write(f'{0},{0},{0}')

def score_board():
    with open('score.txt','r') as f:
        score = f.read()
        score = score.split(',')
    
    print(f'|| Draws = {score[0]} ||\n|| Wins = {score[1]} ||\n|| Loses = {score[2]} || ')

def clrscr():
    system('clear')

Score = []

#Main While Loop
while True:
        
    #Player Input
    Player_Selection()
    
    
    #Player quit
    if PS == 4:
        break
    
    elif PS  == 5:
        clrscr()
        reset_score()
        score_board()
    #Player wants to play
    else:
        Computer_Selection()
    
    
    
    #Match player and computer
    
    #Draw Case
    if PS == CS and PS != 5:
        clrscr()
        print("Draw!")
        add_draw()
        sleep(2)
        clrscr()
        score_board()
    
    
    #Lose Cases
    elif PS == 0 and CS == 1 and PS != 5:
        clrscr()
        print("Lose!")
        add_lose()
        sleep(2)
        clrscr()
        score_board()

    elif PS == 1 and CS == 2 and PS != 5:
        clrscr()
        print("Lose!")
        add_lose()
        sleep(2)
        clrscr()
        score_board()

    elif PS == 2 and CS == 0 and PS != 5:
        clrscr()
        print("Lose!")
        add_lose()
        sleep(2)
        clrscr()
        score_board()

    #Win Cases
    elif PS == 2 and CS == 1 and PS != 5:
        clrscr()
        print("Win!")
        add_win()
        sleep(2)
        clrscr()
        score_board()
    
    elif PS == 0 and CS == 2 and PS != 5:
        clrscr()
        print("Win!")
        add_win()
        sleep(2)
        clrscr()
        score_board()
    
    elif PS == 1 and CS == 0 and PS != 5:
        clrscr()
        print("Win!")
        add_win()
        sleep(2)
        clrscr()
        score_board()
    
        


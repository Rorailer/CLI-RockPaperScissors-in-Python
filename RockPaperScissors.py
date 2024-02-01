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
        content = f.read()
        f.seek(0)
        draws = int(f.read(1))    
    with open('score.txt','w') as f:
        f.write(content[0:0]+ str(draws+1)+'\n' + content[2:])

def add_win():
    with open("score.txt",'r') as f:
        content = f.read()
        f.seek(2)
        wins = int(f.read(1))  
    with open('score.txt','w') as f:
        f.write(content[0:2]+ str(wins+1) + content[3:])

def add_lose():
    with open("score.txt",'r') as f:
        content = f.read()
        f.seek(4)
        loses = int(f.read(1))   
    with open('score.txt','w') as f:
        f.write(content[0:4]+ str(loses+1) + content[6:])

def reset_score():
    with open('score.txt','w') as f:
        f.write('0\n0\n0')

def score_board():
    with open('score.txt','r') as f:
        score = f.read()
    
    print(f'|| Draws = {score[:1]} ||\n|| Wins = {score[2:3]} ||\n|| Loses = {score[4:5]} || ')

def clrscr():
    system('clear')



#Main While Loop
while True:
        
    #Player Input
    Player_Selection()
    
    
    #Player quit
    if PS == 4:
        try:
            reset_score()
        except:
            pass
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
    
        


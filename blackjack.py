import random

x = random.randint(1,6)
while x < 26:
    if x < 21:
        print("Game on:", x)
        x=x+random.randint(1,6)
    elif x == 21:
        print("You win", x)
        break
    else:
        print("You lose:", x)
        break
       
        
    
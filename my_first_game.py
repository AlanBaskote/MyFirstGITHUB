#First round of direction
import time #Set time in here
items = [] #item list for players
while items == []:
    print('You are in a maze.')
    time.sleep(1)
    print('Which direction do you want to go?')
    time.sleep(1)
    direction1 = input('Left or Right?\n') #choosing left or right
    direction1 = direction1.lower() #Make it lowercase only
    if direction1 == 'left': #Choosing to go left
        print('You found an old map.')
        time.sleep(1)
        print('Do you want to pick it up?')
        direction2 = input('Yes or No?\n') #choosing whether to pick a map up or not
        direction2 = direction2.lower() #lower-case
        if direction2 == 'yes': #pick up a map
            print('You got an "Old map"')
            items.append("Old map")
            time.sleep(1)
            break
        elif direction2 == 'no': #dont' pick a map
            direction2 = direction2.lower()
            print('You choose to ignore the map')
            items.append("Please let me pass")
            time.sleep(1)
            break
        else: 
            print('Please type accordingly')
    elif direction1 == 'right': #Choose to go right
        direction1 = direction1.lower()
        print('You found a weird looking candle\nPick it up?')
        time.sleep(1)
        direction2 = input('Yes or No?\n')
        direction2 = direction2.lower() 
        if direction2 == 'yes': #pick up the candle
            print('You got a "Weird shape candle"')
            items.append("Weird shape candle")
            time.sleep(1)
            break
        elif direction2 == 'no': #not picking up the candle
            direction2 = direction2.lower()
            print('You walk pass the weird candle')
            items.append("Please let me pass")
            time.sleep(1)
            break
    else: #Not typing accordingly returen to the first one
        print('Please type accordingly to the word')
        time.sleep(1)
        print('You will be returned to the starting line')
    time.sleep(1)
# if items == ['Old map'] or items == ["Weird shape candle"] or items == []:
    
while True:
    print('You encounter another cross road') #encounter new direction
    direction3 = input('Left or Right?\n')
    direction3 = direction3.lower()
    if direction3 == 'left':
        print('You found a dangerous monster')
        time.sleep(1)
        if items == ["Old map"]: #Uses an old map
            print("You run for your life")
            time.sleep(1)
            print("You use an old map to find an exit")
            time.sleep(1)
            print("You finally got out of a maze\nCongrats")
            break
        elif items == ["Weird shape candle"]:
            print('The monster is advancing toward you with malicious intent')
            time.sleep(2)
            print('You are too scared to move')
            time.sleep(1)
            print('Suddenly, the candle that you picked up shines a bright purple light')
            time.sleep(2)
            print('You woke up from a dream\nCongrats')
            break
        else: 
            print('The monster is attacking you')
            time.sleep(1)
            print('Without any items in your pocket\nYou die in peace')
            time.sleep(1)
            print('Noob')
            break
    elif direction3 == 'right':
        direction3 = direction3.lower()
        print('You found a dead end')
        time.sleep(1)
        if items == ["Old map"]:
            print('You notice there is a hidden passage written on the old map you picked up')
            time.sleep(2)
            print('You follow the path')
            time.sleep(1)
            print('You got to an exit')
            time.sleep(1)
            print('Congrats')
            break
        elif items == ["Weird shape candle"]:
            print('???')
            time.sleep(1)
            print('The candle is shining very bright purple light')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('You are out of a maze')
            time.sleep(1)
            print('However, you are in the middle of desert')
            time.sleep(1)
            print('Congrats?')
            break
        else: 
            print('You heard a monster roar from behind')
            time.sleep(1)
            print('You turn back and everything turn to black')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('You die')
            break
    else: 
        print('Please type accordingly')
        time.sleep(1)
        print('You will be returned the previous choice')
        time.sleep(1)
print('The end')
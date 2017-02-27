#!/usr/bin/env python

print('hello are you redye')
print('you are lost in a forist and you see a casule inside is a monster with red eyes and green hair')
print('')
answer = input('do you want to run or attack?')

if answer == 'run':
    print('the monster sends his invisable minyon to find out whare you are going he jumps out infront of you')
    answer = input('do you want to fight or keep runing')
    if answer == 'fight':
        print('you difeat him and go home')
    elif answer == 'keep runing':
        print('he captures you and puts you in prision with the princess GAME OVER!!!')   
elif answer == 'attack':
    print('you draw your sword and walk forwerd into the casule you difeat the monster and save the princess')
else:
    print('the monster sends his invisable minyon to spy on you as you plan your next move')
    print('just then you hear a noise behind you you spin around quickley and see a girl with long silver hair and blue eyes')
    print('she says: my sister got capcherd by the evil monster with green hair will you help me find her?')
    print('')
    answer = input('do you want to help her or go home')
    if answer == 'help her':
        print('she smiles and together you diside that you will go inside and difeat the monster and she will get her sister')
        print('you split up and sneek into the catsle but the monster is waiting for you becuse the minyon wornd him')
        answer = input('do you want to fight him or run')

        if answer == 'fight him':
            print('you difeat the monster and help save the princess')

        elif answer == 'run':
            print('the invisable minyon shuts the door the monster captues you and the gril and put you in the dungin with the princess GAME OVER!!!')
    elif answer == 'go home':
        print('you get catured by the monster and put in the dungin with the princess GAME OVER!!!')

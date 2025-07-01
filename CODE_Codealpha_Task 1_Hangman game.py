# SHWETA SUNILKUMAR_CODE_Codealpha_Task 1_Hangman

import random
l = []
newl = []
no_words = 0
chance = 0
s = {1: {'Passion Fruit': 'Its tart and juicy pulp adds zing to drinks and desserts.'},
     2: {'Wood Apple': 'Despite their rock-hard shell, the inside of a wood apple is packed with fluffy, \nedible pulp that tastes tart and tangy, kind of like a mix of apple and lemonade!'},
     3: {'Coconut': 'Coconuts are technically not nuts! They are a type of fruit called a drupe, \nwhich is like a cherry or a peach.  This means they have a hard outer shell with a seed inside, \nsurrounded by a fleshy part that we enjoy.'},
     4: {'Mangosteen': 'Nicknamed the "Queen of Fruits", the Mangosteen is prized for \nits delicious flesh and thick, knobby rind.'},
     5: {'Pineapple': 'Sweet and tropical, pineapples are perfect for summer treats.'},
     }

print('WELCOME TO THE "FRUITS" HANGMAN')
print('Guess each letter of the mystery fruit. You only have 7 chances to go wrong.')
a = random.randrange(1, 6)
name = s[a]
for z in name:
    for i in z.lower():
        l.append(i)
b = len(l)
for s in range(b):
    newl.append('_')

print(newl)
print('Your word has ', b, 'letters.')
while chance < 7:
    inp = input('Enter letter: ')
    if inp in l:
        print('Yes!')
        chance += 0
        word = z.lower()
        for i, char in enumerate(word):
            if char == inp:
                newl[i] = inp
        print(newl)
    elif inp == z.lower():
        break
    elif newl==l:
        break

    else:
        print('No, sorry!')
        chance += 1

print('The word is', z, '!')
print(name[z])

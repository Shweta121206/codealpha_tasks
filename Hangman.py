import random
l = []
newl = []
no_words = 0
chance = 0
s = {1: {'Passion Fruit': 'Its tart and juicy pulp adds zing to drinks and desserts.'},
     2: {'Wood Apple': 'Despite their rock-hard shell, the inside of a wood apple is packed with fluffy, edible pulp that tastes tart and tangy, kind of like a mix of apple and lemonade!'},
     3: {'Coconut': 'Coconuts are technically not nuts! They are a type of fruit called a drupe, which is like a cherry or a peach.  This means they have a hard outer shell with a seed inside, surrounded by a fleshy part that we enjoy.'},
     4: {'Mangosteen': 'Nicknamed the "Queen of Fruits", the Mangosteen is prized for its delicious flesh and thick, knobby rind.'},
     5: {'Pineapple': 'Sweet and tropical, pineapples are perfect for summer treats.'},
     6: {'Grapes': 'Whether red, green, or purple, grapes are a delightful snack and can be turned into wine too!'},
     7: {'Sunmelon': 'Sun melons, also called Sarda melons, are champions of hydration! This high water content also makes them low in calories.'},
     8: {'Rambutan': 'The fruit’s name originates from the Malaysian word “rambit,” meaning hairy.'},
     9: {'Star Fruit': 'The Star fruit magically transforms from a regular fruit into a perfect star shape when you slice it!'},
     10: {'Gooseberry': 'The Nelli is a sour fruit high in vitamin C, used in South India for its culinary and traditional wellness purposes.'},
     11: {'Dragon Fruit': 'Also known as "Pitaya", dragon fruit has vibrant pink or yellow skin and has a mild, sweet flavor.'},
     12: {'Jamun': 'The Jamun fruit, with its astringent taste, is said to be helpful in managing blood sugar levels in some people.'},
     13: {'Karonda': 'The Karonda fruit is enjoyed in South India for its tangy flavor in pickles, jams, and drinks.'},
     14: {'Nungu': 'Nungu fruit, popular in South India, is enjoyed for its refreshing taste, hydration and potential health benefits.'},
     15: {"Travelers Palm": "The traveler's palm fruit has a fuzzy blue covering that can be eaten, but the fruit itself is not commonly consumed."},
     16: {'Lemon': "The scientific name of lemon is Citrus × limon, a hybrid of citron and sour orange."}}

print('WELCOME TO THE "FRUITS" HANGMAN')
print('Guess each letter of the mystery fruit. You only have 7 chances to go wrong.')
a = random.randrange(1, 15)
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
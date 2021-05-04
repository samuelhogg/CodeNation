""" 
def first_thing(num1, num2):
    print(num1 * num2)

first_thing(3,5)
first_thing(4,8)
first_thing(5,13)
 """
######################################################################
""" 
from random import randint

little_coffer_order = ["Mocha", "Cappuccino", "Latte"]

coffee_order = [
    "Mike G - Hot Chocolate",
    "Pesh - Latte",
    "Syed - Cappuccino",
    "Toby - Yorkshire Tea",
    "Keira - Caramel Frapuccino",
    "Amir - Mocha",
    "Mike D -  Solo Espresso",
    "Monir - Floata Coffee",
    "Sam - Builders Tea",
    "Andy - Black Tea",
    "Pedro - Mocha Latte",
    "Chris - Triple Shot Americano",
    "Abdul - Oat Milk Flat White",
    "Geoff - Red Tea",
    "Will - Black Coffee",
]

x = randint(0, len(coffee_order)-1)
print(coffee_order[x])
"""
######################################################################
""" 
fav_songs = ["Pharrell williams - frontin", "AC/DC - Thunderstruck", "Simply Red - if you don't know me by now",]

fav_songs[1] = "George Michael - FastLove" # Replace an item in the list
print(fav_songs)

fav_songs.append("Take That - Never Forget") # Add item to end of list
print(fav_songs)

fav_songs.insert(0, "Queen - Fat Bottomed Girls") # Insert to desired location
print(fav_songs)

fav_songs.pop() # Removes last item
print(fav_songs)

fav_songs.pop(1) # Removes specific item in list
print(fav_songs)

fav_songs.reverse() # Reverse the list
print(fav_songs)
"""
######################################################################
#Activity1
""" 
fav_ws = ["TryHackMe - www.tryhackme.com", "HackTheBox - www.hackthebox.eu", "Liverpool FC - www.liverpoolfc.com",]
fav_ws.append("Github - Github.com")
fav_ws.append("LinkedIn - LinkedIn.com")
fav_ws.pop()
print(fav_ws)

fav_ws = ["TryHackMe - www.tryhackme.com", "HackTheBox - www.hackthebox.eu", "Liverpool FC - www.liverpoolfc.com",]
fav_ws.extend(["Github - Github.com", "LinkedIn - LinkedIn.com"])
fav_ws.pop()
print(fav_ws)
 """
######################################################################
#Activity2
""" Research on the following methods: remove(), reverse(), sort(), count(), extend() (and many more). Create a
program to demonstrate the uses of each method, some of these you may need more than one example.
(Pay attention: not all methods would permanently updates/make changes to the lists themselves.) 

fav_ws = ["TryHackMe - www.tryhackme.com", "HackTheBox - www.hackthebox.eu", "Liverpool FC - www.liverpoolfc.com",]
fav_ws.extend(["Github - Github.com", "LinkedIn - LinkedIn.com"])
print(fav_ws)

fav_ws.pop() # Removes last item
fav_ws.reverse() # Reverses list
print(fav_ws)

fav_ws.sort() # Case insensitive Sort
print(fav_ws)

fav_ws.remove("Github - Github.com") # Remove specific item
print(fav_ws)

print("There is only " + str(fav_ws.count("Liverpool FC - www.liverpoolfc.com")) + " Liverpool FC!")
"""
######################################################################
#For Loops
""" 
favourite_drinks = ["coke", "fanta", "tonic"]

for drink in favourite_drinks:
    print(drink)

for i in range(10):
    print(i)

i = 1
for order in favourite_drinks:
    print(i, "", order)
    i += 1
"""
######################################################################
#For Loops Activity 1
""" 
fav_films = ["Die Hard", "A Good Year", "Ghostbusters", "Croods"]

def filmcheck():
    for films in fav_films:
        print (films)
    if fav_films[2] == "Ghostbusters":
        print("yey it’s ghostbusters")
    else:
        print("booo, we want ghostbusters")

filmcheck()
 """
######################################################################
#For Loops Activity 2
""" 
for i in range(9, -1, -1):
    print(i)
 """
######################################################################
#While Loops
""" 
num = 0

while num < 10:
    num += 1
    print(num)
"""
######################################################################
""" 
import random

rand_num = random.randint(0,50)

my_num = 50

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,50)

print("You've found {}!".format(my_num))
 """
######################################################################
#Attempt at random generator with no duplicates
""" 
import random

r=0
my_num = 50
list=[]

while r != my_num:
    print(r)
    r=random.randint(1,50)
    if r not in list: list.append(r)

print("You've found {}!".format(r))
list.sort()
print(list)
 """
######################################################################
#Activity 1
""" 
for i in range(13):
    print("hello world")

i=0 
while i < 13:
    print("hello world")
    i += 1
"""

#Activity 2
""" 
import random
r=0

for i in range(6):
    r=random.randint(1,30)
    if r % 7 == 0:
        print("Number", r, "is divisible by 7")
    else:
        print("Number", r, "is not divisble by 7")
"""

#Activity 3 My attempt
""" 
import random

current_card = ""
cards = ["Diamond", "Spade", "Club", "Heart"]
pick_card = random.choice(cards)

print("My card is", pick_card)

while pick_card != current_card:
    current_card = random.choice(cards)
    print(current_card)
 """
######################################################################

def multi(*args):
    c = 1
    for i in args:
        c *= i
    return c

print(multi(10,11,12,15))
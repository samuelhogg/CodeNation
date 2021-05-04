# my_name = "Samuel"
# my_age = 46
# lfc = "Red"

# print(f"My name is {my_name} and I am {my_age-10} years old, and the colour of Liverpool is {lfc}")

######################################################################################################

# breakfast = "Weetabix"
# lunch = "Sandwich"
# dinner = "Spaghetti Bolognese"

# print(f"My breakfast today will be {breakfast}, lunch will be a {lunch}, and dinner will be {dinner}")

# breakfast = "Porridge"
# lunch = "Soup"
# dinner = "KFC"

# print(f"My breakfast tomorrow will be {breakfast}, lunch will be a {lunch}, and dinner will be {dinner}")



# breakfast = "Porridge"
# breakfast = breakfast.replace("Porridge","Toast")
# print(breakfast)

######################################################################################################

class bcolors:
    OK = '\033[92m' #GREEN
    RESET = '\033[0m' #RESET COLOR

space1 = "X"
space2 = "O"
space3 = "O"
space4 = "X"
space5 = "X"
space6 = "O"
space7 = "X"
space8 = "O"
space9 = "X"

print(f"{bcolors.OK}    |   | \n  {space1} | {space2} | \n    |   | \n-------------\n    |   | \n  {space5} | {space4} | \n    |   | \n-------------\n    |   | \n  {space8} |   | \n    |   | {bcolors.RESET}")

######################################################################################################

import datetime 

today = datetime.date.today()
birthday = datetime.date(2021, 9, 28)
diff = birthday - today

print(f"Number of days from today to my birthday is {diff}")

######################################################################################################

age = 17
country = "UK"

if age > 17 and country == "UK":
    print("Yes I can serve you")
else:
    print("You aren't old enough and you not in the UK")

######################################################################################################

num = 14

if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")

######################################################################################################

num = 21

if num % 3 == 0 and num % 7 == 0:
    print("fizz buzz")
elif num % 3 == 0:
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(num)

######################################################################################################

word = "abba"

if word[0] == word[-1]:
    print("true")
else:
    print("false")

######################################################################################################
#challenge5

time = 7
place_of_work = "Liverpool"
town_of_home = "Chester"

if time == 7:
    print("I'm at home")
elif time == 8:
    print("I'm commuting")
elif time == 9:
    print("I'm at work")
else:
    print("I don't really know")

######################################################################################################
#challenge6

num1 = 8
num2 = 8

if num1 + num2 % 2 == 0:
    print("The sum of these two numbers is even")
else:
    print("The sum of these two numbers are not even")

######################################################################################################
#challenge7
# num = input('Enter any number : ')

# val = int(num)
# if num == str(num)[::-1]:
#     print('The given number is PALINDROME')
# else:
#     print('The given number is NOT a palindrome')

######################################################################################################
#challenge8 (Find the index of a last vowel in the string)

word = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"
vowels = ['a','e','i','o','u']
ind = -1

if word[ind] in vowels:
    print(ind)

# for index,item in enumerate(word):
#    if item in vowels:
#        print(index)
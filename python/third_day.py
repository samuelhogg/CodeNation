"""
name = input("What is your name?")

if name:
    print("Hello {}, How are you?".format(name))
else:
    print("You did not give me your name!") 
"""

######################################################################
""" 
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
 """
######################################################################

""" 
space1 = "X"
space2 = "O"
space3 = "O"
space4 = "X"
space5 = "X"
space6 = "O"
space7 = "X"
space8 = "O"
space9 = "X"

print("      |   |   ")
print("      |   |   ")
print("      |   |   ")
print("-----------------")
print("      |   |   ")
print("      |   |   ")
print("      |   |   ")
print("-----------------")
print("      |   |   ")
print("      |   |   ")
print("      |   |   ") 
"""

######################################################################
""" if row wins or loses

x1 = 'X'
x2 = 'X'
x3 = 'X'

items = [x1,x2,x3]

def all_same(items):
    return all(x == items[0] for x in items)

print(all_same(items))
"""
######################################################################
"""functions

def press_grind_beans():
    print("Grinding for 20 seconds")

press_grind_beans()
"""
######################################################################
""" 
coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding
    if coffee_is_grinding:
        print("Stopping the grind")
        coffee_is_grinding = False
    else:
        print("Grinding is about to begin")
        coffee_is_grinding = True

press_grind_beans()
press_grind_beans()
"""
######################################################################
""" 
coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding
    if coffee_is_grinding == True:
        print("Stopping the grind")
        coffee_is_grinding = False
    else:
        print("Grinding is about to begin")
        coffee_is_grinding = True

press_grind_beans()
press_grind_beans()
"""
######################################################################
""" 
def cash_withdrawal(amount, accnum):
    print("Withdrawing {} from account {}".format(amount, accnum))

cash_withdrawal(300, 50449921)
cash_withdrawal(30, 50449921)
cash_withdrawal(200, 50447921) 
"""
######################################################################
""" 
def order(size, type):
    print("I would like a {} {} please".format(size, type))

order("large", "Lungo")
order("medium", "Expresso")

"""
######################################################################
""" 
def add_up(num1, num2):
    return num1 + num2
    
add_up(7,3)
print(add_up(2,5))
 """
######################################################################
""" 
def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)

def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32

print("The temperature is {}°F".format(get_fahrenheit(15)))
#Output: The temperature is 59°F
 """
######################################################################
""" 
order_count = 0

def take_order(size, base, topping):
    global order_count
    print("I would like a {} Pizza with {} base, and {} topping".format(size, base, topping))
    order_count += 1
    print("This is order {}".format(order_count))

take_order("large", "classic", "pepperoni")
take_order("medium", "italian", "ham")
 """
######################################################################
#Failed Attempt
""" 
pin = 1234
balance = 555

def withdrawal(amountent):
    global balance
    pinent = input('Please input your pin : ')
    amountent = input('Please enter how much you would like to withdrawal : ')
    print("You have withdrawm {} and your new balance is {}")

pinent = input('Please input your pin : ')

if pinent == pin:
    print("pin is correct")
else:

#     withdrawal(amountent)
# else:
#     print("pin is incorrect, please try again")  
"""
######################################################################
""" 
pin = 1234
balance = 1000
account_number = 12345678
def print_dispencing_cash(pin_number, amount):
    global pin
    global balance
    global acc_entered
    if account_number == acc_entered:
        if pin_number == pin and amount <= balance:
            balance -= amount
            print(f"Pin correct, now dispencing £{amount}. Your remaining balance is balance £{balance}.")
        elif pin == pin_number and amount > balance:
            print(f"Not enough moneeehhhhhhh. Available is {balance}")
        elif pin != pin_number:
            print("Pin incorrect. You have three more tries. Let's roll those dice.")
    else:
        print("Check the ACC number!")
        start_atm()
def start_atm():
    global acc_entered
    acc_entered = int(input("What is the 8 digit account number?"))
    pin_number = int(input("What's your fackin PIN!"))
    amount_num = int(input("How much wonga?"))
    print_dispencing_cash(pin_number, amount_num)
start_atm()
"""
######################################################################


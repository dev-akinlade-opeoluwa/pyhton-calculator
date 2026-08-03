"""
Calculator

A simple command-line calculator written in Python.

Features:
- Addition
- Subtraction
- Multiplication
- Division
- Powers
- Calculation History
- Input Validation
- Clear History

Made by Opeoluwa Akinlade
"""

# Functions
def calculation(option, first_num, second_num, history):
# Addition*******
    if option==1:
        print("=" * 30)
        print("ADDITION".center(30))
        result=first_num+second_num
        display=f"{first_num} + {second_num} = {result:.2f}"
        print(display.center(30))
        print("=" * 30)
        history.append(display)
# Subtraction******        
    elif option==2:
        print("=" * 30)
        print("SUBTRACTION".center(30))
        result=first_num-second_num
        display=f"{first_num} - {second_num} = {result:.2f}"
        print(display.center(30))
        print("=" * 30)
        history.append(display)
 # Multiplication*****       
    elif option==3:
        print("=" * 30)
        print("MULTIPLICATION".center(30))
        result=first_num*second_num
        display=f"{first_num} x {second_num} = {result:.2f}"
        print(display.center(30))
        print("=" * 30)
        history.append(display)
# Division*******
    elif option==4:
        print("=" * 30)
        print("DIVISION".center(30))
        if second_num==0:
            print("Error: Cannot divide by zero.".center(30))
            print("=" * 30)
            history.append(f"{first_num} / {second_num} is Undefined")
            return
        result=first_num/second_num
        display=f"{first_num} / {second_num} = {result:.2f}"
        print(display.center(30))
        print("=" * 30)
        history.append(display)
#Power*********
    elif option==5:
        print("=" * 30)
        print("POWER".center(30))
        result=first_num**second_num
        display=f"{first_num} ^ {second_num} = {result:.2f}"
        print(display.center(30))
        print("=" * 30)
        history.append(display)

# Number input        
def num_check():
    # First Number
    while True:
        try:
            first_num=float(input("Type in the first number: "))
            break
        except ValueError:
            print("Please type in a valid number.")
            print()
            continue
      # Second Number      
    while True:
        try:
            second_num=float(input("Type in the second number: "))
            break
        except ValueError:
            print("Please type in a valid number.")
            print()
            continue
    return first_num, second_num


# Clear History
def clear_history(history):
    while True:
        ans=input("Are you sure you want to clear history? (y/n) ").strip().lower()
        if ans=="y":
            history.clear()
            print("History cleared!\n")
            break
        elif ans=="n":
            break
        
        else:
            print("Please pick between y or n\n")
            continue

# Pause       
def pause ():
    while True:
        if input("Press Enter to continue...") == "":
            break
        print("Just press Enter.")
        
# ==========================
# Main Program
# ==========================



history=[]
# Display Menu
print("=" * 30)
print("CALCULATOR".center(30))
print("=" * 30)
while True:
    print("=" * 30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. View History")
    print("7. Clear History")
    print("8. Exit")
    print("=" * 30)
    try:
        option=int(input("Choose an option from 1 to 8: "))
    except ValueError:
        print("Please type in a valid number")
        continue
# View History
    if option==6:
        print("=" * 30)
        print("HISTORY".center(30))
        if not history:
            print("History is empty")
            print()
            pause()
            continue
        for item in history:
            print(item.center(30))    
        print()
        pause()
        continue
    
# Clear History    
    if option==7:
        if not history:
            print("History is empty.\n")
            continue
        clear_history(history)
        pause()
        continue
# Exit        
    if option==8:
        break
    if option not in (1,2,3,4,5,6,7,8):
        print("Please choose a number from 1 to 8")
        print()
        continue
# Called Functions    
    first_num, second_num=num_check()
    calculation(option, first_num, second_num, history)
    pause()
# Goodbye Message
print("=" * 30)
print("Thanks for using my calculator!")
print("Goodbye!")
print("=" * 30)
    
    

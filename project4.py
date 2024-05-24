# CMSC 254
#Project 4 
# Amra Ibrahim

import datetime

def happy():
    # Returns this line from The Birthday song
    return 'Happy Birthday to YoU!\n'

def getDay():
    # Returns the day of today's date
    return datetime.datetime.now().day

def getMonth():
    # Returns the month of today's date
    return datetime.datetime.now().month

def getYear():
    # Returns the year of today's date
    return datetime.datetime.now().year

# Write your code for the sing function
def sing(person):
    return "\n".join(["Happy Birthday to YOU!"] * 2 + [f"Happy Birthday, dear {person}!", "Happy Birthday to YOU!"])

# Write your code for the isToday function
def isToday(day, month):
    return day == getDay() and month == getMonth()

# Write your code for the birthdayGreeting function
def birthdayGreeting(name, day, month):
    if isToday(day, month):
        return sing(name)
    else:
        return f"Have a nice day, {name}!"

if __name__ == "__main":
    # Display Happy Birthday to Rodney
    print(sing("Rodney"))

    # Display False
    print(str(isToday(3, 10)))

    # Display Have a nice day, Lisa
    print(birthdayGreeting("Lisa", 25, 10))

    


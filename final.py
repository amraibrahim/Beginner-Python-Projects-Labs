#Amra Ibrahim
import random

def calculate_tip(charge, tip_percent):
    # add your code here and update the return statement
    #if either the charge or tip amount is below zero, display an error message
    if charge < 0:
        return "Invalid charge amount"
    elif tip_percent < 0:
        return "Invalid tip percent"
    #bind the tip percentage variable to tip_percent
    tippercent = tip_percent/100
    #calculate the tip 
    tip = charge*tippercent
    return tip

def classify_student(credits):
    # add your code here and update the return statement
    #if the value of credits fall in a specific range,
    if credits in range(1,24):
        return "Freshman"
    elif 23 <= credits <= 54:
        return "Sophomore"
    elif credits in range(54, 84):
        return "Junior"
    elif 85 <= credits:
        return "Senior"
    #it will return a different string depending on where the value of credit falls
    #if credit is 0, it will display an error message.
    elif credits == 0:
        return "Insufficient credits for classification"


def encode_message(inString):
    outString = ''
    # add your code here
    #create the list of letters, and a variable that stores a randomly chosen letter
    randomletter=['r','s','t']
    chosenletter=random.choice(randomletter)
    #iterate through each letter in the string, every vowel has a random letter plus itself added after it. Then add it to the output string.
    for char in inString:
        if char == 'a':
            x=inString.find('a')
            outString+=inString[x]+chosenletter+'a'
        elif char == 'e':
            x=inString.find('e')
            outString+=inString[x]+chosenletter+'e'
        elif char == 'i':
            x=inString.find('i')
            outString+=inString[x]+chosenletter+'i'
        elif char == 'o':
            x=inString.find('o')
            outString+=inString[x]+chosenletter+'o'
        elif char == 'u':
            x=inString.find('u')
            outString+=inString[x]+chosenletter+'u'
    #if letter isn't a vowel, add it to the output string. 
        else:
            outString+=char
    return outString
def decode_message(message):
    outString = ''
    # add your code here
    #tracking the index of the string
    x=0
    length=len(message)
    #creating the list of vowels
    vowel=['a','e','i','o','u']
    #while the index is greater than the length of the string,
    #add each letter to outString
    while x < length:
        outString+=message[x]
        #if the value attached to the index is a vowel,
        #skips the next two letters and counts the letter beside them
        if message[x] in vowel:
            x = x+3
        #if it's not a vowel, it will move to the next letter. 
        else:
            x = x+1
    return (outString)


if __name__ == "__main__":
    print('Tests for calculate_tip function: ')
    # Displays the 20% tip on a bill of 27.5 --> 5.5
    print(calculate_tip(27.5, 20))

    # Displays Invalid charge amount for a bill of negative dollars
    print(calculate_tip(-1.0, 15))

    # Displays Invalid tip percent for a -1% tip
    print(calculate_tip(27.5, -1))
    print()

    print('Tests for classify_student function: ')
    # Displays Freshman
    print(classify_student(20))

    # Displays Senior
    print(classify_student(120))

    # Displays Insufficient credits for classification
    print(classify_student(0))
    print()

    print('Tests for encode_message function: ')
    # Displays something like Heselloro Wosorld
    print(encode_message("Hello World"))

    # Displays something like Ditinneser totoniright asat Tararasa Thasaiti.
    print(encode_message("Dinner tonight at Tara Thai."))

    # Displays something like Mereeret atat setevesen oroclotock.
    print(encode_message("Meet at seven oclock."))
    print()

    print('Tests for decode_message function: ')
    # Displays Hello World
    print(decode_message("Herelloto Wororld"))

    # DisplaysDinner tonight at Tara Thai.
    print(decode_message("Disinneter tosonisight asat Tararata Thasairi."))

    # Displays Meet at seven oclock.
    print(decode_message("Meteeset asat seseveten otoclosock.."))
    print()

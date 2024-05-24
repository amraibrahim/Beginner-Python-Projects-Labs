# CMSC 254 Project 5
# Amra Ibrahim
# Write your code for these functions
def has_illegal_letters (word, letters):
    for x in range(len(word)):
        for y in range (len(letters)):
            if word[x] == letters [y]:
                return True
    return False

def has_only_legal_letters(word, letters):
    word = word.replace(" ", "")
    word= word. lower ()
    letters = letters. lower ()
    for x in word:
        if not x in letters:
            return False
    return True

def uses_all_letters (word, letters):
    word = word. lower ()
    letters = letters.lower()
    for x in letters:
        if x not in word:
            return False
        return True

def is_in_abc_order (word):
    word = word. lower ( )
    for x in range(len (word) -1):
        if word[x] > word [x+1]:
            return False
    return True
if __name__ == "__main__":
    print(has_illegal_letters("hello world", "ео"))  # True
    print(has_illegal_letters("hello world", "abc"))  # False
    print(has_only_legal_letters("Hoe alfalfa", "acefhlo"))  # True
    print(has_only_legal_letters("Have alfalfa", "acefhlo"))  # False
    print(uses_all_letters("Hoe alfalfa", "aefhlo"))  # True
    print(uses_all_letters("Hoe alfalfa", "acefhlo"))  # False
    print(is_in_abc_order("glossy"))  # True
    print(is_in_abc_order("matte"))  # False

def count_up(num):
    result_string = ' '.join(map(str, range(num + 1)))
    return result_string

def sum_up(value):
    total = sum(range(value + 1))
    return total

def get_vowels(word):
    result_string = ''.join(char for char in word if char in "aeiouy")
    return result_string

if __name__ == "__main__":
    # Do not delete or alter this code; run it to test your functions
    # call count_up function with input of 7
    # expected display is "0 1 2 3 4 5 6 7"
    print(count_up(7))
    # call sum_up function with input of 7
    # expected display is the number 28
    sum_result = sum_up(7)
    print(str(sum_result))
    # expected display is "ia"
    print(get_vowels("lisa"))
    # expected display is "aaa"
    print(get_vowels("banana"))

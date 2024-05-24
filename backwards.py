def backwardsNumberTrick(ending_number):
    return (ending_number - 3) // 2

def transform1(numbers):
    return [num + 1 for num in numbers]

def transform2(numbers):
    return [num // 3 for num in numbers]

if __name__ == "__main__":
    numbers1 = [0, 15, 27]
    transformed1 = transform1(numbers1)
    print("Transformed 1:", transformed1)

    numbers2 = [87, 1026, 72]
    transformed2 = transform2(numbers2)
    print("Transformed 2:", transformed2)
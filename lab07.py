import math

def wordCount(someStr):
    # Split the input string by spaces and count the number of words
    words = someStr.split()
    return len(words)

def calculateVolume(radius, height):
    if 1 <= radius <= 100 and 1 <= height <= 100:
        # Calculate the volume of the right circular cone
        volume = (math.pi * radius**2 * height) / 3
        return round(volume, 3)  # Round the result to three decimal places
    else:
        return "Invalid input. Both radius and height should be between 1 and 100."

# Sample usages:
if __name__ == '__main__':
    sample_str_1 = 'hello'
    sample_str_2 = 'a bunch of words'
    sample_str_3 = 'twas brillig and the slithy toves'
    print(f'Word Count for "{sample_str_1}": {wordCount(sample_str_1)}')
    print(f'Word Count for "{sample_str_2}": {wordCount(sample_str_2)}')
    print(f'Word Count for "{sample_str_3}": {wordCount(sample_str_3)}')

    sample_radius_1 = 4
    sample_height_1 = 6
    sample_radius_2 = 9
    sample_height_2 = 12
    print(f'Volume for radius {sample_radius_1} and height {sample_height_1}: {calculateVolume(sample_radius_1, sample_height_1)}')
    print(f'Volume for radius {sample_radius_2} and height {sample_height_2}: {calculateVolume(sample_radius_2, sample_height_2)}')

def countLines(fileName):
    try:
        with open(fileName, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()

            # Count lines with alphanumeric characters
            count = sum(1 for line in lines if any(c.isalnum() for c in line))
            return count
    except FileNotFoundError:
        return f"File cannot be opened: {fileName}"

def getLongestLine(fileName):
    try:
        with open(fileName, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()

            # Find the longest line with alphanumeric characters
            longest_line = max((line.strip() for line in lines if any(c.isalnum() for c in line)), key=len, default="")
            return longest_line
    except FileNotFoundError:
        return f"File cannot be opened: {fileName}"

if __name__ == "__main__":
    # displays the number of lines of text in "jabberwocky.txt" -> 29
    print(countLines("jabberwocky.txt"))

    # returns an error message, File cannot be opened: jabberwock.txt
    print(countLines("jabberwock.txt"))

    # displays the longest line in the text, "jabberwocky.txt"
    print(getLongestLine("jabberwocky.txt"))

    # returns an error message, File cannot be opened: jabberwock.txt
    print(getLongestLine("jabberwock.txt"))

import sys

if len(sys.argv) != 2:
    print("Usage: python project2.py <N> ")
    sys.exit(1)

N = int(sys.argv[1])

if N < 1 or N > 5:
    print("N must be a whole number between 1 and 5.")
    sys.exit(1)

base_sentence = "A long time ago in a galaxy"

result_sentence = base_sentence + " far" * N + " away..."

print(result_sentence)

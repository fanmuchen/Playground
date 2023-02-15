# Define the 4x4 grid of letters
letters = [
    ['S', 'S', 'E', 'R'],
    ['U', 'H', 'O', 'T'],
    ['I', 'E', 'N', 'L'],
    ['R', 'B', 'T', 'H']
]

# Ask the user to enter the letters as a string
# letters_str = input("Enter the 16 letters as a single string: ").upper()

# Convert the string to a 4x4 grid of letters
# letters = [[letters_str[i*4 + j] for j in range(4)] for i in range(4)]

# Read the English dictionary file into a set
dictionary = set()
with open('files/Collins Scrabble Words (2019).txt', 'r') as f:
    for line in f:
        dictionary.add(line.strip().upper())

# Define a list of words to search for
# words = ['ABC', 'DEF', 'GHI', 'MNO', 'ADG',
#          'BEH', 'CFI', 'MGL', 'NHL', 'KJ', 'MJGKFA']
words = dictionary

# Define a function to check if a word can be formed in the grid


def is_word_possible(word, grid):
    # Check all starting positions for the first letter of the word
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if word[0] == grid[i][j]:
                # Check all possible paths from the starting position
                if is_word_possible_helper(word[1:], grid, [(i, j)]):
                    return True
    return False

# Define a helper function to check if a word can be formed in the grid from a given position


def is_word_possible_helper(word, grid, path):
    if len(word) == 0:
        return True
    # Get the current position from the path
    i, j = path[-1]
    # Check all adjacent positions for the next letter of the word
    for di in range(-1, 2):
        for dj in range(-1, 2):
            # Ignore the current position and out-of-bounds positions
            if (di, dj) != (0, 0) and 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]):
                if word[0] == grid[i+di][j+dj] and (i+di, j+dj) not in path:
                    # Recursively check the next letter of the word
                    if is_word_possible_helper(word[1:], grid, path + [(i+di, j+dj)]):
                        return True
    return False


# Define a list to store the found words
found_words = []

# Find all possible words
for word in words:
    if is_word_possible(word, letters):
        found_words.append(word)

# Sort the list of found words by length (from longest to shortest), then alphabetically
found_words.sort(key=lambda x: (-len(x), x))

# Print the list of found words
print(found_words)

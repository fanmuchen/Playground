# Define the 4x4 grid of letters
letters = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

# Define a list of words to search for
words = ['ABC', 'DEF', 'GHI', 'MNO', 'ADG',
         'BEH', 'CFI', 'MGL', 'NHL', 'KJ', "MJGDHLPKFA"]

# Define a function to check if a word can be formed in the grid


def is_word_possible(word, grid):
    # Check if the word can be formed horizontally
    for row in grid:
        if word in ''.join(row):
            return True
    # Check if the word can be formed vertically
    for col in range(len(grid[0])):
        if word in ''.join([row[col] for row in grid]):
            return True
    # Check if the word can be formed diagonally
    for i in range(len(grid)):
        if word in ''.join([grid[i+j][j] for j in range(min(len(grid)-i, len(grid[0])))]):
            return True
        if word in ''.join([grid[j][i+j] for j in range(min(len(grid[0])-i, len(grid)))]):
            return True
        if word in ''.join([grid[i-j][j] for j in range(min(i+1, len(grid[0])))]):
            return True
        if word in ''.join([grid[j][i-j] for j in range(min(len(grid)-i, len(grid[0])))]):
            return True
    return False


# Define a list to store the found words
found_words = []

# Find all possible words
for word in words:
    if is_word_possible(word, letters):
        found_words.append(word)

# Sort the list of found words by length (from longest to shortest)
found_words.sort(key=len, reverse=True)

# Print the list of found words
print(found_words)

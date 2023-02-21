# 这个程序采用了一种方法，用字典里的单词一个个去试，看是否能在网格里跑通。这样似乎并不是最高效的。
# Note that this implementation assumes that your terminal supports ANSI escape sequences for text coloring. If your terminal does not support text coloring, the colored step numbers may not be visible or may appear as regular text.

# Read the English dictionary file into a set
dictionary = set()
with open('./files/Collins Scrabble Words (2019).txt', 'r') as f:
    for line in f:
        dictionary.add(line.strip().upper())

# Define the 4x4 grid of letters
# 测试用
# letters = [
#     ['S', 'S', 'E', 'R'],
#     ['U', 'H', 'O', 'T'],
#     ['I', 'E', 'N', 'L'],
#     ['R', 'B', 'T', 'H']
# ]

if not "letters" in locals() or not letters:
    # Ask the user to enter the letters as a string
    letters_str = input("Enter the 16 letters as a single string: ").upper()

    # Convert the string to a 4x4 grid of letters
    letters = [[letters_str[i*4 + j] for j in range(4)] for i in range(4)]

# Read the English dictionary file into a set
dictionary = set()
with open('./files/Collins Scrabble Words (2019).txt', 'r') as f:
    for line in f:
        dictionary.add(line.strip().upper())

# Define a list of words to search for
# words = ['ABC', 'DEF', 'GHI', 'MNO', 'ADG',
#          'BEH', 'CFI', 'MGL', 'NHL', 'KJ', 'MJGKFA']
words = dictionary

# Define a function to check if a word can be formed in the grid


def is_word_possible(word, grid, paths):
    # Check all starting positions for the first letter of the word
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if word[0] == grid[i][j]:
                # Check all possible paths from the starting position
                if is_word_possible_helper(word[1:], grid, [(i, j)], paths):
                    return True
    return False

# Define a helper function to check if a word can be formed in the grid from a given position


def is_word_possible_helper(word, grid, path, paths):
    if len(word) == 0:
        if len(path) >= 5:
            paths.append(path)
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
                    if is_word_possible_helper(word[1:], grid, path + [(i+di, j+dj)], paths):
                        return True
    return False


# Define a list to store the found words
found_words = []
long_paths = []

# Find all possible words
for word in words:
    if is_word_possible(word, letters, long_paths):
        found_words.append(word)

# Sort the list of found words by length (from longest to shortest), then alphabetically
found_words.sort(key=lambda x: (-len(x), x))
long_paths.sort(key=len)

# Print the list of found words


def print_path_on_grid(grid, path):
    # Define the rainbow colors as a list of ANSI escape sequences
    rainbow_colors = [
        '\033[91m',  # Red
        '\033[38;5;208m',  # Orange
        '\033[93m',  # Yellow
        '\033[92m',  # Green
        '\033[96m',  # Cyan
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
    ]
    # Create a copy of the grid to modify
    grid_copy = [list(row) for row in grid]
    # Mark the path on the copy of the grid
    for i, j in path:
        # Calculate the step number based on the index of the position in the path
        step_num = str(path.index((i, j)) + 1)
        # Calculate the color index based on the step number
        color_index = (int(step_num) - 1) % len(rainbow_colors)
        # Replace the corresponding character in the copy of the grid with the colored step number
        grid_copy[i][j] = f'{rainbow_colors[color_index]}{step_num}\033[0m'
    # Print the marked grid
    for row in grid_copy:
        print(' '.join(row))

# 一起输出
# def print_paths_on_grid(grid, paths):
#     # Iterate over each path and print it on a separate graph
#     for i, path in enumerate(paths):
#         word = ''.join([grid[i][j] for i, j in path])
#         print(f'{word}:')
#         print_path_on_grid(grid, path)
#         print()

# 分别输出，按Enter输出下一个


def print_paths_on_grid(grid, paths):
    # Sort the paths by length (from longest to shortest)
    paths.sort(key=len, reverse=True)

    # Iterate over each path and print it on a separate graph
    for i, path in enumerate(paths):
        word = ''.join([grid[i][j] for i, j in path])
        print(f'{word}:')
        print_path_on_grid(grid, path)
        print()
        # Wait for user to press enter before printing the next path
        if i < len(paths) - 1:
            input("Press enter to show the next path...")


print_paths_on_grid(letters, long_paths)

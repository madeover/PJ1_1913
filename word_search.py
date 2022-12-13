# CSCI 1913 Fall 2022
# Author: (Your name here)

# QUESTIONS -- DO THESE LAST.
# Assumptions: assume the letter grid has width W and height H
# Further assume the word parameter has length L (for find) and than the max_len parameter is L (for extract)
# Finally, Assume that concatenating a letter to a string takes time O(1)
# List any other assumptions you make.

# For each question below, answer your questions by filling in the provided multi-line strings.
# (yes it's a bit of a hokey way to do this, but it should work well enough and it keeps the answers in 1 file)
# For each question state any extra assumptions you made, and explain your answer.
# An incorrect answer with no explanation will get no partial credit.

# Question 1: What is the worst-case big-O runtime of your get_size function?
Question1 = '''
O(1)
'''

# Question 2: What is the worst-case big-O runtime of your copy_word_grid function?
Question2 = '''
O(N^2)
'''

# Question 3: What is the worst-case big-O runtime of your extract function?
Question3 = '''
O(N)
'''

# Question 4: What is the worst-case big-O runtime of your find function?
Question4 = '''
O(N^4)
'''

### LEAVE THESE LINES ALONE BEGIN:
# So the code I provide at the bottom needs these lines of code.
import random

# This code defines valid directions a word can travel.
# Each direction is a tuple (dx, dy) that says how you change x and y 
# coordinates to go in a given direction.
RIGHT=(1, 0)       # to go right add 1 to x
DOWN=(0,1)         # to go down add 1 to y
RIGHT_DOWN=(1, 1)  # to go right_down add 1 to both x and y
RIGHT_UP=(1,-1)    # to go right_up add 1 to x and subtract 1 from y
DIRECTIONS = (RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP)
# Good use of these direction-tuples makes for much easier programs for this project. assignment.

### LEAVE THESE LINES ALONE END:
def get_size(word_grid):
    # Returns the Width and Height of the 2d array in the order of a tuple
    return (len(word_grid[0]), len(word_grid))    
    
def print_word_grid(word_grid):
    # Prints the grid in a format that the user is famaliar with as for the word grid
    for i in (word_grid):
        for j in i:
            print(j, end='')
        print()

def copy_word_grid(word_grid):
    # It copies the entirety of the word grid and returns it, for references it allows us to make changes
    # While keeping the original
    grid_1 = []
    for lnth in range(len(word_grid)):
        grid_2 = []
        for elem in word_grid[lnth]:
            grid_2.append(elem)
        grid_1.append(grid_2)
    return grid_1

def extract(word_grid, position, direction, max_len):
    # At a given postiion it should extract a string of letters moving around in set direction in the word grid
    word_grid_size = get_size(word_grid)
    x, y = position
    string = ""
    for i in range(0, max_len):
        if 0 <= x < word_grid_size[0] and 0 <= y < word_grid_size[1]:
            string += word_grid[y][x] 
            x += direction[0]
            y += direction[1]
    return string

def find(word_grid, word):
    # If the word is found within the word grid it will return the positon and the direction of the word grid
    (width, height) = get_size(word_grid)
    for i in range(height):
        for j in range(width):
            for direction in DIRECTIONS:
                if word == extract(word_grid, (i,j), direction, len(word)):
                    return ((i,j), (direction))
    return None

def show_solution(word_grid, word):
    # If the word is found in the word grid it will print the word grid with the word capitalized on there
    # If not it will print the word and that its not found in this word search
    new_grid = copy_word_grid(word_grid)
    finding_word = find(word_grid, word)
    if finding_word == None:
        print(word, "is not found in this word search")
    else:
        position, direction = finding_word
        x, y = position
        a, b = direction
        for i in range(len(word)):
            new_grid[y][x] = new_grid[y][x].upper()
            x += a
            y += b
        print(word.upper(), "can be found as below")
        return print_word_grid(new_grid)

def make_empty_grid(width, height):
    # Creates an empty word grid set be the width and height filled by ? marks 
    empty_grid = []
    for i in range(height):
        w = (["?"] * width)
        empty_grid.append(w)
    return empty_grid

def can_add_word(word_grid, word, position, direction):
    # It checks if a given word is possible to add a word given to us with the grid provided to us as well
    # If so it returns true if not False
    the_word = extract(word_grid, position, direction, len(word))
    if len(word) != len(the_word):
        return False
    for i in range(len(the_word)):
        if the_word[i] != word[i] and the_word[i] != "?":
            return False
    return True

def do_add_word(word_grid, word, position, direction):
    # The function should change the word grid to add the word to it, if possible
    word_allowed = can_add_word(word_grid, word, position, direction)
    x, y = position
    for i in range(len(word)):
        if word_allowed == True:
            word_grid[y][x] = word[i]
            x += direction[0]
            y += direction[1]

def fill_blanks(word_grid):
    # In a given word grid it checks through all the ? marks and replaces it with random letters
    word_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if word_grid[i][j] == "?":
                word_grid[i][j] = random.choice(word_letters)

####
#
#  PROVIDED CODE -- You shouldn't need to change any of this.
#  (it's not that we didn't think you could write this, it's this stuff is either
#  1) really easy and not worth putting in a 1913 project or
#  2) really, really specific. (it's hard to describe the correct function of
#     these two functions without just telling you exactly how to do it.)
#
#  These are provided to "complete" the project -- I.E. these work with the code you write and allow you to use your
#  functions to generate word-searches for personal use. It is RECOMMENDED that you build a front-end for this behavior
#  so you can more easily use and play-with the finished product.
####
def add_word(word_grid, word):
    ''' Attempts to '''
    width, height = get_size(word_grid)
    for attempt_num in range(50):
        direction = random.choice(DIRECTIONS)
        x = random.randrange(width)
        y = random.randrange(height)
        location = (x, y)
        if can_add_word(word_grid, word, location, direction):
            do_add_word(word_grid, word, location, direction)
            return True
    return False

def generate(width, height, words):
    words_actual = []
    word_grid = make_empty_grid(width, height)
    for word in words:
        if add_word(word_grid, word):
            words_actual.append(word)
    fill_blanks(word_grid)
    return word_grid, words_actual

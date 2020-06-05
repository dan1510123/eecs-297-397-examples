# Here is the assignment skeleton we compiled together in class.
# 
# You do not have to structure your code this way, but this is
# one logical way to group things. Feel free to build off of
# this or incorporate ideas into your own code.
#

import sys

# return whether line is a comment
def is_comment(line):
    return line.startswith("#")

# look for width, return next int
def parse_line(line):
    # assuming line is a string, use line.split() to create a list of tokens.
    # find the index of 'width' in the list (list.index() can help with this).
    # the following item after that index will be the integer you want. cast it to
    # an int with the int() function and return that value 
    pass

# return the total line width
def get_width_from_schema(schema_file):
    # initialize total width to 0
    # open schema_file
    # go over lines in file
    # check if comment
    # when it's not, parse line and get the correct int.
    #    add the int to the total width

    # return total width
    pass

# return (valid, invalid)
def calculating_valid_invalid_lines(data_file, line_width):
    # initialize counters for valid lines and invalid lines
    valid_lines, invalid_lines = 0, 0
    
    # open file
    # go over each line in the file
    #    if the length of the line (without trailing \n) matches line_width, 
    #    increment valid lines 
    #
    #    otherwise increment invalid lines
    return valid_lines, invalid_lines



# Get the two arguments from the command line
schema_file = sys.argv[1]
data_file = sys.argv[2]

try:
    line_width = get_width_from_schema(schema_file)
    valid_lines, invalid_lines = calculating_valid_invalid_lines(data_file, line_width)
    print(valid_lines, invalid_lines)

# If we fail opening one of the files in the previous try block,
# this except block will handle the error and print out ‘0 0’
except FileNotFoundError:
    print(0, 0)

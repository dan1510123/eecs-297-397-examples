import sys


input_file_name = "008-testdata.txt"


# If an argument is passed in, use it instead
# of the default file value above.
if len(sys.argv) > 1:
    input_file_name = sys.argv[1]


# Open the file for reading. Text mode (non-binary)
input_file = open(input_file_name, 'r')

# Reads 5 characters from the file
data = input_file.read(5)
print(data)

# Read 1 character from the file
data = input_file.read(1)
print(data)

# Read until end of file (EOF)
data = input_file.read()
print(data)


# Always make sure you close files when you 
# are done with them.
input_file.close()


input_file_again = open(input_file_name)

for line in input_file_again:
    print(len(line))

input_file_again.close()

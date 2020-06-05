EXAMPLE_FILE_NAME = "some-file"

with open(EXAMPLE_FILE_NAME, "w") as output_file:
    output_file.write("line 1\n")
    output_file.write("line 2\n")

# File will be closed at the end of the with block.
# If you try a write outside of the block, an error
# will occur.
# output_file.write("ERROR")



# Append mode will add line to the end of the file.
# Otherwise, file would be overwritten
with open(EXAMPLE_FILE_NAME, "a") as append_file:
    append_file.write("line 3\n")


input("Pause to check file contents. Press Enter.")

with open(EXAMPLE_FILE_NAME, "w") as write_file:
    write_file.write("line 1 again\n")


BINARY_FILE_NAME = "binary-file"


output_file = open(BINARY_FILE_NAME, "wb")

# The next line would be an error:
# output_file.write("this was a string")
#
# Traceback (most recent call last):
#   File "010-binary-files.py", line 3, in <module>
#     output_file.write("this was a string")
# TypeError: a bytes-like object is required, not 'str'


output_file.write(bytes("this was a string", "utf-8"))

# bytes takes an iterable and converts the elements to bytes
output_file.write(bytes([22]))
output_file.write(bytes([18]))

output_file.close()



input_file = open(BINARY_FILE_NAME, "rb")
byte_data = input_file.read(1)
while byte_data:
    print(byte_data)
    byte_data = input_file.read(1)

input_file.close()


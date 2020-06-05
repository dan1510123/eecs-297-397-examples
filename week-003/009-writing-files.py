
# Use 'w' mode to open a file for writing
def output_bad_file(data):
    # "Bad since we are skipping newline characters"
    output_file = open("bad-output.txt", "w")

    for d in data:
        output_file.write(d)

    output_file.close()


def output_good_file(data):
    output_file = open("good-output.txt", "w")

    for d in data:
        output_file.write(d)
        output_file.write('\n')

    output_file.close()


data = ["eecs", "297", "397"]

output_bad_file(data)
output_good_file(data)

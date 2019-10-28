import subprocess
import unittest
import sys


def massage_output(result):
    no_newline = result.rstrip('\n')
    both_vals = no_newline.split()
    if len(both_vals) != 2:
        # At least we will see the result in the testing output
        return result
    else:
        # If there was extra whitespace on a single line, good enough
        return f"{both_vals[0]} {both_vals[1]}"

class MainTest(unittest.TestCase):
    file_to_run = ""

    # You may have to change 'python3' to the name of the
    # executable you use to run python on your system!
    def run_test(self, schema, data, expected):
        result = subprocess.check_output(f"python3 {self.file_to_run} {schema} {data}", shell=True, text=True)
        self.assertEqual(expected, massage_output(result))

    # Normal tests from github
    def test_normal_example_001(self):
       self.run_test("example-001/schema.txt", "example-001/data.txt", "2 1")

    def test_normal_example_002(self):
        self.run_test("example-002/schema.txt", "example-002/data.txt", "4 1")
 
    def test_normal_example_003(self):
        self.run_test("example-003/schema.txt", "example-003/data.txt", "5 4")

    def test_normal_example_004(self):
        self.run_test("example-004/schema.txt", "example-004/data.txt", "4 1")
    # End Normal Test Cases

    # Missing Files
    def test_no_schema(self): 
        self.run_test("example-004/noschema.txt", "example-004/data.txt", "0 0")

    def test_no_data(self): 
        self.run_test("example-004/schema.txt", "example-004/nodata.txt", "0 0")
    # End Missing Files


    # Empty Files
    def test_empty_schema(self):
        self.run_test("example-005/schema.txt", "example-005/data.txt", "0 1")    

    def test_empty_data(self):
        self.run_test("example-006/schema.txt", "example-006/data.txt", "0 0")
    # End Empty Files


    # Width in comment
    def test_width_in_comment(self):
        self.run_test("example-007/schema.txt", "example-007/data.txt", "2 1")
    # End width in comment

    # Other tokens containing "width"
    def test_orig_width_before_width(self):
        self.run_test("example-008/schema.txt", "example-008/data.txt", "2 1")
    # End other tokens containing "width"
    
    # Whitespace special cases
    def test_no_newline_at_end_of_data(self):
        self.run_test("example-009/schema.txt", "example-009/data.txt", "5 4")

    def test_multiple_whitespace_in_schema(self):
        self.run_test("example-010/schema.txt", "example-010/data.txt", "2 1")
    # End whitespace special cases:

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Please provide the name of the python file to test as an argument. Example:")
        print("    python3 test-assignments.py my-final-project.py")
        sys.exit(0)

    # Assume the only argument to this program is the name of the file to test.
    MainTest.file_to_run = sys.argv.pop()
    unittest.main()

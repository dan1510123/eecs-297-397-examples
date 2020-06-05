# Instructions
You should be able to run these integration tests with the command:

```
python3 test-final.py your-python-file.py
```

Substitute your actual file name in place of `your-python-file.py`.

The script assumes Python 3 scripts on your system can be run with with the
command `python3`. If this is not the case, you will have to edit the 
`run_test()` method to invoke `python` instead (or whatever other executable)
you may invoke on your system.

Keep in mind that these tests are end-to-end integration tests. While they should
help you figure out if adjustments are needed for your code's logic, you should focus on 
first breaking your code into smaller functions that can be tested. The integration
tests can help you later with making sure that your overall program logic is correct.

# Tests
Each test shows which files it uses as its input and what the expected output is for the test.
You are encouraged to not only run the tests, but also to look through the example files
to make sure you understand what is being tested in each case.

# Extra Information
Each example directory has and extra file called `expected-width`. These files are not meant to
be read by your program. They are there for your information in case you had any questions about
the expected width for a schema file.
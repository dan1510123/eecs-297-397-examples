def is_float_string(s):
    try:
        f = float(s)
        return True
    # This will handle any exception thrown in the try block
    except:
        return False

def convert_to_float(s):
    return float(s)


print(is_float_string("2.3"))
print(is_float_string("asdfs"))
print()

values = ["25.0", "DSFDDF" "0.0"]
for s in values:
    try:
        10 / convert_to_float(s)
    except ValueError:
        print("Error: Tried to convert non-float string to float")
        print("Program will continue")
    except ZeroDivisionError:
        print("Error: Tried to divide by zero.")
        print("Program will continue")
    except:
        print("Other error handled. Program continues")
    finally:
        print("This is executed regardless of an exception being thrown.")
print()

convert_to_float("sdfsfd")
# Program stops running after the unhandled exception.

print("This line should not print out")

def continue_example():
    try:
        for i in range(10):
            continue
    finally:
        print("This prints for continue")

def break_example():
    try:
        for i in range(10):
            break
    finally:
        print("This prints for break")

def return_example():
    try:
        for i in range(10):
            if i == 5:
                print("Going to return")
                return
    finally:
        print("This prints for return")

continue_example()
break_example()
return_example()

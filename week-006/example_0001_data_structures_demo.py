def calculate_with_list(tuple_list, checkout_list, print_every=-1):
    total = 0
    num_iterations = 0

    for item in checkout_list:
        for tuple in tuple_list:
            if print_every > 0:
                num_iterations += 1
                if num_iterations % print_every == 0:
                    print("Total checks so far:", num_iterations)

            if tuple[0] == item:
                total += tuple[1]
                break

    if print_every > 0:
        print()
        print("Checks performed:", num_iterations)
        print("Size of tuple_list:", len(tuple_list))
        print("Size of checkout list:", len(checkout_list))
        print()

    return total

def calculate_with_dictionary(dictionary, checkout_list, print_every=-1):
    total = 0
    num_iterations = 0

    for item in checkout_list:
        if print_every > 0:
            num_iterations += 1
            if num_iterations % print_every == 0:
                print("Total checks so far:", num_iterations)
        total += dictionary.get(item, 0)

    if print_every > 0:
        print()
        print("Checks performed:", num_iterations)
        print("Size of dictionary:", len(dictionary))
        print("Size of checkout list:", len(checkout_list))
        print()

    return total

SMALL_RANGE = range(1, 101)
LARGE_RANGE = range(1, 100_001)

small_tuple_list = [(str(i), i) for i in SMALL_RANGE]
small_dictionary = {str(i): i for i in SMALL_RANGE}

small_checkout_list = [str(i) for i in SMALL_RANGE]


large_tuple_list = [(str(i), i) for i in LARGE_RANGE]
large_dictionary = {str(i): i for i in LARGE_RANGE}

large_checkout_list = [str(i) for i in LARGE_RANGE]
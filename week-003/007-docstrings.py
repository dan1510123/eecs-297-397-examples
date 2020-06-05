#!/usr/local/bin/python3

def excited_print(message, num_exclamation_points=3):
    """Print out a message string followed by some number
       of exclamation points.

       Parameters
       ----------
       message : str
           String message to print.
       num_exclamation_points : int
           Number of exclamation points to print
           following the message. Default 3.
    """
    print(f"{message}{num_exclamation_points * '!'}")

excited_print("Documentation is the best", 21)

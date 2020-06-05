#!/usr/local/bin/python3

def modify_int(i):
    i += 10
    print("in function", i)

def modify_float(f):
    f += 5.7
    print("in function", f)

def modify_tuple(t):
    t = (9,9,9,9,9)
    print("in function", t)

def modify_bool(b):
    b = not b
    print("in function", b)

def modify_string(s):
    s = s.upper()
    print("in function", s)

def modify_list(l):
    if list:
        l.pop()
    else:
        l.append("new thing")
    print("in function", l)

# int, float, string, bool, and tuple
# will all retain their original values
# even after passed to a function that
# attempts to assign a new value to them

an_int = 1
print("original", an_int)
modify_int(an_int)
print("after", an_int, end='\n\n')

a_float = 4.3
print("original", a_float)
modify_float(a_float)
print("after", a_float, end='\n\n')

a_string = "normal"
print("original", a_string)
modify_string(a_string)
print("after", a_string, end='\n\n')

a_bool = True
print("original", a_bool)
modify_bool(a_bool)
print("after", a_bool, end='\n\n')

a_tuple = (1, 2, 3)
print("original", a_tuple)
modify_tuple(a_tuple)
print("after", a_tuple, end='\n\n')

a_list = ["a", "A", "eh", "Eh"]
print("original", a_list)
modify_list(a_list)
print("after", a_list, end='\n\n')
modify_list(a_list)
print("after again", a_list, end='\n\n')

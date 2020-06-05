#!/usr/local/bin/python3

# Can use 'in' to check if value is in a list.
# Use 'not in' to see if value is missing from list.

def check_for_ringo(band):
    if "Ringo" in band:
        print("I'm a real drummer!")
    elif "ringo" in band:
        print("I guess I can call .capitalize() on myself.")
    else:
        print("Ringo is sad :(")


band_members = ["John", "Paul", "George"]

check_for_ringo(band_members)

if "Ringo" not in band_members and "ringo" not in band_members:
    band_members.append("ringo")

check_for_ringo(band_members)


# Can check if a list is empty by providing the 
# list in a conditional. 

if band_members:
    print("There are band members!")

while band_members:
    print(f"{band_members.pop()} was in the band!")

if not band_members:
    print("No more band members.")

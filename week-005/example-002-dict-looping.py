example_data = [("roses", "red"), ("violets", "blue"), ("sunflowers", "yellow")]


# Can make a dictionary by passing a sequence of key value pairs
flower_colors = dict(example_data)


# Can loop through key value pairs in a dictionary
for key, value in flower_colors.items():
    print(key, value)



# Can loop over just the keys
for key in flower_colors.keys():
    print(key)
    print("If we want the value, we have to get it:", flower_colors[key])


# Can loop over just the values
for value in flower_colors.values():
    print(value)


### How can we loop over keys in sorted order? 


for k in sorted(flower_colors.keys()):
    print(k)








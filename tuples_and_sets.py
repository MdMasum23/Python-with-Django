# Tuple Handling

# Creating a tuple with duplicate fruits
fruits = ("apple", "banana", "apple", "orange", "banana", "grape")

# Access and print individual elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Using tuple methods
print("Count of 'apple':", fruits.count("apple"))
print("Index of 'orange':", fruits.index("orange"))

# Tuple unpacking
fruit1, fruit2, fruit3, fruit4, fruit5, fruit6 = fruits
print("Unpacked fruits:", fruit1, fruit2, fruit3, fruit4, fruit5, fruit6)

# Set Handling

# Creating a set with duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", numbers)

# Create another set
other_numbers = {4, 5, 6, 7}

# Union
print("Union:", numbers.union(other_numbers))

# Intersection
print("Intersection:", numbers.intersection(other_numbers))

# Difference
print("Difference (numbers - other_numbers):", numbers.difference(other_numbers))

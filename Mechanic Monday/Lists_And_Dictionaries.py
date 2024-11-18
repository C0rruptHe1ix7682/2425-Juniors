#Lists are ordered
#Dictionaries are unordered collections/ Key-Value Pairs

fruits = ['apple', 'banana', 'kiwi', 'strawberry'] #List
print(fruits)

fruit_colors = {'apple': 'red', 'banana': 'green', 'kiwi': 'golden'} #Dictionary

#List Methods - append, remove, sort, pop, and insert.

#Add
fruits.append('orange')
print(fruits)

#Remove
fruits.remove('banana')
print(fruits)

#Sort
fruits.sort()
print(fruits)

#Nest
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#output
print(matrix[1][1])
print(matrix[0][2])
print(matrix[2][0])

# Dictionary Methods - Accessing Keys and Values
keys = fruit_colors.keys()
values = fruit_colors.values()
print(keys)
print(values)

# Update
fruit_colors['apple'] = 'green'
print(values)

# Get()
print(fruit_colors.get('orange', 'Not Found'))

fruit_colors['orange'] = "blood orange"

fruit_colors.update({'grapes': 'purple'})
print(fruit_colors)
# set list name and assign names to index
cities = ['kumasi', 'tamale', 'ho', 'wa', 'madina', 'lapaz', 'boko']
print(cities)
# Display the last list using negative index
print(cities[-1])
# Display message to each city
message = ' is my favourite city'
print(cities[0] + message)
print(cities[1] + message)
print(cities[2] + message)
print(cities[3] + message)
print(cities[4] + message)
print(cities[5] + message)
print(cities[6] + message)
# change index 0 to "Accra"
cities[0] = 'accra'
print(cities)
# Add kasoa to the list using append
cities.append('kasoa')
print(cities)
# insert "medie " to the list of cities
cities.insert(0, 'medie')
print(cities)
# delete using del
del cities[-1]
print(cities)
# Remove last city and print message with it
popped_city = cities.pop()
message = 'I hate '
print(message + popped_city +
      ' that is why i removed it from my favourite cities in ghana')
# Remove first city and print message with it
popped_city = cities.pop(0)
print(message + popped_city +
      ' that is why i removed it from my favourite cities in ghana')
print(cities)
# Remove "madina " using its name
cities.remove('madina')
print(cities)
# Use sorting to organize the list
# cities.sort()
# print(cities)
# reverse the list of cities
# cities.sort(reverse=True)
#print (cities)
# Using Sorted
# print(cities)
# print(sorted(cities))
#print(sorted(cities, reverse=True))
# Reverse the order of list
cities.reverse()
print(cities)
# Find the length of list
len(cities)
print(len(cities))

# Printing the list through a for loop
magicians = ['alice', 'david', 'caroline', 'tawia', 'afforkor', 'isaac']
for magician in magicians:
    print(magician.title() + ", that was a great trick")
print("I can't wait to see your next trick " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

print("\nThe first three magicians in the list are: ")
print(magicians[0:3])

print('\nThree magicians from the middle of the list are: ')
print(magicians[1:4])

print('\nThe last three magicians in the list are: ')
print(magicians[-3:])

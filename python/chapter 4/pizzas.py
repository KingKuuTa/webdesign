pizzas = ['pepperoni pizza', 'chesse pizza',
          'pineapple pizza', 'vegetable pizza', 'lemon pizza']
for pizza in pizzas:
    print('I like ' + pizza + '.')
print("\nI really like pizzas. ")

print("The first three items in the list are: ")
print(pizzas[0:3])

print('Three items from the middle of the list are: ')
print(pizzas[1:4])

print("The last three items in the list are: ")
print(pizzas[-3:])

friend_pizzas = pizzas[:]

pizzas.append('green pizza')
friend_pizzas.append('orange pizza')
print(pizzas)
print(friend_pizzas)

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

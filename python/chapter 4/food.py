my_foods = ['pizza', 'falafei', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friends favourite foods are")
for foods in friends_foods:
    print(foods)

# recipe
#* name recipe
#* ingredients
#* preparation time (minutes)
#* Dificulty (easy, medium, hard)
#* Send print to recipe

name_recipe = input("Enter the name of the recipe: ")
question = int(input("How many ingredients does the recipe have? "))
ingredients = []
print(f"Enter {question} ingredients of the recipe: ")

for i in range(0, question):
    ingredient = input(f"Enter the {i + 1} ingredient of the recipe: ")
    ingredients.append(ingredient)
ingredients = ', '.join(ingredients)# join the list into a string separate by commas
    
time = int(input("Enter the preparation time of the recipe (in minutes): "))
difficulty = input("Enter the difficulty of the recipe (easy, medium, hard): ")

print(f"Recipe: {name_recipe}")
print(f"Ingredients: {ingredients}")
print(f"Preparation time: {time} minutes")
print(f"Difficulty: {difficulty}")
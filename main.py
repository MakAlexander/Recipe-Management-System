import json

# Function to add a new recipe
def add_recipe(name, ingredients, instructions, prep_time):
    try:
        with open('recipes.json', 'r+') as file:
            try:
                recipes = json.load(file)
            except json.JSONDecodeError:
                recipes = {}
            recipes[name] = {
                'ingredients': ingredients,
                'instructions': instructions,
                'prep_time': prep_time
            }
            file.seek(0)
            json.dump(recipes, file, indent=4)
            file.truncate()
        return "Recipe added successfully."
    except Exception as e:
        return str(e)

# Function to view all recipes
def view_recipes():
    try:
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
            if recipes:
                for name, details in recipes.items():
                    print(f"Recipe: {name}")
                    for ingredient in details['ingredients']:
                        print(f"Ingredient: {ingredient['name']}, Quantity: {ingredient['quantity']}")
                    print(f"Instructions: {details['instructions']}")
                    print(f"Preparation time: {details['prep_time']} minutes\n")
            else:
                print("No recipes found.")
    except Exception as e:
        print(str(e))

# Function to update an existing recipe
def update_recipe(name, ingredients=None, instructions=None, prep_time=None):
    try:
        with open('recipes.json', 'r+') as file:
            recipes = json.load(file)
            if name in recipes:
                if ingredients:
                    recipes[name]['ingredients'] = ingredients
                if instructions:
                    recipes[name]['instructions'] = instructions
                if prep_time:
                    recipes[name]['prep_time'] = prep_time
                file.seek(0)
                json.dump(recipes, file, indent=4)
                file.truncate()
                return "Recipe updated successfully."
            else:
                return "Recipe not found."
    except Exception as e:
        return str(e)

# Function to delete a recipe
def delete_recipe(name):
    try:
        with open('recipes.json', 'r+') as file:
            recipes = json.load(file)
            if name in recipes:
                del recipes[name]
                file.seek(0)
                json.dump(recipes, file, indent=4)
                file.truncate()
                return "Recipe deleted successfully."
            else:
                return "Recipe not found."
    except Exception as e:
        return str(e)

# Function to display the landing page
def landing_page():
    print("""
Welcome to My Recipe Book. Type either of these commands to continue:
/about               Brings you to the about page
/manage-recipes      Brings you to the manage-recipes page 
/recipe-list         Brings you to the recipe-list page
/help                Displays additional commands
    """)

if __name__ == "__main__":
    landing_page()
    while True:
        command = input("Enter command: ").strip()
        if command == "/about":
            print("This is the Recipe Book application.")
        elif command == "/manage-recipes":
            print("Available commands for managing recipes:")
            print("/add-recipe        Add a new recipe")
            print("/update-recipe     Update an existing recipe")
            print("/delete-recipe     Delete a recipe")
            manage_command = input("Enter manage command: ").strip()
            if manage_command == "/add-recipe":
                name = input("Enter recipe name: ").strip()
                ingredients = []
                while True:
                    ingredient_name = input("Enter ingredient name (or press Enter to finish): ").strip()
                    if not ingredient_name:
                        break
                    quantity = input(f"Enter quantity for {ingredient_name}: ").strip()
                    ingredients.append({'name': ingredient_name, 'quantity': quantity})
                instructions = input("Enter instructions: ").strip()
                prep_time = input("Enter preparation time in minutes: ").strip()
                print(add_recipe(name, ingredients, instructions, prep_time))
            elif manage_command == "/update-recipe":
                name = input("Enter recipe name to update: ").strip()
                ingredients = []
                while True:
                    ingredient_name = input("Enter ingredient name (or press Enter to finish): ").strip()
                    if not ingredient_name:
                        break
                    quantity = input(f"Enter quantity for {ingredient_name}: ").strip()
                    ingredients.append({'name': ingredient_name, 'quantity': quantity})
                instructions = input("Enter new instructions or press enter to skip: ").strip()
                prep_time = input("Enter new preparation time in minutes or press enter to skip: ").strip()
                updated_ingredients = ingredients if ingredients else None
                updated_instructions = instructions if instructions else None
                updated_prep_time = prep_time if prep_time else None
                print(update_recipe(name, updated_ingredients, updated_instructions, updated_prep_time))
            elif manage_command == "/delete-recipe":
                name = input("Enter recipe name to delete: ").strip()
                print(delete_recipe(name))
            else:
                print("Unknown manage command. Type /help for available commands.")
        elif command == "/recipe-list":
            view_recipes()
        elif command == "/help":
            landing_page()
        else:
            print("Unknown command. Type /help for available commands.")

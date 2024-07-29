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
 __  __        _____           _              ____              _   
|  \/  |_   _  |  _ \ ___  ___(_)_ __   ___  | __ )  ___   ___ | | __
| |\/| | | | | | |_) / _ \/ __| | '_ \ / _ \ |  _ \ / _ \ / _ \| |/ /
| |  | | |_| | |  _ <  __/ (__| | |_) |  __/ | |_) | (_) | (_) |   <
|_|  |_|\__, | |_| \_\___|\___|_| .__/ \___| |____/ \___/ \___/|_|\_\.
        |___/                   |_|                                  
          
Welcome to My Recipe Book. Type either of these commands to continue:
/about               Brings you to the about page
/manage-recipes      Brings you to the manage-recipes page 
/recipe-list         Brings you to the recipe-list page
/home                Brings you back to the homepage
/exit                Exits My Recipe Book program
    """)

if __name__ == "__main__":
    landing_page()
    while True:
        command = input("Enter command: ").strip()
        if command == "/about":
            print("""
                      _    _                 _   
                     / \  | |__   ___  _   _| |_ 
                    / _ \ | '_ \ / _ \| | | | __|
                   / ___ \| |_) | (_) | |_| | |_ 
                  /_/   \_\_.__/ \___/ \__,_|\__|

            Welcome to Your Ultimate Recipe Companion!
            
    The My Recipe Book Program is designed with every cooking enthusiast in mind, 
whether you're a seasoned chef or a home cook just starting out. We understand that 
cooking is more than just preparing food – it's about creativity, experimentation, 
and sharing your culinary creations with others. That's why we've created a 
comprehensive platform to help you manage and explore recipes with ease.

Features at a Glance:

* Add Recipes:     Easily add new recipes with a simple form that captures the name, 
                   ingredients, and step-by-step instructions. Keep track of all your 
                   culinary masterpieces in one place.

* View Recipes:    Browse through your collection of recipes effortlessly. 
                   Our organized list view lets you find exactly what you're 
                   looking for, whether it's a quick weekday dinner or an elaborate weekend feast.

* Update Recipes:  Made a tweak to your favorite dish? Update recipe details on 
                   the fly to ensure your collection is always up-to-date with your 
                   latest culinary innovations.

* Delete Recipes:  Clear out the clutter by deleting recipes you no longer need. 
                   Keep your recipe book tidy and focused on what matters most.


Type ‘/home’ to go back to home:
	
                  """)
        elif command == "/manage-recipes":
            print(""" 
          __  __                                ____           _                 
         |  \/  | __ _ _ __   __ _  __ _  ___  |  _ \ ___  ___(_)_ __   ___  ___ 
         | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ | |_) / _ \/ __| | '_ \ / _ \/ __|
         | |  | | (_| | | | | (_| | (_| |  __/ |  _ <  __/ (__| | |_) |  __/\__ \\
         |_|  |_|\__,_|_| |_|\__,_|\__, |\___| |_| \_\___|\___|_| .__/ \___||___/
                                    |___/                        |_|              

""")
            print("Available commands for managing recipes:")
            print("/add-recipe        Add a new recipe")
            print("/update-recipe     Update an existing recipe")
            print("/delete-recipe     Delete a recipe")
            print("/home              Brings you back to the homepage")
            print("/exit              Exits My Recipe Book program")
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
                print("Type ‘/home’ to go back to home:")
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
                print("Type ‘/home’ to go back to home:")
            elif manage_command == "/delete-recipe":
                name = input("Enter recipe name to delete: ").strip()
                print(delete_recipe(name))
                print("Type ‘/home’ to go back to home:")
            elif manage_command == "/home":
                landing_page()
            elif manage_command == "/exit":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Unknown manage command. Type /home for available commands.")
        elif command == "/recipe-list":
            print(""" ____           _              _     _     _   
                     |  _ \ ___  ___(_)_ __   ___  | |   (_)___| |_ 
                     | |_) / _ \/ __| | '_ \ / _ \ | |   | / __| __|
                     |  _ <  __/ (__| | |_) |  __/ | |___| \__ \ |_ 
                     |_| \_\___|\___|_| .__/ \___| |_____|_|___/\__|
                                    |_|                           
            
                Welcome to the Recipe List page for navigating through all your saved recipes. 
     Here, you can easily view your recipes, ensuring you find exactly what you need quickly and efficiently.
""")
            view_recipes()
        elif command == "/home":
            landing_page()
        elif command == "/exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Unknown command. Type /home for available commands.")

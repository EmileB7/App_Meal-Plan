class Recipe:
    def __init__(self, id, name, image, description):
        self.id = id
        self.name = name
        self.image = image
        self.description = description
        self.ingredients = []  # List of (ingredient_name, quantity_per_serving)

    def add_ingredient(self, name, quantity_per_serving):
        self.ingredients.append((name, quantity_per_serving))

class GroceryList:
    def __init__(self):
        self.ingredients = {}  # Dictionary to store ingredient names and total quantities

    def add_ingredients(self, recipe, servings):
        for ingredient_name, quantity_per_serving in recipe.ingredients:
            total_quantity = quantity_per_serving * servings
            if ingredient_name in self.ingredients:
                self.ingredients[ingredient_name] += total_quantity
            else:
                self.ingredients[ingredient_name] = total_quantity

    def get_list(self):
        return self.ingredients
    


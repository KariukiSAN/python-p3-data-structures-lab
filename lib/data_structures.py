spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = []
    for item in spicy_foods:
        new = [value for key,value in item.items()]
        spicy_names.append(new[0])
    return spicy_names


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
 

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_menu = f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
        print(food_menu)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food 


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")  


def get_average_heat_level(spicy_foods):
    heats = [food['heat_level'] for food in spicy_foods]
    average = sum(heats)/len(spicy_foods)
    return int(average)


def create_spicy_food(spicy_foods, spicy_food):
    new_list = [food for food in spicy_foods]
    new_list.append(spicy_food)
    return new_list
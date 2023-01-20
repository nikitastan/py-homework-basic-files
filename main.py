# Задание №1

with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = f.readline().strip()
            ingredient_name, ingredient_quantity, unit_of_measurement = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': ingredient_quantity,
                'measure': unit_of_measurement
            })
        f.readline()
        cook_book[dish_name] = ingredients

# Задание №2
def get_shop_list_by_dishes(dishes, person_count, cook_book=cook_book):
    ingredients_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients_list.keys():
                ingredients_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
            else:
                ingredients_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': int(ingredient['quantity']) * person_count
        }
    return ingredients_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание 3
import os

files_dict = {}
new_dir = os.getcwd() + r'\texts'

for filename in os.listdir(new_dir):
    with open(os.path.join(new_dir, filename), 'r', encoding='utf-8') as f:
        files_dict[filename] = len(f.readlines())

for filename in sorted(files_dict, key=files_dict.get):
    with open(os.path.join(new_dir, filename), 'r', encoding='utf-8') as f:
        with open(os.path.join(os.getcwd(), 'tst_all.txt'), 'a', encoding='utf-8') as f2:
            f2.writelines(['\n'.join([filename, str(files_dict[filename])])+'\n'] + f.readlines())





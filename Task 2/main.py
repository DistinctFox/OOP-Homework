from pprint import pprint


def get_cook_book():
    with open("recipes.txt", "r", encoding='utf-8') as f:
        dishes = {}
        for line in f:
            dish_name = line.strip()
            ingredient_count = int(f.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': quantity,
                     'measure': measure
                     }
                )
            dishes[dish_name] = ingredients
            f.readline()
    return dishes


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book.get(dish):
            shop_list[ingredient.get('ingredient_name')] = {
                'measure': ingredient.get('measure'),
                'quantity': ingredient.get('quantity') * person_count
            }
    pprint(shop_list, sort_dicts=False)


if __name__ == "__main__":
    get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)

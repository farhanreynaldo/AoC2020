from functools import reduce
from typing import NamedTuple, List
from collections import defaultdict
from itertools import chain

SAMPLE = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


class Food(NamedTuple):
    ingredients: List[str]
    allergents: List[str]


def parse_foods(raw):
    foods = []
    for food in raw.split("\n"):
        ingredients, allergents = food.split("(contains ")
        allergents = allergents.rstrip(")").split(", ")
        ingredients = ingredients.split()
        foods.append(Food(ingredients=ingredients, allergents=allergents))
    return foods


def find_allergent(foods):
    allergents = {allergent for food in foods for allergent in food.allergents}
    allergent_ingredients = set()
    allergent_dict = defaultdict(set)
    for allergent in allergents:
        food_ingredients = [
            food.ingredients for food in foods if allergent in food.allergents
        ]
        intersect = reduce(
            lambda food1, food2: set(food1) & set(food2), food_ingredients
        )
        allergent_ingredients.update(intersect)
        allergent_dict[allergent] = set(intersect)
    return allergent_dict


def count_non_allergent(raw):
    foods = parse_foods(raw)
    allergent_dict = find_allergent(foods)
    allergent_ingredients = list(chain(*allergent_dict.values()))
    return sum(
        ingredient not in allergent_ingredients
        for food in foods
        for ingredient in food.ingredients
    )


def arrange_ingredients(raw):
    foods = parse_foods(raw)
    allergent_dict = find_allergent(foods)
    seen_allergent = defaultdict(set)
    while len(seen_allergent) < len(allergent_dict):
        for allergent in allergent_dict:
            seen_ingredients = set(chain(*seen_allergent.values()))
            ingredients = allergent_dict[allergent] - seen_ingredients
            if len(ingredients) == 1:
                seen_allergent[allergent] = ingredients
            else:
                continue
    return ",".join(
        ingredient
        for allergent in sorted(seen_allergent)
        for ingredient in seen_allergent[allergent]
    )


assert count_non_allergent(SAMPLE) == 5
day21 = open("input/day21.txt").read()
assert arrange_ingredients(SAMPLE) == 'mxmxvkd,sqjhc,fvjkl'
print(arrange_ingredients(day21))

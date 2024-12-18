from dataclasses import dataclass
from typing import List, Tuple, Union
from .ingredients import LiquidIngredient, SolidIngredient

@dataclass
class BaseDrink:
    name: str
    ingredients: List[Tuple[Union[LiquidIngredient, SolidIngredient], float]]
    sell_price: float

    def __post_init__(self):
        self.alcohols = []
        self.liquids = []
        self.solids = []
        self._organize_ingredients()
        self._calculate_real_price()

    def _organize_ingredients(self):
        for ingredient, amount in self.ingredients:
            if isinstance(ingredient, LiquidIngredient):
                if ingredient.liquid_type == "Alcohol":
                    self.alcohols.append((ingredient, amount))
                else:
                    self.liquids.append((ingredient, amount))
            elif isinstance(ingredient, SolidIngredient):
                self.solids.append((ingredient, amount))

    def _calculate_real_price(self):
        total = 0
        for ingredient, amount in self.ingredients:
            if isinstance(ingredient, LiquidIngredient):
                total += ingredient.price_per_ml * amount
            elif isinstance(ingredient, SolidIngredient):
                total += ingredient.price_per_gram * amount
        self.real_price = round(total, 2)

@dataclass
class Cocktail(BaseDrink):
    sell_price: float = 5.0

@dataclass
class Shot(BaseDrink):
    sell_price: float = 2.5

@dataclass
class Gluwein:
    name: str
    alcohol: Tuple[LiquidIngredient, float]
    sell_price: float = 2.5

    def __post_init__(self):
        self.real_price = round(self.alcohol[0].price_per_ml * self.alcohol[1], 2) 
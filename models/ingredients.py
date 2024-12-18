from dataclasses import dataclass

@dataclass
class LiquidIngredient:
    name: str
    liquid_type: str
    price_per_bottle: float
    volume: float

    def __post_init__(self):
        self.price_per_ml = self.price_per_bottle / self.volume

@dataclass
class SolidIngredient:
    name: str
    solid_type: str
    price: float
    grams: float

    def __post_init__(self):
        self.price_per_gram = self.price / self.grams 
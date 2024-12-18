from models.ingredients import LiquidIngredient, SolidIngredient

# Alcohols
ROM = LiquidIngredient("Rom", "Alcohol", 20, 1000)
GIN = LiquidIngredient("Gin", "Alcohol", 23, 1000)
VODKA = LiquidIngredient("Vodka", "Alcohol", 15, 1000)
WHISKEY = LiquidIngredient("Whiskey", "Alcohol", 25, 1000)
ANGOSTURA = LiquidIngredient("Angostura", "Alcohol", 20, 200)
AMARETTO = LiquidIngredient("Amaretto", "Alcohol", 25, 700)
GLUWEIN = LiquidIngredient("Gluwein", "Alcohol", 3, 1000)
SECCO = LiquidIngredient("Secco", "Alcohol", 10, 750)

# Solvents
TONIC = LiquidIngredient("Tonic", "Lemonade", 10, 1000)
GINGER_BEER = LiquidIngredient("Ginger Beer", "Lemonade", 10, 1000)
SODA = LiquidIngredient("Soda", "Lemonade", 10, 1000)
EGG_WHITE = LiquidIngredient("Egg White", "Liquid", 10, 1000)
REDBULL = LiquidIngredient("Redbull", "Lemonade", 0.55, 250)

# Syrups
MONIN_MANDARIN = LiquidIngredient("mandarin syrup", "Syrup", 15, 1000)
MONIN_BERGAMOT = LiquidIngredient("bergamot syrup", "Syrup", 15, 1000)
MONIN_RASPBERRY = LiquidIngredient("raspberry syrup", "Syrup", 15, 1000)
ELDERFLOWER = LiquidIngredient("elderflower syrup", "Syrup", 15, 1000)
MOHITO_SYRUP = LiquidIngredient("mohito syrup", "Syrup", 15, 1000)

# Lemon
LEMON = LiquidIngredient("Lemon", "Lemon", 6, 1000)

# Juices
ORANGE_JUICE = LiquidIngredient("Orange Juice", "Juice", 5, 1000)
GRAPEFRUIT = LiquidIngredient("Grapefruit Juice", "Juice", 5, 1000)
CRANBERRY = LiquidIngredient("Cranberry Juice", "Juice", 5, 1000)

# Ice and Garnishes
ICE = SolidIngredient("Ice", "Ice", 10, 5000)
MINT = SolidIngredient("Mint", "Garnish", 2, 20)
BASIL = SolidIngredient("Basil", "Garnish", 2, 20)
ROSEMARY = SolidIngredient("Rosemary", "Garnish", 2, 20)
ORANGE = SolidIngredient("Orange", "Garnish", 4, 1000)
STAR_ANISE = SolidIngredient("Star Anise", "Garnish", 2, 20)
CINNAMON = SolidIngredient("Cinnamon", "Garnish", 2, 20)
LIME = SolidIngredient("Lime", "Garnish", 4, 400)

# Create a dictionary of all ingredients for easy access
INGREDIENTS = {
    ingredient.name: ingredient for ingredient in [
        ROM, GIN, VODKA, WHISKEY, ANGOSTURA, AMARETTO, GLUWEIN, SECCO,
        TONIC, GINGER_BEER, SODA, EGG_WHITE, REDBULL,
        MONIN_MANDARIN, MONIN_BERGAMOT, MONIN_RASPBERRY, ELDERFLOWER, MOHITO_SYRUP,
        LEMON, ORANGE_JUICE, GRAPEFRUIT, CRANBERRY,
        ICE, MINT, BASIL, ROSEMARY, ORANGE, STAR_ANISE, CINNAMON, LIME
    ]
} 
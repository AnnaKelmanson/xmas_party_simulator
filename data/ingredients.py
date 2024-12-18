import json
from pathlib import Path
from models.ingredients import LiquidIngredient, SolidIngredient

# Load ingredient data
data_path = Path(__file__).parent / "ingredients.json"
with open(data_path, "r") as f:
    data = json.load(f)

# Alcohols
ROM = LiquidIngredient("Rom", data["alcohols"]["Rom"]["type"], data["alcohols"]["Rom"]["price"], data["alcohols"]["Rom"]["volume"])
GIN = LiquidIngredient("Gin", data["alcohols"]["Gin"]["type"], data["alcohols"]["Gin"]["price"], data["alcohols"]["Gin"]["volume"])
VODKA = LiquidIngredient("Vodka", data["alcohols"]["Vodka"]["type"], data["alcohols"]["Vodka"]["price"], data["alcohols"]["Vodka"]["volume"])
WHISKEY = LiquidIngredient("Whiskey", data["alcohols"]["Whiskey"]["type"], data["alcohols"]["Whiskey"]["price"], data["alcohols"]["Whiskey"]["volume"])
ANGOSTURA = LiquidIngredient("Angostura", data["alcohols"]["Angostura"]["type"], data["alcohols"]["Angostura"]["price"], data["alcohols"]["Angostura"]["volume"])
AMARETTO = LiquidIngredient("Amaretto", data["alcohols"]["Amaretto"]["type"], data["alcohols"]["Amaretto"]["price"], data["alcohols"]["Amaretto"]["volume"])
GLUWEIN = LiquidIngredient("Gluwein", data["alcohols"]["Gluwein"]["type"], data["alcohols"]["Gluwein"]["price"], data["alcohols"]["Gluwein"]["volume"])
SECCO = LiquidIngredient("Secco", data["alcohols"]["Secco"]["type"], data["alcohols"]["Secco"]["price"], data["alcohols"]["Secco"]["volume"])

# Solvents
TONIC = LiquidIngredient("Tonic", data["solvents"]["Tonic"]["type"], data["solvents"]["Tonic"]["price"], data["solvents"]["Tonic"]["volume"])
GINGER_BEER = LiquidIngredient("Ginger Beer", data["solvents"]["Ginger Beer"]["type"], data["solvents"]["Ginger Beer"]["price"], data["solvents"]["Ginger Beer"]["volume"])
SODA = LiquidIngredient("Soda", data["solvents"]["Soda"]["type"], data["solvents"]["Soda"]["price"], data["solvents"]["Soda"]["volume"])
EGG_WHITE = LiquidIngredient("Egg White", data["solvents"]["Egg White"]["type"], data["solvents"]["Egg White"]["price"], data["solvents"]["Egg White"]["volume"])
REDBULL = LiquidIngredient("Redbull", data["solvents"]["Redbull"]["type"], data["solvents"]["Redbull"]["price"], data["solvents"]["Redbull"]["volume"])

# Syrups
MONIN_MANDARIN = LiquidIngredient("mandarin syrup", data["syrups"]["mandarin syrup"]["type"], data["syrups"]["mandarin syrup"]["price"], data["syrups"]["mandarin syrup"]["volume"])
MONIN_BERGAMOT = LiquidIngredient("bergamot syrup", data["syrups"]["bergamot syrup"]["type"], data["syrups"]["bergamot syrup"]["price"], data["syrups"]["bergamot syrup"]["volume"])
MONIN_RASPBERRY = LiquidIngredient("raspberry syrup", data["syrups"]["raspberry syrup"]["type"], data["syrups"]["raspberry syrup"]["price"], data["syrups"]["raspberry syrup"]["volume"])
ELDERFLOWER = LiquidIngredient("elderflower syrup", data["syrups"]["elderflower syrup"]["type"], data["syrups"]["elderflower syrup"]["price"], data["syrups"]["elderflower syrup"]["volume"])
MOHITO_SYRUP = LiquidIngredient("mohito syrup", data["syrups"]["mohito syrup"]["type"], data["syrups"]["mohito syrup"]["price"], data["syrups"]["mohito syrup"]["volume"])

# Lemon
LEMON = LiquidIngredient("Lemon", data["lemons"]["Lemon"]["type"], data["lemons"]["Lemon"]["price"], data["lemons"]["Lemon"]["volume"])

# Juices
ORANGE_JUICE = LiquidIngredient("Orange Juice", data["juices"]["Orange Juice"]["type"], data["juices"]["Orange Juice"]["price"], data["juices"]["Orange Juice"]["volume"])
GRAPEFRUIT = LiquidIngredient("Grapefruit Juice", data["juices"]["Grapefruit Juice"]["type"], data["juices"]["Grapefruit Juice"]["price"], data["juices"]["Grapefruit Juice"]["volume"])
CRANBERRY = LiquidIngredient("Cranberry Juice", data["juices"]["Cranberry Juice"]["type"], data["juices"]["Cranberry Juice"]["price"], data["juices"]["Cranberry Juice"]["volume"])

# Ice and Garnishes
ICE = SolidIngredient("Ice", data["garnishes"]["Ice"]["type"], data["garnishes"]["Ice"]["price"], data["garnishes"]["Ice"]["weight"])
MINT = SolidIngredient("Mint", data["garnishes"]["Mint"]["type"], data["garnishes"]["Mint"]["price"], data["garnishes"]["Mint"]["weight"])
BASIL = SolidIngredient("Basil", data["garnishes"]["Basil"]["type"], data["garnishes"]["Basil"]["price"], data["garnishes"]["Basil"]["weight"])
ROSEMARY = SolidIngredient("Rosemary", data["garnishes"]["Rosemary"]["type"], data["garnishes"]["Rosemary"]["price"], data["garnishes"]["Rosemary"]["weight"])
ORANGE = SolidIngredient("Orange", data["garnishes"]["Orange"]["type"], data["garnishes"]["Orange"]["price"], data["garnishes"]["Orange"]["weight"])
STAR_ANISE = SolidIngredient("Star Anise", data["garnishes"]["Star Anise"]["type"], data["garnishes"]["Star Anise"]["price"], data["garnishes"]["Star Anise"]["weight"])
CINNAMON = SolidIngredient("Cinnamon", data["garnishes"]["Cinnamon"]["type"], data["garnishes"]["Cinnamon"]["price"], data["garnishes"]["Cinnamon"]["weight"])
LIME = SolidIngredient("Lime", data["garnishes"]["Lime"]["type"], data["garnishes"]["Lime"]["price"], data["garnishes"]["Lime"]["weight"])

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
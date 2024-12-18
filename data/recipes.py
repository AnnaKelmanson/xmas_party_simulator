from models.drinks import Cocktail, Shot, Gluwein
from .ingredients import *

REGULAR_COCKTAILS = {
    "Strasbourg": Cocktail(
        "Strasbourg",
        [(ROM, 60), (LEMON, 15), (MONIN_BERGAMOT, 20), (SODA, 100),
         (ICE, 50), (BASIL, 1), (ANGOSTURA, 3)]
    ),
    "Raspberry Grapefruit": Cocktail(
        "Raspberry Grapefruit",
        [(ROM, 60), (LEMON, 5), (MONIN_RASPBERRY, 15), (SODA, 100),
         (ICE, 50), (ROSEMARY, 1), (ANGOSTURA, 3), (GRAPEFRUIT, 15)]
    ),
    "Gluwein": Gluwein("Gluwein", (GLUWEIN, 200)),
    "London Mule": Cocktail(
        "London Mule",
        [(GIN, 45), (GINGER_BEER, 150), (ICE, 50), (MINT, 1), (LIME, 5)]
    ),
    "Moscow Mule": Cocktail(
        "Moscow Mule",
        [(VODKA, 45), (GINGER_BEER, 100), (ICE, 50), (MINT, 1), (LIME, 5)]
    ),
    "Mojito": Cocktail(
        "Mojito",
        [(ROM, 50), (LEMON, 15), (MOHITO_SYRUP, 20), (SODA, 100),
         (ICE, 50), (MINT, 3)]
    ),
    "Raspberry Gin Tonic": Cocktail(
        "Raspberry Gin Tonic",
        [(GIN, 45), (TONIC, 100), (ICE, 15), (ROSEMARY, 1),
         (MONIN_RASPBERRY, 15)]
    ),
    "Redbull Vodka": Shot(
        "Redbull Vodka",
        [(VODKA, 25), (REDBULL, 25)]
    ),
    "Vodka Shot": Shot("Vodka Shot", [(VODKA, 50)]),
    "Gin Shot": Shot("Gin Shot", [(GIN, 50)]),
    "Gin Tonic": Shot("Gin Tonic", [(GIN, 50), (TONIC, 100)])
}

LIMITED_COCKTAILS = {
    "Mandarin fizz": Cocktail(
        "Mandarin fizz",
        [(ROM, 60), (LEMON, 15), (MONIN_MANDARIN, 20), (SODA, 100),
         (ICE, 50), (ROSEMARY, 1), (ANGOSTURA, 3)]
    ),
    "Amaretto sour": Cocktail(
        "Amaretto sour",
        [(AMARETTO, 45), (LEMON, 30), (EGG_WHITE, 15), (WHISKEY, 20),
         (ICE, 50), (ANGOSTURA, 3)]
    ),
    "Hugo": Cocktail(
        "Hugo",
        [(SECCO, 150), (ELDERFLOWER, 15), (ICE, 15), (MINT, 1), (SODA, 50)]
    ),
    "Raspberry Spritz": Cocktail(
        "Raspberry Spritz",
        [(SECCO, 150), (MONIN_RASPBERRY, 15), (ICE, 15), (MINT, 1), (SODA, 50)]
    ),
    "Mandarin Spritz": Cocktail(
        "Mandarin Spritz",
        [(SECCO, 150), (MONIN_MANDARIN, 15), (ICE, 15), (MINT, 1), (SODA, 50)]
    ),
    "Mandarin Whiskey Sour": Cocktail(
        "Mandarin Whiskey Sour",
        [(WHISKEY, 50), (LEMON, 30), (EGG_WHITE, 15), (MONIN_MANDARIN, 20),
         (ICE, 50), (ANGOSTURA, 3)]
    ),
    "Whiskey Shot": Shot("Whiskey Shot", [(WHISKEY, 50)]),
    "Amaretto Shot": Shot("Amaretto Shot", [(AMARETTO, 50)])
}

ALL_COCKTAILS = {**REGULAR_COCKTAILS, **LIMITED_COCKTAILS} 
# 🎄 Anna's Christmas Bar Simulator

Hey there! This is a fun little project I made to help plan drink quantities for our Christmas party. It simulates how many drinks people might order and helps figure out how much of each ingredient we need. 

## 🍸 What's in the Anna's Bar?

The simulator includes some of our favorite drinks:
- Classic cocktails like Mojitos and Moscow Mules
- Special Christmas drinks including Glühwein
- Various shots for the brave ones
- Fancy-schmancy special cocktails like Raspberry Spritz, Strasbourg and more!

## 🎯 What Does It Do?

- Predicts how many drinks we might serve
- Calculates how much of each ingredient we need
- Estimates costs and potential revenue
- Helps avoid running out of important ingredients!

## 🚀 Want to Try It?

1. Clone the repo:


```bash
git clone git@github.com:AnnaKelmanson/xmas_party_simulator.git
```

2. Run the simulation:


```bash
python main.py
```

3. Check out the results in `simulation_results.txt`

## 📊 How It Works

The simulator assumes that each guest:
- Usually orders 2-3 cocktails (give or take)
- Might have 1-2 shots
- Could drink 2-3 Glühweins if they're feeling festive
- Won't spend more than 20 CHF


## 🎨 Project Structure

```plaintext
xmas_party_simulator/
├── data/               # All our drinks and ingredients
├── models/            # The boring but necessary stuff
├── simulation/        # The magic happens here
└── main.py           # Press play!
```


## 🎅 Happy Holidays!

Hope this helps make your party planning a bit easier. Cheers! 🥂

---

### 📝 Example Output

```plaintext
=== AVERAGE STATISTICS ACROSS ALL RUNS ===

Financial Summary:
Average Revenue: CHF 850.25
Average Cost: CHF 156.80
Average Profit: CHF 693.45
Profit Margin: 81.6%

Average Drink Orders:
Moscow Mule: 45.2
Mojito: 42.8
Glühwein: 38.5
...

Average Ingredient Requirements:
Vodka: 2250ml
Mint: 135g
Ice: 2500g
...
```


### 📚 File Structure Details

```plaintext
xmas_party_simulator/
├── data/
│   ├── ingredients.py    # Ingredient definitions and properties
│   └── recipes.py        # Cocktail and shot recipes
├── models/
│   ├── drinks.py        # Base classes for different drink types
│   └── ingredients.py   # Classes for liquid and solid ingredients
├── simulation/
│   └── party_simulator.py # Core simulation logic
└── main.py              # Entry point and configuration
```

### 🔧 Configuration

You can adjust simulation parameters in `config/settings.py`:
```python
    'cocktail_mean': 2,    # Average number of cocktails per person
    'cocktail_std': 1,     # Standard deviation for cocktails
    'shot_mean': 1.5,      # Average number of shots per person
    'shot_std': 1,         # Standard deviation for shots
    'gluwein_mean': 2,     # Average number of gluwein per person
    'gluwein_std': 1,      # Standard deviation for gluwein
    'max_guest_spend': 20,  # Maximum amount a guest can spend
    'num_guests': 55        # Number of guests
```

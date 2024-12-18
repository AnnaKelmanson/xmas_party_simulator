import random
from collections import defaultdict
from typing import Dict, Tuple, DefaultDict
from models.drinks import Cocktail, Shot, Gluwein
from models.ingredients import SolidIngredient

class PartySimulator:
    def __init__(self, cocktails: Dict, seed: int = None):
        self.cocktails = cocktails
        if seed is not None:
            random.seed(seed)

        # Define simulation parameters
        self.cocktail_mean = 2  # Average number of cocktails per person
        self.cocktail_std = 1   # Standard deviation for cocktails
        self.shot_mean = 1.5    # Average number of shots per person
        self.shot_std = 1       # Standard deviation for shots
        self.gluwein_mean = 2   # Average number of gluwein per person
        self.gluwein_std = 1    # Standard deviation for gluwein
        self.max_guest_spend = 20  # Maximum amount a guest can spend

    def simulate(self, num_guests: int = 55) -> Tuple[DefaultDict, DefaultDict, int, float, float]:
        drink_orders = defaultdict(int)
        ingredient_usage = defaultdict(float)
        total_drinks_count = 0
        total_revenue = 0
        total_cost = 0

        for _ in range(num_guests):
            guest_total = 0
            
            # Simulate cocktail orders
            num_cocktail_orders = max(0, round(random.gauss(self.cocktail_mean, self.cocktail_std)))
            for _ in range(num_cocktail_orders):
                available_cocktails = [name for name, drink in self.cocktails.items() 
                                     if isinstance(drink, Cocktail)]
                if not available_cocktails:
                    continue
                
                drink_name = random.choice(available_cocktails)
                drink = self.cocktails[drink_name]
                
                if guest_total + drink.sell_price <= self.max_guest_spend:
                    self._process_order(drink, drink_name, drink_orders, ingredient_usage)
                    total_drinks_count += 1
                    guest_total += drink.sell_price
                    total_revenue += drink.sell_price
                    total_cost += drink.real_price

            # Simulate shot orders
            num_shot_orders = max(0, round(random.gauss(self.shot_mean, self.shot_std)))
            for _ in range(num_shot_orders):
                available_shots = [name for name, drink in self.cocktails.items() 
                                 if isinstance(drink, Shot)]
                if not available_shots:
                    continue
                
                drink_name = random.choice(available_shots)
                drink = self.cocktails[drink_name]
                
                if guest_total + drink.sell_price <= self.max_guest_spend:
                    self._process_order(drink, drink_name, drink_orders, ingredient_usage)
                    total_drinks_count += 1
                    guest_total += drink.sell_price
                    total_revenue += drink.sell_price
                    total_cost += drink.real_price

            # Simulate Gluwein orders
            if "Gluwein" in self.cocktails:
                num_gluwein_orders = max(0, round(random.gauss(self.gluwein_mean, self.gluwein_std)))
                for _ in range(num_gluwein_orders):
                    drink = self.cocktails["Gluwein"]
                    
                    if guest_total + drink.sell_price <= self.max_guest_spend:
                        drink_orders["Gluwein"] += 1
                        total_drinks_count += 1
                        guest_total += drink.sell_price
                        total_revenue += drink.sell_price
                        total_cost += drink.real_price
                        ingredient_usage[drink.alcohol[0].name] += drink.alcohol[1]

        return drink_orders, ingredient_usage, total_drinks_count, total_revenue, total_cost

    def _process_order(self, drink, drink_name: str, 
                      drink_orders: DefaultDict, ingredient_usage: DefaultDict):
        drink_orders[drink_name] += 1
        if isinstance(drink, (Cocktail, Shot)):
            for ingredient, amount in drink.ingredients:
                ingredient_usage[ingredient.name] += amount

    def run_multiple(self, num_runs: int, output_file: str = 'simulation_results.txt'):
        print(f"\nRunning {num_runs} party simulations...")
        
        total_drinks = defaultdict(int)
        total_ingredients = defaultdict(float)
        total_per_run = []
        total_revenues = []
        total_costs = []
        
        for run in range(num_runs):
            print(f"\nSimulation #{run + 1}")
            drink_orders, ingredient_usage, total_count, revenue, cost = self.simulate()
            
            total_per_run.append(total_count)
            total_revenues.append(revenue)
            total_costs.append(cost)
            
            # Print drink statistics
            print("\nDrink Orders:")
            for drink, count in sorted(drink_orders.items(), key=lambda x: x[1], reverse=True):
                print(f"{drink}: {count}")
                total_drinks[drink] += count
            
            print(f"\nTotal drinks this run: {total_count}")
            
            # Add to total ingredients
            for ing, amount in ingredient_usage.items():
                total_ingredients[ing] += amount
        
        self._write_results(output_file, num_runs, total_drinks, 
                           total_ingredients, total_per_run, total_revenues, total_costs)

    def _write_results(self, output_file: str, num_runs: int, 
                      total_drinks: Dict, total_ingredients: Dict,
                      total_per_run: list, total_revenues: list, total_costs: list):
        with open(output_file, 'w') as f:
            f.write("\n=== AVERAGE STATISTICS ACROSS ALL RUNS ===\n")
            
            # Add revenue statistics
            avg_revenue = sum(total_revenues) / num_runs
            avg_cost = sum(total_costs) / num_runs
            avg_profit = avg_revenue - avg_cost
            
            f.write(f"\nFinancial Summary:\n")
            f.write(f"Average Revenue: CHF {avg_revenue:.2f}\n")
            f.write(f"Average Cost: CHF {avg_cost:.2f}\n")
            f.write(f"Average Profit: CHF {avg_profit:.2f}\n")
            f.write(f"Profit Margin: {(avg_profit/avg_revenue)*100:.1f}%\n\n")
            
            f.write("\nAverage Drink Orders:\n")
            for drink in total_drinks:
                avg = total_drinks[drink] / num_runs
                f.write(f"{drink}: {avg:.1f}\n")
            
            f.write("\nAverage Ingredient Requirements:\n")
            for ing in total_ingredients:
                avg = total_ingredients[ing] / num_runs
                # Check if ingredient is a Solid_Ingredient
                is_solid = any(isinstance(ingredient[0], SolidIngredient) and ingredient[0].name == ing 
                             for drink in self.cocktails.values() 
                             if isinstance(drink, (Cocktail, Shot))
                             for ingredient in drink.ingredients)
                f.write(f"{ing}: {avg:.1f} {'g' if is_solid else 'ml'}\n")
                
            f.write(f"\nAverage drinks per run: {sum(total_per_run)/len(total_per_run):.1f}\n") 
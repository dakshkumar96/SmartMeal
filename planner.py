# Meal Planner 

import numpy as np
from collections import defaultdict

# Full Recipe Database
RECIPES = [
    {
    "name": "Cauliflower Cheese",
    "cost": 3.00,
    "prep_time": 30,
    "diet_type": "vegetarian",
    "cuisine": "british",
    "skill_level": "intermediate",
    "allergies": ["dairy"],
    "nutrition": { "calories": 450, "protein": 15, "carbs": 25, "fat": 28 },
    "ingredients": [
      { "name": "cauliflower", "quantity": 200 },
      { "name": "dairy-free cheese", "quantity": 50 },
      { "name": "dairy-free milk", "quantity": 100 },
      { "name": "flour", "quantity": 1 },
      { "name": "nutritional yeast", "quantity": 1 }
    ]
  },
  {
    "name": "Pulled Pork Sandwich",
    "cost": 4.20,
    "prep_time": 20,
    "diet_type": "non-vegan",
    "cuisine": "american",
    "skill_level": "beginner",
    "allergies": [],
    "nutrition": { "calories": 600, "protein": 30, "carbs": 50, "fat": 25 },
    "ingredients": [
      { "name": "pulled pork", "quantity": 100 },
      { "name": "burger bun", "quantity": 1 },
      { "name": "bbq sauce", "quantity": 2 },
      { "name": "coleslaw", "quantity": 50 }
    ]
  },
  {
    "name": "Bean Burrito",
    "cost": 3.10,
    "prep_time": 20,
    "diet_type": "vegan",
    "cuisine": "mexican",
    "skill_level": "beginner",
    "allergies": [],
    "nutrition": { "calories": 520, "protein": 18, "carbs": 70, "fat": 14 },
    "ingredients": [
      { "name": "tortilla", "quantity": 1 },
      { "name": "refried beans", "quantity": 100 },
      { "name": "cooked rice", "quantity": 50 },
      { "name": "salsa", "quantity": 2 },
      { "name": "avocado", "quantity": 0.25 }
    ]
  },
  {
    "name": "Tuna Pasta Bake",
    "cost": 3.50,
    "prep_time": 25,
    "diet_type": "non-vegan",
    "cuisine": "italian",
    "skill_level": "intermediate",
    "allergies": ["fish", "dairy"],
    "nutrition": { "calories": 600, "protein": 35, "carbs": 65, "fat": 20 },
    "ingredients": [
      { "name": "pasta", "quantity": 80 },
      { "name": "chicken (substitute)", "quantity": 100 },
      { "name": "dairy-free cheese", "quantity": 50 },
      { "name": "dairy-free milk", "quantity": 100 },
      { "name": "flour", "quantity": 1 }
    ]
  },
     {
    "name": "Granola & Yogurt",
    "cost": 1.80,
    "prep_time": 5,
    "diet_type": "vegetarian",
    "cuisine": "american",
    "skill_level": "beginner",
    "allergies": ["dairy", "nuts"],
    "nutrition": { "calories": 350, "protein": 12, "carbs": 55, "fat": 10 },
    "ingredients": [
      { "name": "nut-free granola", "quantity": 50 },
      { "name": "dairy-free yogurt", "quantity": 100 },
      { "name": "honey", "quantity": 1 }
    ]
  },
  {
    "name": "Omelette",
    "cost": 2.10,
    "prep_time": 10,
    "diet_type": "vegetarian",
    "cuisine": "french",
    "skill_level": "beginner",
    "allergies": ["egg"],
    "nutrition": { "calories": 350, "protein": 20, "carbs": 5, "fat": 28 },
    "ingredients": [
      { "name": "chickpea flour", "quantity": 30 },
      { "name": "water", "quantity": 60 },
      { "name": "spinach", "quantity": 30 },
      { "name": "mushrooms", "quantity": 30 },
      { "name": "turmeric", "quantity": 0.5 }
    ]
  },
  {
    "name": "Bean Chili",
    "cost": 3.40,
    "prep_time": 30,
    "diet_type": "vegan",
    "cuisine": "mexican",
    "skill_level": "intermediate",
    "allergies": [],
    "nutrition": { "calories": 500, "protein": 20, "carbs": 60, "fat": 12 },
    "ingredients": [
      { "name": "black beans", "quantity": "150g" },
      { "name": "tomato paste", "quantity": "1 tbsp" },
      { "name": "onion", "quantity": "1 medium" },
      { "name": "chili powder", "quantity": "1 tsp" },
      { "name": "cooked rice", "quantity": "100g" }
    ]
  },
  {
    "name": "Beef Tacos",
    "cost": 4.80,
    "prep_time": 15,
    "diet_type": "non-vegan",
    "cuisine": "mexican",
    "skill_level": "beginner",
    "allergies": ["gluten"],
    "nutrition": { "calories": 600, "protein": 28, "carbs": 50, "fat": 30 },
    "ingredients": [
      { "name": "corn tortillas", "quantity": "2" },
      { "name": "ground beef", "quantity": "100g" },
      { "name": "lettuce", "quantity": "30g" },
      { "name": "diced tomatoes", "quantity": "30g" },
      { "name": "taco seasoning", "quantity": "1 tbsp" }
    ]
  },
  {
    "name": "Chicken Caesar Salad",
    "cost": 4.50,
    "prep_time": 15,
    "diet_type": "non-vegan",
    "cuisine": "american",
    "skill_level": "beginner",
    "allergies": ["dairy", "egg"],
    "nutrition": { "calories": 480, "protein": 28, "carbs": 20, "fat": 30 },
    "ingredients": [
      { "name": "chicken breast", "quantity": "150g" },
      { "name": "romaine lettuce", "quantity": "50g" },
      { "name": "dairy-free caesar dressing", "quantity": "2 tbsp" },
      { "name": "dairy-free croutons", "quantity": "20g" }
    ]
  },
  {
    "name": "Spaghetti Bolognese",
    "cost": 3.80,
    "prep_time": 25,
    "diet_type": "non-vegan",
    "cuisine": "italian",
    "skill_level": "beginner",
    "allergies": ["gluten"],
    "nutrition": { "calories": 600, "protein": 30, "carbs": 75, "fat": 22 },
    "ingredients": [
      { "name": "gluten-free spaghetti", "quantity": 80 },
      { "name": "ground beef", "quantity": 100 },
      { "name": "tomato sauce", "quantity": 100 },
      { "name": "onion", "quantity": 0.5 },
      { "name": "garlic", "quantity": 1 }
    ]
  },
  {
    "name": "Chicken Korma",
    "cost": 4.50,
    "prep_time": 30,
    "diet_type": "non-vegan",
    "cuisine": "indian",
    "skill_level": "intermediate",
    "allergies": [],
    "nutrition": { "calories": 620, "protein": 32, "carbs": 50, "fat": 28 },
    "ingredients": [
      { "name": "chicken breast", "quantity": 150 },
      { "name": "korma paste", "quantity": 2 },
      { "name": "coconut milk", "quantity": 100 },
      { "name": "onion", "quantity": 0.5 },
      { "name": "garlic", "quantity": 1 }
    ]
  },
  {
    "name": "Halloumi Wrap",
    "cost": 3.20,
    "prep_time": 10,
    "diet_type": "vegetarian",
    "cuisine": "mediterranean",
    "skill_level": "beginner",
    "allergies": ["dairy"],
    "nutrition": { "calories": 500, "protein": 20, "carbs": 40, "fat": 28 },
    "ingredients": [
      { "name": "vegan halloumi", "quantity": 80 },
      { "name": "tortilla wrap", "quantity": 1 },
      { "name": "lettuce", "quantity": 30 },
      { "name": "tomato", "quantity": 0.5 },
      { "name": "hummus", "quantity": 1 }
    ]
  },
  {
    "name": "Thai Green Curry",
    "cost": 4.80,
    "prep_time": 25,
    "diet_type": "non-vegan",
    "cuisine": "thai",
    "skill_level": "intermediate",
    "allergies": [],
    "nutrition": { "calories": 580, "protein": 28, "carbs": 60, "fat": 24 },
    "ingredients": [
      { "name": "chicken breast", "quantity": 150 },
      { "name": "thai green curry paste", "quantity": 2 },
      { "name": "coconut milk", "quantity": 100 },
      { "name": "bamboo shoots", "quantity": 50 },
      { "name": "basil", "quantity": 5 }
    ]
  },
  {
    "name": "Shakshuka",
    "cost": 3.20,
    "prep_time": 25,
    "diet_type": "vegetarian",
    "cuisine": "middle eastern",
    "skill_level": "intermediate",
    "allergies": ["egg"],
    "nutrition": { "calories": 480, "protein": 18, "carbs": 40, "fat": 25 },
    "ingredients": [
      { "name": "silken tofu", "quantity": 150 },
      { "name": "canned tomatoes", "quantity": 150 },
      { "name": "bell pepper", "quantity": 0.5 },
      { "name": "paprika", "quantity": 1 },
      { "name": "onion", "quantity": 0.5 }
    ]
  },
  {
    "name": "Falafel Plate",
    "cost": 3.00,
    "prep_time": 20,
    "diet_type": "vegan",
    "cuisine": "middle eastern",
    "skill_level": "intermediate",
    "allergies": [],
    "nutrition": { "calories": 450, "protein": 15, "carbs": 50, "fat": 18 },
    "ingredients": [
      { "name": "falafel", "quantity": 4 },
      { "name": "pita bread", "quantity": 1 },
      { "name": "hummus", "quantity": 2 },
      { "name": "mixed salad", "quantity": 50 },
      { "name": "tahini", "quantity": 1 }
    ]
  }
]


class MealPlanner:
    def __init__(self, recipes):
        self.recipes = recipes

    def matches(self, recipe, prefs):
        diet_type = recipe["diet_type"].lower()
        if prefs["diet"] and diet_type != prefs["diet"]:
            return False
        if prefs["cuisine"] and recipe["cuisine"].lower() != prefs["cuisine"]:
            return False
        if prefs["skill"] and recipe["skill_level"].lower() != prefs["skill"]:
            return False
        if recipe["prep_time"] > prefs["max_time"]:
            return False
        if any(a in [ra.lower() for ra in recipe["allergies"]] for a in prefs["allergies"]):
            return False
        return True

    def generate_meal_plan(self, prefs):
        total_meals = prefs["meals_per_day"] * 7
        budget_per_meal = prefs["budget"] / total_meals

        # Filter matching recipes
        valid = [r for r in self.recipes if self.matches(r, prefs)]
        if not valid:
            return None, {"error": "No recipes match your preferences."}

        # Sort by cost and pick within budget
        valid.sort(key=lambda r: r["cost"])
        selected, total_cost = [], 0.0
        for r in valid:
            if len(selected) >= total_meals:
                break
            if r["cost"] <= budget_per_meal:
                selected.append(r)
                total_cost += r["cost"]

        # If still short, pad with cheapest
        if len(selected) < total_meals:
            cheapest = valid[0]
            while len(selected) < total_meals:
                selected.append(cheapest)
                total_cost += cheapest["cost"]

        # Build grocery list (strings collected in lists)
        grocery = defaultdict(list)
        for r in selected:
            for ing in r["ingredients"]:
                grocery[ing["name"]].append(ing["quantity"])      

    

        result = {
            "meals": [
                {"name": r["name"], "cost": r["cost"], "prep_time": r["prep_time"]}
                for r in selected
            ],
            "grocery": dict(grocery),
            "cost_summary": {
                "total":    total_cost,
                "per_meal": total_cost / total_meals,
                "per_day":  total_cost / 7,

            }
        }

        return result, None


# 🍽️ Smart Meal - Intelligent Meal Planner

**Generate personalized weekly meal plans in seconds. Smart budget optimization, dietary preferences, and allergies in one click.**

A full-stack web application that reduces meal planning time from 45 minutes to 10 minutes through intelligent recipe filtering and budget optimization.

---

## ⚡ Quick Start

```bash
git clone https://github.com/dakshkumar96/smart-meal.git
cd smart-meal

# Install dependencies
pip install flask

# Start the server
python app.py

# Open http://localhost:5000
```

---

## ✨ Features

- **Budget Optimization**: Smart algorithm selects cost-effective recipes within your weekly budget
- **Multi-Criteria Filtering**: Diet (vegan/vegetarian/non-veg), cuisine, skill level, prep time, allergies
- **Automatic Grocery List**: Aggregates ingredients from selected meals with quantities
- **Cost Breakdown**: Total weekly cost, per-meal, per-day calculations
- **17+ Recipes**: Diverse cuisines (Italian, Mexican, Indian, Thai, etc.)
- **Responsive Design**: Dark theme UI, mobile-friendly interface

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, RESTful API
- **Frontend**: HTML5, CSS3, JavaScript (ES6+, async/await)
- **UI Framework**: Bootstrap 5.3.0
- **Data**: In-memory recipe database with intelligent filtering

---

## 💡 How It Works

1. **Input preferences**: Budget, meals per day, diet, cuisine, allergies, prep time
2. **Filtering**: Recipes matched against all constraints
3. **Optimization**: Budget-aware selection algorithm sorts by cost
4. **Generation**: Meal plan + auto-generated grocery list with cost summary

**Example**: £50 budget → 21-meal plan (3 meals × 7 days) with shopping list in seconds

---

## 📁 Project Structure

```
smart-meal/
├── app.py              # Flask API & routes
├── planner.py          # MealPlanner class & recipe database
├── templates/
│   └── index.html      # Frontend
└── static/
    └── script.js       # JavaScript logic
```

---

## 📡 API Endpoint

**POST** `/api/mealplan`

**Request:**
```json
{
  "budget": 50.00,
  "meals_per_day": 3,
  "max_time": 30,
  "diet": "vegetarian",
  "skill": "beginner",
  "cuisine": "italian",
  "allergies": ["dairy", "nuts"]
}
```

**Response:**
```json
{
  "meals": [{"name": "...", "cost": 3.10, "prep_time": 20}],
  "grocery": {"ingredient": [quantity, ...]},
  "cost_summary": {"total": 45.50, "per_meal": 2.17, "per_day": 6.50}
}
```

---

## 🎯 Key Technical Achievements

- **Algorithm Design**: Multi-constraint filtering with cost optimization
- **Data Structures**: `defaultdict` for efficient ingredient aggregation
- **Performance**: Generates meal plans in < 100ms
- **Client-Server**: Clean REST API separation
- **User Experience**: Real-time calculations, dynamic UI updates

---

## 👤 Author

**Daksh Kumar**
- **GitHub**: [@dakshkumar96](https://github.com/dakshkumar96)
- **LinkedIn**: [linkedin.com/in/dakshkumar96](https://linkedin.com/in/dakshkumar96)
- **Email**: dakshkumar2k2@gmail.com

---

Built with ❤️ to save time and money on meal planning

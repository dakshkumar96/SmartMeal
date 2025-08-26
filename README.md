# 🍽️ SmartMeal – AI-Powered Student Meal Planner

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)


A smart web app that helps students and busy people plan affordable, healthy meals based on their budget, diet, allergies, and cooking skills – with zero external APIs.

---

## ✨ What is SmartMeal?

SmartMeal is a **Python + Flask-based meal planner** that generates personalized weekly meal plans and grocery lists. It’s built for students and young professionals who want to eat well without spending too much time, money, or mental energy.

### You tell us:
- Your weekly budget (£)
- Meals per day
- Max prep time
- Diet (vegan, vegetarian, non-veg)
- Cooking skill level
- Allergies (e.g., nuts, dairy, gluten)
- Preferred cuisine (e.g., Italian, Indian)

### We give you:
- A full weekly meal plan 🗓️
- A consolidated grocery list 🛒
- Total cost breakdown 💰
- All recipes tailored to your needs

---

## 🛠️ Tech Stack

| Part           | Technology Used |
|----------------|-----------------|
| **Backend**    | Python 3, Flask |
| **Frontend**   | HTML5, Bootstrap 5, JavaScript |
| **Logic**      | Custom filtering and budgeting algorithm |
| **Data**       | In-memory recipe database (no external APIs) |
| **Styling**    | Custom CSS with dark mode |

---

## 🧠 How It Works

1. **User fills out** a simple web form with their preferences.
2. **JavaScript sends** the data to the Flask backend.
3. **Python filters** recipes based on diet, skill, time, allergies, and budget.
4. **Algorithm builds** a weekly plan, reusing affordable meals if needed.
5. **Grocery list is auto-generated** by combining ingredients from all meals.
6. **Results are displayed** in clean, responsive tables – no page reload needed.
   

### Prerequisites
- Python 3.8+
- pip

### 💡Why We Built This
We wanted to solve a real problem: students often struggle to eat healthy due to limited time, budget, and cooking experience. SmartMeal makes it easy to eat well without the stress – no subscriptions, no ads, just a simple tool that works.

### 🔮 Future Ideas
- Nutrition tracking (calories, protein)
- User accounts and saved preferences
- Recipe import/export
- Meal prep tutorials

📁 Project Structure
smartmeal/
├── app.py # Flask server and routes
├── planner.py # Core meal planning logic
├── static/
│ └── script.js # Frontend JavaScript
├── templates/
│ └── index.html # Main UI page
└── README.md

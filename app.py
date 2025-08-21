from flask import Flask, render_template, request, jsonify
from planner import MealPlanner, RECIPES

app = Flask(__name__)
planner = MealPlanner(RECIPES)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/mealplan', methods=['POST'])
def mealplan_api():
    prefs = request.json
    result, error = planner.generate_meal_plan(prefs)
    if error:
        return jsonify(error), 400
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

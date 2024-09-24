from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

class CalorieCounter:
    def __init__(self, api_key):
        self.api_url = 'https://api.calorieninjas.com/v1/nutrition?query={}'
        self.headers = {'X-Api-Key': api_key}

    def fetch_food_nutrition(self, query):
        try:
            response = self._make_api_request(query)
            if response.status_code == requests.codes.ok:
                data = response.json()
                if data and 'items' in data:
                    for item in data['items']:
                        if 'calories' in item:
                            return item['calories']
                else:
                    return None
            else:
                return None
        except Exception as e:
            return None

    def _make_api_request(self, query):
        try:
            response = requests.get(self.api_url.format(query), headers=self.headers)
            return response
        except Exception as e:
            return None

calorie_counter = CalorieCounter(api_key='UTFXq4wzICoSe7hsxeNoEPfLL1pNUSQKFPIixhOq')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    food_items = request.form.getlist('food_name')
    food_weights = request.form.getlist('food_weight')  
    total_calories = 0
    for food, weight in zip(food_items, food_weights):
        calorie_info = calorie_counter.fetch_food_nutrition(food)
        if calorie_info:
            total_calories += calorie_info * float(weight)
    return redirect(url_for('result', total_calories=total_calories))

@app.route('/result/<total_calories>')
def result(total_calories):
    total_calories = round(float(total_calories)/100, 2) 

    return render_template('result.html', total_calories=total_calories)

if __name__ == '__main__':
    app.run(debug=True)

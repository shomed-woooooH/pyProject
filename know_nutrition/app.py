from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    food_name = request.form['food_name']
    nutrition_info = fetch_nutrition_info(food_name)
    if nutrition_info:
        return render_template('result.html', nutrition_info=nutrition_info)
    else:
        return "Nutrition information not found for " + food_name

def fetch_nutrition_info(food_name):
    try:
        api_url = f"https://api.calorieninjas.com/v1/nutrition?query={food_name}"
        headers = {'X-Api-Key': 'UTFXq4wzICoSe7hsxeNoEPfLL1pNUSQKFPIixhOq'}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                return data['items']
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Error fetching data:", str(e))
    return None

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__, template_folder='templates')


YELP_API_KEY = "w4XPLQSvzwPfDEShcubKcTMD9bVnoNrgG1AbYLDdxLV9zRR6Haq8V7-RWlwsBtEJwTh8CC6oUOa6PpZaObpuer0id5D4gjBlLLrFOmyMicEeAgx8mWbAFW3IhHdNZHYx"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    zip_code = data['zip_code']
    restaurant_type = data['restaurant_type']

    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {
        "term": restaurant_type,
        "location": zip_code,
        "sort_by": "rating"
    }

    response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
    restaurants = response.json()["businesses"]

    three_months_ago = datetime.now() - timedelta(days=90)
    filtered_restaurants = []

    for restaurant in restaurants:
        if restaurant["rating"] >= 4:
            reviews_response = requests.get(f"https://api.yelp.com/v3/businesses/{restaurant['id']}/reviews", headers=headers)
            reviews = reviews_response.json()["reviews"]
            recent_ratings = [review for review in reviews if datetime.strptime(review["time_created"], "%Y-%m-%d %H:%M:%S") >= three_months_ago]
            recent_avg_rating = sum([review["rating"] for review in recent_ratings]) / len(recent_ratings) if recent_ratings else 0
            if recent_avg_rating >= 4:
                filtered_restaurants.append(restaurant)

    return jsonify(filtered_restaurants)


if __name__ == '__main__':
    app.run(debug=True)

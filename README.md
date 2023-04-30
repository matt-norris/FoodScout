# FoodScout
FreshBites

FoodScout is a web application designed to help users discover highly-rated restaurants in their area by filtering search results based on recent customer ratings. Users can enter their desired cuisine type and zip code, and FreshBites will display a curated list of nearby establishments with ratings above 4 stars from the past three months, ensuring they get the freshest and most reliable recommendations.

Getting Started

To run FoodScout locally, you'll need to have Python 3 and Flask installed on your machine.

Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/matt-norris/FoodScout.git
Install Flask and other dependencies:
bash
Copy code
pip install -r requirements.txt
Start the Flask development server:
bash
Copy code
export FLASK_APP=app.py
flask run
Open your web browser and navigate to http://localhost:5000 to access the FreshBites app.
Usage

To search for restaurants using FoodScout, follow these steps:

Enter the desired cuisine type in the "Type of Restaurant" field.
Enter the desired zip code in the "Zip Code" field.
Click the "Search" button.
Wait for the search results to appear.
Click on a restaurant box to view its Yelp page.
Contributing

If you would like to contribute to FoodScout, please submit a pull request with your proposed changes. I welcome contributions from the community and appreciate your help in making FoodScout a better application.

License

FoodScout is licensed under the MIT License. Please see the LICENSE file for more details.

Credits

FoodScout was created by Matt Norris. This project was inspired by Yelp and uses the Yelp Fusion API to retrieve restaurant data.

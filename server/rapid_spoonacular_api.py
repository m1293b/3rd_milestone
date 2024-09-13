import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"tags":"vegetarian,dessert","number":"1"}

headers = {
	"x-rapidapi-key": "1ae5d1a06bmsh8f531bacea26c61p136969jsn304d3133c079",
	"x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
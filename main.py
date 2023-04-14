import requests

api_key = "1546de173fe342dfbb3002ba48bfbeff"

url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-03-14&sortBy " \
      "=publishedAt&" \
      "apiKey=1546de173fe342dfbb3002ba48bfbeff"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print(article['url'])

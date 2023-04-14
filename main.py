import requests
from sent_email import send_email

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
body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + '\n' + article['description'] + 3*'\n'

body = body.encode('utf-8')
send_email(message=body)

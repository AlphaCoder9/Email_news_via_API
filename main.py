import requests
from sent_email import send_email

topic = "tesla"

api_key = "1546de173fe342dfbb3002ba48bfbeff"

# Note that date is mentioned you need to update to the current date.
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2023-03-15&sortBy " \
      "=publishedAt&" \
      "apiKey=1546de173fe342dfbb3002ba48bfbeff&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Tesla New's " + "\n"
for article in content['articles'][:20]:
    if (article['title'] is not None) and (article['description'] is not None):
        body = body + article['title'] + "\n"\
               + article['description'] \
               + "\n" + article['url'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)

import requests

url = "https://chompthis.com/api/product-search.php"

response = requests.request("GET", url)

print(response.text)

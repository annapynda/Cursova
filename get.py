import http.client

conn = http.client.HTTPSConnection("chompthis.com")

conn.request("GET", "/api/product-search.php?token=EXAMPLE&name=Starburst")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

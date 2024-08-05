import urllib.parse

encoded_url = "https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F0754%2F3727%2F7491%2Ffiles%2Ft-shirt-circles-blue.png%3Fv%3D1690003396&w=256&q=75"
decoded_url = urllib.parse.unquote(encoded_url)
print(decoded_url)

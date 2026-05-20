import requests
import sys
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) != 2:
    sys.exit("Too many arguments")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:

    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=5ccaf8224fa1aebdee9d7a3c5e6a372809b6d005d2e474436370b3df77109269')
    # print(type(r))
except requests.RequestException:
    print("Request failed!")

else:
    r = r.json()
    price = float(r['data']['priceUsd'])
    print(f"${n*price:,.4f}")
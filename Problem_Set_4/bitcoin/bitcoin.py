import requests
import sys

# API Key from https://pro.coincap.io/dashboard
API_KEY = "75d195d14424f52e86825e57be458b4d8a9644c01554563484232559fae39fc3"

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API_KEY)
    usd_price = float(response.json()["data"]["priceUsd"])
except requests.RequestException:
    print("There seems to be an API issue. Try again later.")
except KeyError:
    print("There seems to be an issue with API Key. Try generating another one.")
else:
    print(f"${round(n * usd_price, 4):,}")
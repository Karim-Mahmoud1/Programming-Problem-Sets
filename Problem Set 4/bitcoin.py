import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=3d93ffefe418c02869f0c7736dea9ad8695135d34bc6b4a60a9852381f327d9e"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException:
    sys.exit("API request failed")

json_data = response.json()

price_usd_string = json_data["data"]["priceUsd"]
usd_rate = float(price_usd_string)

total_cost = bitcoins * usd_rate
print(f"${total_cost:,.4f}")
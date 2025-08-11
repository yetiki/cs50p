"""Bitcoin is a form of digital currency, otherwise known as cryptocurrency.
Rather than rely on a central authority like a bank, Bitcoin instead relies
on a distributed network, otherwise known as a blockchain, to record
transactions.

Because there's demand for Bitcoin (i.e., users want it), users are willing
to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

This program:
- Expects the user to specify as a command-line argument the number of
Bitcoins, n, that they would like to buy. If that argument cannot be
converted to a float, the program exits via sys.exit with an error message.
- Queries the API for the CoinCap Bitcoin Price Index at
rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey - where YourApiKey
has been replaced with the actual API key obtained from your CoinCap
account dashboard, which returns a JSON object, among whose nested keys is
the current price of Bitcoin as a float.
- Outputs the current cost of n Bitcoins in USD to four decimal places,
using ',' as a thousands separator."""

import sys
import requests

API_KEY: str = ""
API_URL: str = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="+API_KEY

def main() -> None:
    # Read the number of bitcoins from command-line argument
    try:
        n_bitcoins: float = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    # Query the API for the CoinCap Bitcoin Price Index
    try:
        response = requests.get(API_URL)
        content: dict = response.json()
    except requests.RequestException:
        sys.exit("HTTPS request failed")
    
    bitcoin_price_index: float = float(content["data"]["priceUsd"])
    cost: float = n_bitcoins * bitcoin_price_index
    
    # Output the current cost of n bitcoins in USD
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()
import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
                        params={"apiKey": "YOUR_API_KEY"},
                        timeout=10
        )
        response.raise_for_status()

        data = response.json()
        rate = float(data["data"]["priceUsd"])

    except requests.RequestException :
        sys.exit("Could not retrieve Bitcoin price")

    amount = bitcoins * rate
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()









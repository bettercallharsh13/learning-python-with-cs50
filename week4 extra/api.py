import requests

def main():
    print("search the art institute of chicago!")
    artist = input("Artist: ")
    try:
            x = requests.get("https://api.artic.edu/api/v1/artworks/search", {"q": artist})
            x.raise_for_status()
    except requests.HTTPError:
         print("ERRORRRRRRR")
         return

    y = x.json()
    for i in y["data"]:
        print(f"* {i['title']}")





main()

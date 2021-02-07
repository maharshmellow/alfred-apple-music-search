import sys 
import json 
import requests

searchTerm = sys.argv[1:]

# docs: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/ 
api_url = "https://itunes.apple.com/search?term={}&entity=song&limit=20".format(searchTerm)

search_results = requests.get(api_url).json()["results"]
alfred_results = []

for item in search_results:
    # docs: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/ 
    result = {
        "title": item["trackName"],
        "subtitle": "{} - {}".format(item["artistName"], item["collectionName"]),
        "arg": item["trackViewUrl"].replace("https", "music").replace("/us/", "/ca/") + "&app=music",
        "autocomplete": "{} {}".format(item["trackName"], item["artistName"]),
        "icon": {
            "path": "./icon.png"
        }
    }
    
    alfred_results.append(result)

response = json.dumps({
    "items": alfred_results
})

sys.stdout.write(response)

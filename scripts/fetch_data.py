import requests
import json

def get_live_data(country="IN",limit =10 ):
    url = f"https://api.openaq.org/v2/measurements?country_id={country}&limit={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully!")
        print(json.dumps(data["results"][:3],indent=4))
    else:
        print("❌ Error! ❌ Failed to fetch data",response.status_code)
    

if __name__ == "__main__":
        get_live_data()

# get_live_data()

# https://api.openaq.org/v3/sensors/{sensors_id}/measurements/daily
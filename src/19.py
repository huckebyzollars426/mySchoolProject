import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get data. Status code: {response.status_code}")

# Example usage
url = "https://api.example.com/data"
data = fetch_data(url)

if data is not None:
    print("Data fetched successfully.")
    for item in data["items"]:
        print(item)
else:
    print("No data found.")

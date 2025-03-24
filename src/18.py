import requests
from bs4 import BeautifulSoup
import re

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to load {url}, status code: {response.status_code}"
    except Exception as e:
        return str(e)

def extract_url(html_content):
    url_pattern = re.compile(r"(https?://\S+)")
    urls = [line.strip() for line in html_content.split('\n') if url_pattern.search(line)]
    return list(set(urls))

def main():
    # Replace with your project's URL
    url = "https://example.com"
    print("Fetching and parsing HTML...")
    html_content = fetch_html(url)
    urls = extract_url(html_content)
    
    for url in urls:
        print(f"Extracting URLs from {url}")
        data = {"url": url}
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            print(f"Successfully extracted data from {url}!")
        else:
            print(f"Failed to extract data from {url}, status code: {response.status_code}")

if __name__ == "__main__":
    main()

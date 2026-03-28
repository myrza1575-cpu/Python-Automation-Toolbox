import requests
from bs4 import BeautifulSoup
import json

class AmazonScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5"
        }

    def fetch_product_details(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None

            soup = BeautifulSoup(response.content, "html.parser")
            
            product_data = {
                "title": self._get_title(soup),
                "price": self._get_price(soup),
                "rating": self._get_rating(soup)
            }
            return product_data
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return None

    def _get_title(self, soup):
        title = soup.find("span", attrs={"id": 'productTitle'})
        return title.text.strip() if title else "Title not found"

    def _get_price(self, soup):
        price = soup.find("span", class_="a-offscreen")
        return price.text if price else "Price not found"

    def _get_rating(self, soup):
        rating = soup.find("i", class_="a-icon-star")
        return rating.text if rating else "No rating"

if __name__ == "__main__":
    test_url = "https://www.amazon.com/dp/B08L5TNJHG"
    scraper = AmazonScraper()
    result = scraper.fetch_product_details(test_url)
    if result:
        print(json.dumps(result, indent=4))

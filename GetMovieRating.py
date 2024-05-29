from bs4 import BeautifulSoup
import requests

def get_rating(movie_url):

    link = movie_url

    response = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'a58c1747-b977-45bb-a504-8e68b99ffbbf',
            'url': link, 
        },
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    rating_div = soup.find('div', class_ = "sc-bde20123-2 gYgHoj")
    rating = rating_div.find('span', class_ = "sc-bde20123-1 iZlgcd").text

    return rating

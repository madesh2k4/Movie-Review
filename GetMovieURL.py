from bs4 import BeautifulSoup
import requests

def get_url(movie_name):

    formatted_movie_name = '+'.join(movie_name.split())

    link = f"https://www.imdb.com/find/?q={formatted_movie_name}&ref_=nv_sr_sm"

    response = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'a58c1747-b977-45bb-a504-8e68b99ffbbf',
            'url': link, 
        },
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    url_div = soup.find('div', class_ = "ipc-metadata-list-summary-item__tc")
    url_tag = url_div.find('a', class_ = "ipc-metadata-list-summary-item__t")
    url_href = url_tag.get('href')
    
    url = f"https://www.imdb.com{url_href}"

    return url

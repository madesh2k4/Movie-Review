from bs4 import BeautifulSoup
import requests

def get_plot_summary(movie_url):

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
    summary_div = soup.find('section', class_ = "sc-52d569c6-4 eAiKYC")
    summary = summary_div.find('span', class_ = "sc-6a7933c5-0 cUeLJx").text

    return summary

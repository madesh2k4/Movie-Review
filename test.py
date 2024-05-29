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

movie_name = input("Enter movie name: ")
link = get_url(movie_name)

response = requests.get(
    url='https://proxy.scrapeops.io/v1/',
    params={
        'api_key': 'a58c1747-b977-45bb-a504-8e68b99ffbbf',
        'url': link, 
    },
)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

def get_movie_title():

    title_div = soup.find('div', class_ = "sc-52d569c6-0 kNzJA-D")
    title = title_div.find('span', class_ = "sc-afe43def-1 fDTGTb").text

    return(title)

def get_rating():

    rating_div = soup.find('div', class_ = "sc-bde20123-2 gYgHoj")
    rating = rating_div.find('span', class_ = "sc-bde20123-1 iZlgcd").text

    return rating

def get_plot_summary():

    summary_div = soup.find('section', class_ = "sc-52d569c6-4 eAiKYC")
    summary = summary_div.find('span', class_ = "sc-6a7933c5-0 cUeLJx").text

    return summary


movie_title = get_movie_title()
movie_rating = get_rating()
movie_summary = get_plot_summary()

print()
print(movie_title)
print()
print("Movie Rating: ", movie_rating)
print()
print("Movie Plot Summary: ")
print(movie_summary)
print()

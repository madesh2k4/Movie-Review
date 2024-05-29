from bs4 import BeautifulSoup
import requests

import GetMovieURL

movie_name = input("Enter movie name: ")

link = GetMovieURL.get_url(movie_name)

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


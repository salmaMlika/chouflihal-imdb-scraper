from bs4 import BeautifulSoup
import requests
import numpy as np
from config import HEADERS


pages = np.arange(1, 7)

try:
    for page in pages:
        url = 'https://www.imdb.com/title/tt7151672/episodes/?season=' + str(page) + '&ref_=ttep'
        source = requests.get(url, headers=HEADERS)
        source.raise_for_status() 
        
        soup = BeautifulSoup(source.text, 'html.parser')  # parsing
        
        episods_list = soup.find('section', class_="sc-67c7a421-0 jsgvdx").find_all('article', class_="sc-983cc52-1 iReApi episode-item-wrapper")
        
        for episod in episods_list:
            ep_number_elem = episod.find('div', class_="ipc-title__text")
            if ep_number_elem:
                ep_text = ep_number_elem.text.strip()
                ep_number_full = ep_text.split('∙')[0].strip()   
                
                
                ep_season=ep_number_full.split('.')[0].strip()
                ep_number = ep_number_full.split('.')[1].strip()   
                
            ep_rating_elem = episod.find('span', class_="ipc-rating-star--rating")
            ep_rating = ep_rating_elem.text if ep_rating_elem else "Not Available"

            ep_raters_elem = episod.find('span', class_="ipc-rating-star--voteCount")
            ep_raters_number = ep_raters_elem.text.replace('(', '').replace(')', '') if ep_raters_elem else "Not Available"

            ep_brief = episod.find('div', class_="ipc-html-content-inner-div").text
            ep_date = episod.find('span', class_="sc-f2169d65-10 bYaARM").text

            print(ep_season)
except Exception as e:
    print(f"An error occurred: {e}")

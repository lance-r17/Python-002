import requests
from bs4 import BeautifulSoup as bs

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

user_agent = 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'

header = {}

cookie = {}

header['user-agent'] = user_agent
cookie['uuid'] = 'A7084B80CE4711EA84EECD6A0404A9092D9E3C73C67D46E594773750BA1370D2'

url = 'https://maoyan.com/films?showType=3'

mylist = []

def get_movie_top10(myurl):
    response = requests.get(myurl, headers=header, cookies=cookie)

    print(f'Status code: {response.status_code}')

    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'movie-item'}, limit=10):
        print('------------------------------')
        nameTag = tags.find_next('div', attrs={'class': 'movie-hover-title'})
        filmname = nameTag.find('span', attrs={'class': 'name'}).get_text()
        print(f'电影名称: {filmname}')

        typeTag = nameTag.find_next_sibling('div')
        filmtype = typeTag.contents[2].strip()
        print(f'电影类型: {filmtype}')

        dateTag = typeTag.find_next_sibling('div').find_next_sibling('div')
        releasedate = dateTag.contents[2].strip()
        print(f'上映时间: {releasedate}')

        mylist.append([filmname, filmtype, releasedate])

get_movie_top10(url)

import pandas as pd

movie = pd.DataFrame(data = mylist)

movie.to_csv(f'{dir_path}/movie.csv', encoding='utf8', index=False, header=['电影名称', '电影类型', '上映时间'])
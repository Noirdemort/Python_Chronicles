# from bs4 import BeautifulSoup as soup

# with open("./code_snippets/BeautifulSoup/simple.html",'r') as f:
#     psoup = soup(f, 'html.parser')

# print(psoup.prettify())

# # or we can use lxml parser  and prettify() on psoup
# articles = psoup.find_all('div', class_='article')
# print(len(articles))

import requests
from bs4 import BeautifulSoup as soup 

source =requests.get('http://coreyms.com').text 
psoup = soup(source, 'lxml')
print(psoup.prettify())

for article in psoup.find_all(article): # or findAll('div',{'class':'article'})
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div',class_='entry-content').p.text 
    print(summary)
    
    try:
        vid_src = article.sinf('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split("?")[0]
        yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    
    print(yt_link)
    print()

import bs4
from urllib.request import urlopen as uo 
from bs4 import BeautifulSoup as soup


my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
# my_url = 'https://twitter.com/picoiyer'

uCLient = uo(my_url)
page_html = uCLient.read()
uCLient.close()

# parsing html here
page_soup = soup(page_html,'html.parser')


#grab parts of page
containers = page_soup.findAll("div",{"class":"item-container"})
# print(page_soup.p, page_soup.h1)
# print(containers[0])

for container in containers:
    # print(container)
    brand = container.div.div.a.img["title"]
    title_container = container.findAll('a',{"class":"item-title"})
    # print(title_container)
    product_name = title_container[0].text
    shipping = container.findAll('li',{"class":"price-ship"})[0].text.strip()
    
    print("Brand: {}".format(brand))
    print("product Name: {}".format(product_name))
    print("Shipping: {}".format(shipping))
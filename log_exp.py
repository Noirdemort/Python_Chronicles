#from selenium import webdriver
#browser = webdriver.Firefox()
#
#browser.get('https://twitter.com/PicoIyer')
#
#elem = browser.find_element_by_css_selector('#stream-item-tweet-984428771812950016 > div.tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable.dismissible-content.original-tweet.js-original-tweet > div.content > div.js-tweet-text-container > p')
#
#elem1 = browser.find_element_by_css_selector('#stream-item-tweet-984074160421744646 > div.tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable.dismissible-content.original-tweet.js-original-tweet > div.content > div.js-tweet-text-container > p')
#
#for i in range(8):
#    elem2 = browser.find_element_by_class_name('TweetTextSize')
#    elem2 = browser.find_element_by_class_name('tweet')
#    print(elem2.text)
#print(elem.text)
#print(elem1.text)
#
#
#browser.quit()
import os
import pyautogui as pta
import time
#time.sleep(7)
#pta.click()
#dist = 300
#while dist>0:
#    pta.click()
#    pta.dragRel(dist,0,duration=0.3)
#    pta.click()
#    dist = dist - 40
#    pta.dragRel(0,dist,duration=0.3)
#    pta.click()
#    pta.dragRel(-dist,0,duration=0.3)
#    pta.click()
#    dist = dist - 60
#    pta.dragRel(0,-dist,duration=0.3)
#    pta.click()


# for pages
pta.click(x=253,y=863)

pta.typewrite("pages")
time.sleep(2)
pta.click(x=717,y=96)

time.sleep(5)

pta.click(x=467,y=302)
time.sleep(5)
pta.press('enter')
pta.typewrite(" auto print generation", interval=0.3)
pta.press('enter')
file = open("fpd.py",'r')
lines = file.readlines()
for i in lines:
    pta.typewrite(i)
file.close()


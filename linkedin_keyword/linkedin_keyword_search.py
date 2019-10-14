from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time as tm
import pandas as pd
import requests
import re
import random


df = pd.read_csv('Linkedin bot new links.csv')
a = list(df['url'])
b = a[0:20]
# b = ['https://www.linkedin.com/in/david-mayekawa-9284341/']
# b = ['https://www.linkedin.com/in/angel-amparo-40ba4553/']
# b = ['accommodating']
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

# csrf = client.get(url).cookies['csrftoken']

chrome_options = Options()
chrome_options.headless = False
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path = '/home/algoscale/Documents/Crawling/Linkedin/chromedriver')

browser.get("http://www.linkedin.com/uas/login")
    
# browser.maaximize_window()
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("wanetaDays@mail.com")
password.send_keys("HieDriUp4usW")
login_attempt = browser.find_element_by_class_name("from__button--floating").click()
tm.sleep(3)

cookies_list = browser.get_cookies()
# print(cookies_list)
cookies_dict = {}
for cookie in cookies_list:
    cookies_dict[cookie['name']] = cookie['value']
    
session_id = cookies_dict.get('JSESSIONID')
print(session_id)
    
data_undone=[]
ii = 0
# --------------------------------------------------------------------------------------    NEW CODE
for keyword in b:
#     tm.sleep(3)
    ii += 1
    print("------->>>>>>>>> {}".format(ii))
    # if ii == 2:
    #     break
#     browser.get('https://www.linkedin.com/feed/')
#     tm.sleep((random.randint(1, 5)) * 8)
    try:
        search_keywords   = browser.find_element_by_css_selector("#extended-nav-search input")
        search_keywords.send_keys(keyword)
        search_keywords.send_keys(Keys.RETURN)
        time.sleep((random.randint(1, 5)))
#         search_bar = browser.find_element_by_css_selector("nav-search-controls").click()
        see_all = browser.find_element_by_class_name('search-results__see-all-cards')
        print(see_all.length)
        tm.sleep(3)
        for i in see_all:
            try:
                see_all[i].click()
                print('see all clicked count',i)
            except:
                pass
        selected_urls = []
        try:
            user_url = soup.find_all("div", {"class":"actor-name"}, href=True)
            for i in website_url:
                selected_urls.append(user_url['href'])
        except Exception as e:
            print("--selected_urls--",e)
            selected_urls = None
            
        df = pd.DataFrame(selected_urls)
        df.to_csv('/home/algoscale/Documents/linkedin_keyword_temp.csv', index=False)
#         see_all = browser.find_element_by_class_name('search-results__see-all-cards flex-shrink-zero link-without-hover-visited mlA ember-view')
    except Exception as e:
        print(e)
        data_undone.append(search_keywords)
        continue
df.to_csv('/home/algoscale/Documents/linkedin_keyword_final.csv', index=False)

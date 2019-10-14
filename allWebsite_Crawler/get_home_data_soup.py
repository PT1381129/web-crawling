from bs4 import BeautifulSoup
import urllib
def clean_soup(soup):
    try:
        soup1 = soup.find('body')
        for i in range(len(soup1.find_all('script'))):
            try:
                soup1.script.decompose()
            except:
                pass
        for i in range(len(soup1.find_all('style'))):
            try:
                soup1.script.decompose()
            except:
                pass
        return soup1.text.strip()
    except:
        try:
            return soup.find('body').text.strip()
        except:
            return soup.text
        
def get_content(data):
    url = data[1]
    urls = ["https://"+url, "https://www."+url, "http://"+url, "http://www."+url, url]
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent' : "Magic Browser"})
            soup = BeautifulSoup(urllib.request.urlopen(req, timeout = 10))
            return (data[0], " ".join(clean_soup(soup).split()))
        except:
            pass
    return (data[0], "NULL")
        
    

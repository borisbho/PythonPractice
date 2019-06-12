import requests 
from bs4 import BeautifulSoup
import json
import datetime



url = "https://www.nytimes.com/"
r = requests.get(url)
now = datetime.datetime.now()
now = now.strftime('%A, %B %d, %Y  %I:%M %p')

r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

scripts = soup.find_all('script')
for script in scripts:
    if 'preloadedData' in script.text:
        jsonStr = script.text
        jsonStr = jsonStr.split('=', 1)[1].strip()
        jsonStr = jsonStr.rsplit(';', 1)[0]
        jsonObj = json.loads(jsonStr)


print ('%s\nHeadlines\n%s\n' %(url, now))
count = 1
for ele, v in jsonObj['initialState'].items():
    try:
        if v['headline'] and v['__typename'] == 'PromotionalProperties':
            print('Headline %s: %s' %(count, v['headline']))
            count += 1
    except:
        continue
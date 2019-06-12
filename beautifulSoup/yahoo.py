import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

site = 'http://www.nasdaq.com/symbol/nflx/news-headlines'
'''scrape the html of the site'''
html = requests.get(site).content
 
'''convert html to BeautifulSoup object'''
soup = BeautifulSoup(html , 'lxml')
 
'''get list of all links on webpage'''
links = soup.find_all('a')
 
'''Filter the list of urls to just the news articles'''
news_urls = [url for url in urls if '/article/' in url]
 
len(news_urls)
'''6'''
'''Set news_url equal to the 0th element in news_urls '''
news_url = news_urls[0]
 
'''Get HTML of the webpage associated with news_url'''
news_html = requests.get(news_url).content
 
'''Convert news_url to a BeautifulSoup object'''
news_soup = BeautifulSoup(news_html , 'lxml')
 
'''Use news_soup to get the text from all pargraphs on page'''
paragraphs = [par.text for par in news_soup.find_all('p')]
 
'''Lastly, join all text in the list above into a single string'''
news_text = '\n'.join(paragraphs)
len(urls)
'''226'''
'''Filter the list of urls to just the news articles'''
news_urls = [url for url in urls if '/article/' in url]
 
len(news_urls)
'''6'''
def scrape_news_text(news_url):
 
    news_html = requests.get(news_url).content
 
    '''convert html to BeautifulSoup object'''
    news_soup = BeautifulSoup(news_html , 'lxml')
 
    paragraphs = [par.text for par in news_soup.find_all('p')]
    news_text = '\n'.join(paragraphs)
 
    return news_text

def get_news_urls(links_site):
    '''scrape the html of the site'''
    resp = requests.get(links_site)
 
    if not resp.ok:
        return None
 
    html = resp.content
 
    '''convert html to BeautifulSoup object'''
    soup = BeautifulSoup(html , 'lxml')
 
    '''get list of all links on webpage'''
    links = soup.find_all('a')
 
    urls = [link.get('href') for link in links]
    urls = [url for url in urls if url is not None]
 
    '''Filter the list of urls to just the news articles'''
    news_urls = [url for url in urls if '/article/' in url]
 
    return news_urls

 
def scrape_all_articles(ticker , upper_page_limit = 5):
 
    landing_site = 'http://www.nasdaq.com/symbol/' + ticker + '/news-headlines'
 
    all_news_urls = get_news_urls(landing_site)
 
    current_urls_list = all_news_urls.copy()
 
    index = 2
 
    '''Loop through each sequential page, scraping the links from each'''
    while (current_urls_list is not None) and (current_urls_list != []) and \
        (index <= upper_page_limit):
 
        '''Construct URL for page in loop based off index'''
        current_site = landing_site + '?page=' + str(index)
        current_urls_list = get_news_urls(current_site)
 
        '''Append current webpage's list of urls to all_news_urls'''
        all_news_urls = all_news_urls + current_urls_list
 
        index = index + 1
 
    all_news_urls = list(set(all_news_urls))
 
    '''Now, we have a list of urls, we need to actually scrape the text'''
    all_articles = [scrape_news_text(news_url) for news_url in all_news_urls]
 
    return all_articles

nflx_articles = scrape_all_articles('nflx' , 5)
 
print(nflx_articles[0])
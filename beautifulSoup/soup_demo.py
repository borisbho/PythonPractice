from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AMD/community?p=AMD'

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
 
the_table = soup.find(class_='comments-list')
the_tds = the_table.find_all('div')
total_list = []
game_list = []

for element in the_tds:
    if element.find('a'):
        contents = element.find('a').contents[0]
    elif element.find('span'):
        contents = element.find('span').contents[0]
    else:
        contents=element.contents[0]

    contents = str(contents)
    contents = contents.replace('\n',"")
    game_list.append(contents)
    if len(game_list) == 7:
        print(game_list)
        total_list.append(game_list)
        game_list.clear()
import datetime as dt
from urllib.request import urlopen
from bs4 import BeautifulSoup


data =[]

titleData = []

def start():
    url = 'http://neumont.smartcatalogiq.com/2019-2020/Catalog/Academic-Calendar-2018-2019'

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    the_table = soup.find_all('tr')
    the_title = soup.find_all('h2')

    for title in the_title:
        title_list = title.find_all('h2')
        title_row = []
        for dd in title_list:
            title_row.append(dd.text)
        titleData.append(title.text)
    for row in the_table:
        row_list = row.find_all('td')
        dataRow = []
        for cell in row_list:
            dataRow.append(cell.text)
        data.append(dataRow)
    get_list()

def get_list():
    get_list = []
    text = titleData[0]
    get_list.append(text)
    for i in range(13):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[1]
    get_list.append(text)
    for i in range(13, 13+12):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[2]
    get_list.append(text)
    for i in range(25, 25+13):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[3]
    get_list.append(text)
    for i in range(38, 38+13):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[4]
    get_list.append(text)
    for i in range(51, 51+13):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[5]
    get_list.append(text)   
    for i in range(64, 64+12):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[6]
    get_list.append(text)
    for i in range(76, 76+13):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    text = titleData[7]
    get_list.append(text)
    for i in range(89, 89+13):
        content = data[i][0] + ' - ' + data[i][1]
        get_list.append(content)
    for data_val in get_list:
        file = open('list_data.txt', 'a')
        file.write(data_val + '\n')
        file.close()
        print(data_val)
    return get_list    

if __name__ == "__main__":
   start() 
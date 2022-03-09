from bs4 import BeautifulSoup
import requests

def web_page(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    col_1 = soup.find('div', class_='col-1')
    h1 = col_1.find_all('p')
    col_2 = soup.find('div', class_='col-2')
    h2 = col_2.find_all('p')
    namlik = h1[0].text.replace('Namlik:', '').strip()
    shamol = h1[1].text.replace('Shamol:', '').strip()
    bosim = h1[2].text.replace('Bosim:', '').strip()
    oy = h2[0].text.replace('Oy:', '').strip()
    quyosh_chiqishi = h2[1].text.replace('Quyosh chiqishi:', '').strip()
    quyosh_botishi = h2[2].text.replace('Quyosh botishi:', '').strip()
    news = soup.find_all('div', class_='news-item')
    day = soup.find('div', class_='current-day')
    temp = soup.find_all('strong')
    temp2 = soup.find_all('span')
    bugun = day.text.replace('Bugun,','').strip()
    title = soup.find('title').text.replace('- Obhavo.uz','').strip()
    print("{}".format(title))
    print("Havo harorati: {} {}".format(temp[0].text, temp2[3].text))
    print('Bugun: {}'.format(bugun), '\nNamlik:', namlik, '\nShamol:', shamol, '\nBosim:', bosim, '\nOy:', oy, '\nQuyosh chiqishi:', quyosh_chiqishi, '\nQuyosh botishi:', quyosh_botishi)
    print("\nYangiliklar:")
    i = 1
    for x in news:
        title = x.find('span').text.strip()
        print("{}. {}".format(i, title))
        i += 1
viloyat = input('Viloyat kiriting: ')
web_page('https://obhavo.uz/{}/'.format(viloyat))

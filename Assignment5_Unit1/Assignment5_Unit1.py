import requests, bs4

page = 0
current_year = "2022"
count = 0
All_id =[]
All_name =[]
while page !=3:
    url = f"https://www.cisa.gov/uscert/ncas/alerts/{current_year}?page={page}"
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    lists = soup.find_all('div', class_ = 'views-field views-field-title' )
    page = page + 1
    for list in lists:
        title = list.find('span', class_ = 'field-content').text

        csv_id = title[0:9]
        All_id.append(csv_id)

        csv_name = title[11:]
        All_name.append(csv_name)

for id in All_id:
    re_id = id.lower()
    link = f"https://www.cisa.gov/uscert/ncas/alerts/{re_id}]"
    work = requests.get(link)
    work.raise_for_status()
    re_soup = bs4.BeautifulSoup(work.text, 'html.parser')
    csv_lists = re_soup.find_all('div', class_="region region-content")
    for csv_list in csv_lists:
        date = csv_list.find('div', class_="submitted meta-text")
        print(date)




import requests, bs4

page = 0
current_year = str(input())
count = 0
while page !=3:
    url = f"https://www.cisa.gov/uscert/ncas/alerts/{current_year}?page={page}"
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    lists = soup.find_all('div', class_ = 'views-field views-field-title' )
    page = page + 1
    for list in lists:
        count += 1
print(count)


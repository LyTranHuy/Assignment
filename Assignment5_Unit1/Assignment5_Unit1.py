import requests, bs4
from csv import writer
page = 0
current_year = "2022"
count = 0
All_id =[]
All_name =[]
All_date =[]
All_revise =[]
All_link = []
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
    link = f"https://www.cisa.gov/uscert/ncas/alerts/{re_id}"
    All_link.append(link)
    work = requests.get(link)
    work.raise_for_status()
    re_soup = bs4.BeautifulSoup(work.text, 'html.parser')
    csv_lists = re_soup.find_all('div', class_="region region-content")
    for csv_list in csv_lists:
        item = csv_list.find('div', class_="submitted meta-text").text
        all_line = item.strip()
        date_revise = all_line.split(' ')
        length = len(date_revise)
        date = date_revise[3] + " " + date_revise[4] + " " + date_revise[5]
        All_date.append(date)
        revise = date_revise[length-3] + " " + date_revise[length-2] + " " + date_revise[length-1]
        All_revise.append(revise)

length = len(All_id)
with open('All_alert.csv', 'w') as f:
    thewriter = writer(f)
    header = ['Alert ID', 'Alert Name', 'Release Date', 'Last revised', 'Alert Link']
    thewriter.writerow(header)
    for i in range (0, length-1):
        Alert_ID = All_id[i]
        ALert_Name = All_name[i]
        Release_Date = All_date[i]
        Last_revised = All_revise[i]
        Alert_Link = All_link[i]
        info = [Alert_ID, ALert_Name, Release_Date, Last_revised, Alert_Link]
        thewriter.writerow(info)
    




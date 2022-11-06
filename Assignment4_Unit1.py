import requests, os, bs4

url = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'               # starting url
os.makedirs('D:\\TestCode\\Assignment\\Assignment4_Unit1\\img', exist_ok=True)    # store img in images
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
     # Find the URL of the comic image.
    imgElem = soup.select('img')
    if imgElem == []:
        print('Could not find image.')
    else:
        imgUrl = 'https:' + imgElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (imgUrl))
        res = requests.get(imgUrl)
        res.raise_for_status()
        # Save the image to .
        imageFile = open(os.path.join('D:\\TestCode\\Assignment\\Assignment4_Unit1\\img', os.path.basename(imgUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales' + prevLink.get('href')
print('Done.')
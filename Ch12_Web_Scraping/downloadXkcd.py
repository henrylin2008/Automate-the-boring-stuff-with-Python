#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()          # Throw an exception and end of the program if something went wrong with the download

    soup = bs4.BeautifulSoup(res.text)    # BeautifulSoup object from the text of the downloaded page

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')      # get <image> element inside <div id ="comic">
                                                                            #   <img src ="xxx">
    if comicElem == []:                        # return message when return a blank list
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')   # get the URL of the image
        # TODO: Download the image.
        print('Downloading image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    # xkcd = local folder
    # os.path.basename(comicUrl) returns the last part of the URL ('heartbleed_explanation.png')
    # wb: write binary mode

    for chunk in res.iter_content(100000): # Loop over return value in chunk of 100000 bytes each
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    # 'a[rel="prev"]' identifies the <a> element with the rel attribute set to prev, and use this <a> element's href
    # attribute to ge tht previous comic's URL, which gets stored in url
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')

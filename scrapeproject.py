from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import http.client
import csv

main = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"

paths = []
songs_list = []

def getTableLinks(my_url):
    html = urlopen(my_url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    tabledata = bsObj.find("table", {"class":"wikitable"}).find_all("tr")
    for table in tabledata:
        try:
            links = table.find("a")
            if 'href' in links.attrs:
                # creates a list of paths to follow
                paths.append(links.attrs['href'])
        except:
            pass

# creates URLs to top 100 pages
for n in range(2010, 2015):
    mainLinkList = getTableLinks(main + str(n))

def get_tr_list(bsObj):
    global tr_list
    try:
        tr_list = bsObj.find("table", {"class":"infobox vevent"}).find_all("tr")
    except AttributeError as e:
        return e
        pass

def getTitle(bsObj):
    titles = tr_list[0].find("th", {"class":"summary"})
    for title in titles:
        try:
            return title
        except AttributeError as e:
            return e

def getArtist(bsObj):
    try:
        artists = tr_list[2].find("a").next_sibling.next_siblings
        for artist in artists:
            try:
                return artist.text
            except AttributeError as e:
                return e
                pass
    except AttributeError as e:
        return e
        pass

def getGenre(bsObj):
    try:
        for tr in tr_list:
            try:
                if tr.get_text().find('Genre') > -1 :
                    return tr.td.text.strip()
            except AttributeError as e:
                return e
                pass
    except AttributeError as e:
        return e
        pass

def getLabel(bsObj):
    try:
        for tr in tr_list:
            try:
                if tr.get_text().find('Label') > -1 :
                    return tr.td.text.strip()
            except AttributeError as e:
                return e
                pass
    except AttributeError as e:
        return e
        pass

def getWriter(bsObj):
    try:
        for tr in tr_list:
            try:
                if tr.get_text().find('Writer(s)') > -1 :
                    return tr.td.text.strip()
            except AttributeError as e:
                return e
                pass
    except AttributeError as e:
        return e
        pass

def getProducer(bsObj):
    try:
        for tr in tr_list:
            try:
                if tr.get_text().find('Producer(s)') > -1 :
                    return tr.td.text.strip()
            except AttributeError as e:
                return e
                pass
    except AttributeError as e:
        return e
        pass

# goes to every link and finds all the things
def goToLink(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    get_tr_list(bsObj)

    title = getTitle(bsObj)
    artist = getArtist(bsObj)
    genre = getGenre(bsObj)
    label = getLabel(bsObj)
    writer = getWriter(bsObj)
    producer = getProducer(bsObj)
    songs = [title, artist, genre, label, writer, producer]
    songs_list.append(songs)

    with open('songs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in songs_list:
            writer.writerow(row)

# goes through list of paths to get info from each page
for i in paths:
    goToLink("https://en.wikipedia.org" + i)

import requests
from bs4 import BeautifulSoup
import random
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
}

tags = ['Rock', 'Electronic', 'Pop', 'Folk%2C+World%2C+%26+Country', 'Jazz', 'Funk+%2F+Soul', 'Hip+Hop', 'Classical', 'Latin', 'Reggae', 'Stage+%26+Screen', 'Blues', 'Non-Music', 'Children%27s', 'Brass+%26+Military']

database = {}


for tag in tags:
    print("Downloading YTs for tag: %s" % tag)
    
    if tag in tags:
        resp = requests.get("https://www.discogs.com/search/?sort=want%2Cdesc&genre_exact="+tag,headers=headers)
        print("Status code of a try finding albums: ", resp.status_code)

        soup = BeautifulSoup(resp.text, "html.parser")

        
    links = []


    for link in soup.find_all('a', class_="search_result_title"):
        links.append(link.get('href'))


    discogs = 'https://www.discogs.com'
    yt = []


    def play(url):
        try:
            #time.sleep(20)
            soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
            x = soup.find(id = "youtube_player_placeholder")["data-video-ids"]
            y = x.split(',')
            yt.append(y)
        except TypeError:
            print("Code 429 or album {0} has no videos.".format(url))


    for link in links:
        play(discogs+link)
    
    
    for video_id in yt:
            try:
                print(random.choice(video_id))
            except IndexError:
                print("There's no videos in this genre to display")
    
    
    database[tag] = yt


d = json.dumps(database)

with open("C:\pytong\projekt1_cylson\database.txt", "w") as f:
    f.write(d)




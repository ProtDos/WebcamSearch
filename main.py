import requests
from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.CloudScraper()
#meG = scraper.get("https://www.webcamtaxi.com/en/search.html?searchword=germany&ordering=newest&searchphrase=all&limit=0")

def get_links(res):
    al = []
    data = res.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        a = link.get('href')
        if a not in al:
            al.append(a)
    print("-"*50)
    return al

def get_img(res):
    al = []
    data = res.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('img'):
        #print(link)
        a = link.get('src')
        if a not in al:
            al.append(a)
    print("-"*50)
    return al

city = input("Enter location: ").replace(" ", "")

# 1
res = scraper.get(f"https://www.webcamtaxi.com/en/search.html?searchword={city}&ordering=newest&searchphrase=all&limit=0")
#get_links(res)
#print(res.text)
# 2
res2 = requests.get(f"https://worldcam.live/en/search?q={city}")
al = get_links(res2)
for item in al:
    if str(item).startswith("/en/webcam/"):
        print("https://worldcam.live" + item)
    

# 3
res3 = requests.get(f"https://worldcam.eu/search?q={city}")
al = get_links(res3)
b = ["https://worldcam.eu/webcams/europe/united-kingdom",
"https://worldcam.eu/webcams/poland",
"https://worldcam.eu/webcams/africa",
"https://worldcam.eu/webcams/north-america",
"https://worldcam.eu/webcams/south-america",
"https://worldcam.eu/webcams/australia-oceania",
"https://worldcam.eu/webcams/asia",
"https://worldcam.eu/webcams/poles",
"https://worldcam.eu/webcams/europe"]
for item in al:
    if item.startswith("/webcams/"):
        if "https://worldcam.eu" + item in b:
            pass
        else:
            print("https://worldcam.eu" + item)

# 4
print("-"*50)
res = requests.get("https://searchapi.earthcam.com/search.php/?term=germany").json()
for ite in res["item_data"]:
    print(ite["db_url"])


# 5
res5 = requests.get(f"https://www.globocam.de/webcams/suche?q={city}")
al = get_links(res5)
#print(al)
for item in al:
    if item.startswith("/webcams/"):
        print("https://www.globocam.de" + item)

# 6
res6 = requests.get(f"http://www.opentopia.com/search.php?q={city}")
al = get_img(res6)
#print(al)
for item in al:
    if item.startswith("http://images.opentopia.com/cams/"):
        # http://images.opentopia.com/cams/15373/medium.jpg
        # http://www.opentopia.com/webcam/15373
        idd = item.split("/")[4]
        print("http://www.opentopia.com/webcam/" + idd)
        pass 

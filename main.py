import requests
from bs4 import BeautifulSoup
import cloudscraper
import urllib.parse

scraper = cloudscraper.CloudScraper()

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

city = urllib.parse.quote_plus(input("Enter location (e.g. city): "))
print(city)

# 1
res = scraper.get(f"https://www.webcamtaxi.com/en/search.html?searchword={city}&ordering=newest&searchphrase=all&limit=0")

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
res = requests.get(f"https://searchapi.earthcam.com/search.php/?term={city}").json()
for ite in res["item_data"]:
    if str(ite["db_url"]).startswith("http"):
        print(ite["db_url"])
    else:
        pass


# 5
res5 = requests.get(f"https://www.globocam.de/webcams/suche?q={city}")
al = get_links(res5)
badd = ["https://www.globocam.de/webcams/melden",
"https://www.globocam.de/webcams/suche",
"https://www.globocam.de/webcams/search/reset",
f"https://www.globocam.de/webcams/suche?page=2&search={city}"]
for item in al:
    if item.startswith("/webcams/"):
        if "https://www.globocam.de" + item in badd:
            pass
        else:
            print("https://www.globocam.de" + item)

# 6
res6 = requests.get(f"http://www.opentopia.com/search.php?q={city}")
al = get_img(res6)
#print(al)
for item in al:
    if item.startswith("http://images.opentopia.com/cams/"):
        idd = item.split("/")[4]
        print("http://www.opentopia.com/webcam/" + idd)
        pass 
print("-"*50)
def get_city(city):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
    res = requests.get(
        f"http://insecam.org/en/bycity/{city}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycity/{city}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print(ip)
get_city(str(city))
print("-"*50)
print("[i] Finished...")

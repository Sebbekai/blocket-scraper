import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def parse_ads(url):
    soup = fetch_page(url)
    return soup.findAll("article")


def get_latest_ad(url):
    ads = parse_ads(url)
    latest_ad = ads[0]
    ad_name = latest_ad.find_all("span")
    ad_url = latest_ad.find_all("a", href=True)

    return ad_name[0].text, ad_name[1].text, ad_url[2]["href"]


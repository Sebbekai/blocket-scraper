import time
import scraping.blocket as scrape
import constants
import notification.discord as disc

prev_ad_link = ""

print("scraper is running!")
while True:
    time.sleep(30)
    print("Checked for ads at: ", time.strftime("%H:%M:%S", time.localtime()))
    title, price, link = scrape.get_latest_ad(constants.BLOCKET_URL + constants.BLOCKET_SEARCH_PARAMS)
    if link != prev_ad_link:
        disc.send_notification(title, price, constants.BLOCKET_URL + link, constants.DISC_URL)
        prev_ad_link = link



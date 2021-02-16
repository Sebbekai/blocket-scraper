import requests
import constants


def send_notification(title, price, link, disc):
    data = {
        "content": f"New Add has arrived!  Snoooooze and you lose mother fucker!\n"
                   f"Title: {title} \n**price: {price}** \nLink: {link}"
    }
    #not gracefully handling if this fails.. but dont care
    requests.post(constants.DISC_URL, json=data)

import os
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')


_CHAT_ID = os.getenv('CHAT_ID')
_BETA_ID = os.getenv('BETA_ID')
_BOT_TOKEN = os.getenv('BOT_TOKEN')
_DEBUG = os.getenv('DEBUG')

def is_not_full(text):
    if text == "This beta is full.":
        return False
    else:
        return True 

if __name__ == "__main__":  
    
    if not _CHAT_ID:
        logging.error("You need to set your Telegram chat id to let this program run!")
        exit(2)

    if not _BETA_ID:
        logging.error("You need to set the id of the beta you want to check to let this program run!")
        exit(2)

    if not _BOT_TOKEN:
        logging.error("You need to set your Telegram bot token to let this program run!")
        exit(2)

    _URL = 'https://testflight.apple.com/join/' + _BETA_ID

    logging.info("Starting checking free slot now!")

    if not _DEBUG:
        logging.info("Debug is disabled. You will see only messages when there are free slots or errors. You can define DEBUG environment variable to enable it.")
    else:
        logging.getLogger().setLevel(logging.DEBUG)

    while True:
        now = datetime.now()
        try:
            page = requests.get(_URL)
        
            soup = BeautifulSoup(page.content, "html.parser")
            beta_status_div = soup.find("div", class_="beta-status")
            result =  beta_status_div.find("span").text

            if is_not_full(result):
                loggin.info("Join now!")
                logging.debug("Sending Telegram message.")
                
                text = "Join now on . \n" + _URL 
                token = _BOT_TOKEN
                chat_id = _CHAT_ID
                url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
                results = requests.get(url_req)
                logging.debug("Message sent: " + results.json()['ok'])
                
                break
            else:
                logging.debug("Still full!")
        except requests.exceptions.ConnectionError:
            logging.error("Failure! Check internet connection. Retrying...")
        except:
            logging.error("Cannot check due an exception. Retrying...")

        time.sleep(5)

    logging.warning("Closing because there was at least 1 free slot")
    exit(0)

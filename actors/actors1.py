import config

import dramatiq
import requests
import time
from random import uniform


@dramatiq.actor(store_results=True)
def count_words(url):
    time.sleep(uniform(1, 3))

    response = requests.get(url)
    count = len(response.text.split(" "))
    return count

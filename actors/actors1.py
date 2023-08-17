import config

import dramatiq
import requests


@dramatiq.actor
def count_words(url):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")


@dramatiq.actor
def slow_count_words(url):
    import time

    time.sleep(5)

    count_words(url)

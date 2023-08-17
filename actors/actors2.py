import dramatiq
from periodiq import cron

import config


@dramatiq.actor(store_results=True)
def add(a, b):
    return a + b


@dramatiq.actor(store_results=True)
def mul(a, b):
    return a * b


@dramatiq.actor(periodic=cron("* * * * *"))
def heartbeat():
    print("I am alive")

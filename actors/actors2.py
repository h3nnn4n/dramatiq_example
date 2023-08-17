import dramatiq
from periodiq import cron

import config


@dramatiq.actor
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


@dramatiq.actor
def mul(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")


@dramatiq.actor(periodic=cron("* * * * *"))
def heartbeat():
    print("I am alive")

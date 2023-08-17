import config

from actors import actors1, actors2


if __name__ == '__main__':
    urls = [
        "https://news.ycombinator.com",
        "https://xkcd.com",
        "https://rabbitmq.com",
    ]
    [actors1.count_words.send(url) for url in urls]
    [actors1.slow_count_words.send(url) for url in urls]

    [actors2.add.send(a, b) for a, b in zip(range(10), range(10, 20))]
    [actors2.mul.send(a, b) for a, b in zip(range(10), range(10, 20))]

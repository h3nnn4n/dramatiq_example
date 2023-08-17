import config

from actors import actors1, actors2


if __name__ == "__main__":
    urls = [
        "https://news.ycombinator.com",
        "https://xkcd.com",
        "https://rabbitmq.com",
        "https://dramatiq.io",
        "https://lobste.rs",
    ]
    results = [actors1.count_words.send(url) for url in urls]

    total = 0
    for item in results:
        word_count = item.get_result(block=True)
        result = actors2.add.send(total, word_count)
        total += result.get_result(block=True)
        print(f"{total=}")

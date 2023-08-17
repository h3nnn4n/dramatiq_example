# Dramatiq Example

This repo contains a "complete" example on setting
[dramatiq](https://dramatiq.io/) and
[periodiq](https://gitlab.com/jeverling/periodiq) using redis as a broker and
results backend.

Actors are defined in `actors.actors1` and `actors.actors2`.
`config` handles dramatiq and redis initialization.
`create_jobs` enqueues some jobs to run.

`create_jobs` will iterate over a list of websites, counting how many words it
has on the landing page. The counts are stored in the result backend. The
results are then iterated over using another actor to get to total word count.


# Usage

- Make sure python >3.10 is installed

- Make sure poetry is installed

- Install deps with `poetry install`

- Start actors with:
```bash
poetry run dramatiq --processes=1 --threads=2 config:broker actors.actors1 actors.actors2
```

- Start the scheduler with:
```bash
poetry run periodiq actors.actors1 actors.actors2
```

- Create some test jobs with:
```bash
poetry run python create_jobs.py
```

# LICENSE

Part of the code was taken from the official dramatiq documentation at
[dramatiq.io](dramatiq.io).

See [LICENSE](LICENSE)

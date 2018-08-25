[![Build Status](https://travis-ci.com/critical-path/py-subscribers.svg?branch=master)](https://travis-ci.com/critical-path/py-subscribers) [![Coverage Status](https://coveralls.io/repos/github/critical-path/py-subscribers/badge.svg)](https://coveralls.io/github/critical-path/py-subscribers)

## py-subscribers v1.0.0

py-subscribers is a util that retrieves a list of subscribers (watchers) for a given GitHub user and repo.


## Dependencies

py-subscribers requires Python and the pip package.  It also requires the following packages for usage and testing.

__Usage__:
- click
- requests

__Testing__:
- coveralls
- pylint
- pytest
- pytest-cov
- radon
- responses


## Installing py-subscribers with test cases and testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command and the `--editable` option.

```
sudo pip install --editable .[test]
```


## Installing py-subscribers without test cases or testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command.

```
sudo pip install .
```


## Using py-subscribers with long options

To retrieve a list of subscribers for all repos associated with a given user, run `subscribers` with the `--user` option.

```
subscribers --user <user>
```

To retrieve a list of subscribers associated with a given user and a given repo, run `subscribers` with the `--user` and `--repo` options.

```
subscribers --user <user> --repo <repo>
```

To write the retrieved list of subscribers to disk, run `subscribers` with the `--write` option.

```
subscribers --user <user> --write
subscribers --user <user> --repo <repo> --write
```


## Using py-subscribers with short options

To retrieve a list of subscribers for all repos associated with a given user, run `subscribers` with the `-u` option.

```
subscribers -u <user>
```

To retrieve a list of subscribers associated with a given user and a given repo, run `subscribers` with the `-u` and `-r` options.

```
subscribers -u <user> -r <repo>
```

To write the retrieved list of subscribers to disk, run `subscribers` with the `-w` option.

```
subscribers -u <user> -w
subscribers -u <user> -r <repo> -w
```


## Testing py-subscribers after installation

1. Run `radon` with the `mi` command and the `--show` option.

```
radon mi --show subscribers
```

2. Run `pylint`.

```
pylint subscribers
```

3. Run `pytest` with the `-vv`, `--cov`, and `--cov-report` options.

```
pytest -vv --cov --cov-report=term-missing
```


## Note

py-subscribers makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.

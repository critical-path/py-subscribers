[![Build Status](https://travis-ci.com/critical-path/py-subscribers.svg?branch=master)](https://travis-ci.com/critical-path/py-subscribers)

## py-subscribers v1.0.0

py-subscribers is a util that retrieves a list of subscribers (watchers) for a given GitHub user and repo.


## Dependencies

py-subscribers requires Python as well as the pip, click, requests, pylint, pytest, pytest-cov, and responses packages.


## Installing py-subscribers with test cases and testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip with the install command and the --editable option.

```
sudo pip install --editable .[test] .
```


## Installing py-subscribers without test cases or testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip with the install command.

```
sudo pip install .
```


## Using py-subscribers with long options

To retrieve a list of subscribers for all repos associated with a given user, run subscribers with the --user option.

```
subscribers --user <user>
```

To retrieve a list of subscribers associated with a given user and a given repo, run subscribers with the --user and --repo options.

```
subscribers --user <user> --repo <repo>
```

To write the retrieved list of subscribers to disk, run subscribers with the --write option.

```
subscribers --user <user> --write
subscribers --user <user> --repo <repo> --write
```


## Using py-subscribers with short options

To retrieve a list of subscribers for all repos associated with a given user, run subscribers with the -u option.

```
subscribers -u <user>
```

To retrieve a list of subscribers associated with a given user and a given repo, run subscribers with the -u and -r options.

```
subscribers -u <user> -r <repo>
```

To write the retrieved list of subscribers to disk, run subscribers with the -w option.

```
subscribers -u <user> -w
subscribers -u <user> -r <repo> -w
```


## Testing py-subscribers after installation

1. Run pylint.

```
pylint subscribers
```

2. Change to the tests directory.

```
cd ./tests
```

3. Run pytest with the -vv, --cov, --cov-report, and --cov-config options.

```
pytest -vv --cov=subscribers --cov-report=term-missing --cov-config=.coveragerc
```


## Note

py-subscribers makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.

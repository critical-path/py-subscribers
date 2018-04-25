from json import dumps

from os import (
    remove,
    stat
)

from subscribers.subscribers_lib import (
    get_repos,
    get_subscribers_for_all_repos,
    get_subscribers_for_one_repo,
    write_results
)

from responses import (
    activate,
    add,
    GET
)

from constants import (
    API,
    FILENAME_USER,
    FILENAME_USER_REPO,
    SUBSCRIBERS,
    REPO0,
    REPO1,
    REPOS,
    REPO0_AND_SUBSCRIBERS,
    REPOS_AND_SUBSCRIBERS,
    USER
)


@activate
def test_get_repos():
    endpoint = "{}/users/{}/repos".format(API, USER)

    add(
        method=GET,
        url=endpoint,
        body=dumps(REPOS),
        status=200
    )

    repos = get_repos(API, USER)

    assert repos == ["test-repo0", "test-repo1"]


@activate
def test_get_subscribers_for_one_repo():
    endpoint = "{}/repos/{}/{}/subscribers".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    subscribers = get_subscribers_for_one_repo(API, USER, REPO0)

    assert subscribers == REPO0_AND_SUBSCRIBERS


@activate
def test_get_subscribers_for_all_repos():
    repos_endpoint = "{}/users/{}/repos".format(API, USER)

    add(
        method=GET,
        url=repos_endpoint,
        body=dumps(REPOS),
        status=200
    )

    subscribers_endpoint0 = "{}/repos/{}/{}/subscribers".format(API, USER, REPO0)

    add(
        method=GET,
        url=subscribers_endpoint0,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    subscribers_endpoint1 = "{}/repos/{}/{}/subscribers".format(API, USER, REPO1)

    add(
        method=GET,
        url=subscribers_endpoint1,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    repos = get_repos(API, USER)
    subscribers = get_subscribers_for_all_repos(API, USER, repos)

    assert subscribers == REPOS_AND_SUBSCRIBERS


def test_write_results_user_repo():
    write_results(user=USER, repo=REPO0, subscribers=dumps(REPO0_AND_SUBSCRIBERS))

    assert stat(FILENAME_USER_REPO)
    remove(FILENAME_USER_REPO)


def test_write_results_user_no_repo():
    write_results(user=USER, subscribers=dumps(REPOS_AND_SUBSCRIBERS))

    assert stat(FILENAME_USER)
    remove(FILENAME_USER)

from json import dumps

from os import (
    remove,
    stat
)

from click.testing import CliRunner

from subscribers.cli import get_subscribers

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


def test_cli_help():
    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "--help"
        ]
    )

    assert result.exit_code == 0
    assert "Usage" in result.output


def test_cli_no_user_no_repo_no_write():
    runner = CliRunner()

    result = runner.invoke(
        get_subscribers
    )

    assert result.exit_code != 0
    assert "Missing" in result.output


@activate
def test_cli_user_repo_no_write_long():
    endpoint = "{}/repos/{}/{}/subscribers".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "--user", USER,
            "--repo", REPO0
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_SUBSCRIBERS, indent=2) + "\n"


@activate
def test_cli_user_repo_no_write_short():
    endpoint = "{}/repos/{}/{}/subscribers".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "-u", USER,
            "-r", REPO0
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_SUBSCRIBERS, indent=2) + "\n"


@activate
def test_cli_user_no_repo_no_write_long():
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

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "--user", USER
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_SUBSCRIBERS, indent=2) + "\n"


@activate
def test_cli_user_no_repo_no_write_short():
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

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "-u", USER
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_SUBSCRIBERS, indent=2) + "\n"


@activate
def test_cli_user_repo_write_long():
    endpoint = "{}/repos/{}/{}/subscribers".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "--user", USER,
            "--repo", REPO0,
            "--write"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_SUBSCRIBERS, indent=2) + "\n"
    assert stat(FILENAME_USER_REPO)
    remove(FILENAME_USER_REPO)


@activate
def test_cli_user_repo_write_short():
    endpoint = "{}/repos/{}/{}/subscribers".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(SUBSCRIBERS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "-u", USER,
            "-r", REPO0,
            "-w"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_SUBSCRIBERS, indent=2) + "\n"
    assert stat(FILENAME_USER_REPO)
    remove(FILENAME_USER_REPO)


@activate
def test_cli_user_no_repo_write_long():
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

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "--user", USER,
            "--write"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_SUBSCRIBERS, indent=2) + "\n"
    assert stat(FILENAME_USER)
    remove(FILENAME_USER)


@activate
def test_cli_user_no_repo_write_short():
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

    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "-u", USER,
            "-w"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_SUBSCRIBERS, indent=2) + "\n"
    assert stat(FILENAME_USER)
    remove(FILENAME_USER)


def test_cli_repo_no_user_long():
    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "--repo", REPO0
        ]
    )

    assert result.exit_code != 0
    assert "Missing" in result.output


def test_cli_repo_no_user_short():
    runner = CliRunner()

    result = runner.invoke(
        get_subscribers,
        [
            "-r", REPO0
        ]
    )

    assert result.exit_code != 0
    assert "Missing" in result.output

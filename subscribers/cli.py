"""The command-line interface for py-subscribers."""


from json import dumps

from click import (
    command,
    echo,
    option
)

from subscribers.lib import (
    get_repos,
    get_subscribers_for_one_repo,
    get_subscribers_for_all_repos,
    write_results
)


API = "https://api.github.com"


@command()
@option("--user", "-u", required=True, type=str, help="User of interest")
@option("--repo", "-r", type=str, help="Repo of interest")
@option("--write", "-w", is_flag=True, help="Write results to disk")
def get_subscribers(user=None, repo=None, write=False):
    """Util that retrieves a list of subscribers (watchers) for a given GitHub user and repo."""

    if (user is not None) and (repo is not None):
        subscribers = get_subscribers_for_one_repo(API, user, repo)

    if (user is not None) and (repo is None):
        repos = get_repos(API, user)
        subscribers = get_subscribers_for_all_repos(API, user, repos)

    subscribers = dumps(subscribers, indent=2)

    if write:
        write_results(user=user, repo=repo, subscribers=subscribers)

    echo(subscribers)


if __name__ == "__main__":
    get_subscribers()

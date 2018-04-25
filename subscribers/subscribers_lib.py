from requests import get


def get_repos(api, user):
    """Get list of all repos for a given user.

    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    The parameters help to form the API endpoint.
    """

    repos = []

    endpoint = "{}/users/{}/repos".format(api, user)
    response = get(endpoint)
    response_body = response.json()

    for element in response_body:
        repo = element["name"]
        repos.append(repo)

    return repos


def get_subscribers_for_one_repo(api, user, repo):
    """Get list of all subscribers for a given repo.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    repos : str
        The repo of interest.

    The parameters help to form the API endpoint.
    """

    subscribers = {}

    endpoint = "{}/repos/{}/{}/subscribers".format(api, user, repo)
    response = get(endpoint)
    response_body = response.json()
    subscribers[repo] = response_body

    return subscribers


def get_subscribers_for_all_repos(api, user, repos):
    """Get list of all subscribers for a given list of repos.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    repos : list
        The repos of interest.

    The parameters help to form the API endpoint.
    """

    subscribers = {}

    for repo in repos:
        endpoint = "{}/repos/{}/{}/subscribers".format(api, user, repo)
        response = get(endpoint)
        response_body = response.json()
        subscribers[repo] = response_body

    return subscribers


def write_results(user=None, repo=None, subscribers=None):
    """Write results to disk.

    Parameters
    ---------
    user : str
      The user of interest.

    repo : str, optional
      The repo of interest.

    subscribers : str in JSON format
      The subscribers associated with the user and repo.

    The parameters help to form the filename.
    """

    if user and repo:
        filename = "subscribers-{0}-{1}.json".format(user, repo)
    elif user and not repo:
        filename = "subscribers-{0}.json".format(user)

    with open(filename, "w") as output:
        output.write(subscribers)

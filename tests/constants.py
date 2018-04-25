API = "https://api.github.com"

USER = "test-user"

REPO0 = "test-repo0"

REPO1 = "test-repo1"

REPOS = [
  {
    "name": "test-repo0"
  },
  {
    "name": "test-repo1"
  }
]

SUBSCRIBERS = [
  {
    "id": "1000"
  },
  {
    "id": "1001"
  }
]

REPOS_AND_SUBSCRIBERS = {
  "test-repo0":
    [
      {
        "id": "1000"
      },
      {
        "id": "1001"
      }
    ],

  "test-repo1":
    [
      {
        "id": "1000"
      },
      {
        "id": "1001"
      }
    ]
}

REPO0_AND_SUBSCRIBERS = {
  "test-repo0":
    [
      {
        "id": "1000"
      },
      {
        "id": "1001"
      }
    ]
}

FILENAME_USER = "subscribers-test-user.json"

FILENAME_USER_REPO = "subscribers-test-user-test-repo0.json"

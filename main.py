import asyncio

from github_api.github_client.client import BaseGitHubClient
from github_api.github_client.auth import TokenAuth


if __name__ == "__main__":
    # Tests:
    your_token = ""
    token = TokenAuth(token=your_token)
    github = BaseGitHubClient(token=token.token)
    asyncio.run(github.get(url="/user"))

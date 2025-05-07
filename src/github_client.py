from github import Github
from src.config import GITHUB_TOKEN

g = Github(GITHUB_TOKEN)

def get_repo_updates(repo_full_name):
    repo = g.get_repo(repo_full_name)
    return {
        "commits": repo.get_commits()[:5],
        "issues": repo.get_issues(state="open")[:5],
        "pulls": repo.get_pulls(state="open")[:5]
    }

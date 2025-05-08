from github import Github
from config import GITHUB_TOKEN

g = Github(GITHUB_TOKEN)

def get_repo_updates(repo_full_name):
    repo = g.get_repo(repo_full_name)

    # 获取最新 release（可能为 None）
    try:
        latest_release = repo.get_latest_release()
        release_info = {
            "tag_name": latest_release.tag_name,
            "name": latest_release.title or latest_release.name or "",
            "published_at": str(latest_release.published_at),
            "body": latest_release.body or ""
        }
    except:
        release_info = None

    return {
        "commits": list(repo.get_commits())[:5],
        "issues": list(repo.get_issues(state="open"))[:5],
        "pulls": list(repo.get_pulls(state="open"))[:5],
        "release": release_info
    }

from subscription import list_subscriptions
from github_client import get_repo_updates

def fetch_all_updates():
    updates = {}
    for repo in list_subscriptions():
        try:
            updates[repo] = get_repo_updates(repo)
        except Exception as e:
            print(f"⚠️ 拉取 {repo} 失败: {e}")
            updates[repo] = {}  # 标记为失败
    return updates


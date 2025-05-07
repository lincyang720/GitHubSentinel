from src.subscription import list_subscriptions
from src.github_client import get_repo_updates

def fetch_all_updates():
    updates = {}
    for sub in list_subscriptions():
        updates[sub.repo] = get_repo_updates(sub.repo)
    return updates

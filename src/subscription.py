import json
import os
from config import SUBSCRIPTIONS_FILE

def _load_subscriptions():
    if not os.path.exists(SUBSCRIPTIONS_FILE):
        return []
    with open(SUBSCRIPTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_subscriptions(repos):
    with open(SUBSCRIPTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2)

def list_subscriptions():
    return _load_subscriptions()

def add_subscription(repo):
    repos = _load_subscriptions()
    if repo not in repos:
        repos.append(repo)
        _save_subscriptions(repos)
        return True
    return False

def remove_subscription(repo):
    repos = _load_subscriptions()
    if repo in repos:
        repos.remove(repo)
        _save_subscriptions(repos)
        return True
    return False

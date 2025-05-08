from github import Github
from config import GITHUB_TOKEN
from subscription import list_subscriptions
from datetime import datetime
import os

g = Github(GITHUB_TOKEN)




def get_repo_daily_status(repo_full_name: str) -> str:
    repo = g.get_repo(repo_full_name)
    issues = repo.get_issues(state="open")
    pulls = repo.get_pulls(state="open")
    commits = repo.get_commits()

    today = datetime.utcnow().date().isoformat()
    content = f"# 📌 Daily Update for `{repo_full_name}` - {today}\n\n"

    content += "## 🔨 Recent Commits\n"
    for commit in commits[:5]:
        sha = commit.sha[:7]
        msg = commit.commit.message.split("\n")[0]
        author = commit.author.login if commit.author else "unknown"
        content += f"- [{sha}] {msg} (by @{author})\n"

    content += "\n## 🐞 Open Issues\n"
    for issue in issues[:10]:
        if issue.pull_request is None:
            content += f"- #{issue.number} {issue.title} ({issue.user.login})\n"

    content += "\n## 🔁 Open Pull Requests\n"
    for pr in pulls[:10]:
        content += f"- #{pr.number} {pr.title} ({pr.user.login})\n"

    return content

def export_all_repos_daily_md() -> list[str]:
    """
    导出所有订阅仓库的 issues/PR 为 Markdown 文件。
    返回成功写入的文件路径列表。
    """
    today = datetime.utcnow().date().isoformat()
    os.makedirs("reports/daily", exist_ok=True)

    exported_files = []

    for repo in list_subscriptions():
        try:
            content = get_repo_daily_status(repo)
            filename = f"{repo.replace('/', '_')}_{today}.md"
            filepath = os.path.join("reports/daily", filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ 导出日报：{filepath}")
            exported_files.append(filepath)
        except Exception as e:
            print(f"⚠️ 拉取 {repo} 失败：{e}")

    return exported_files



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

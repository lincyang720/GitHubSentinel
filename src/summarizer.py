def summarize_updates(updates):
    summary = ""

    for repo, data in updates.items():
        summary += f"\n## {repo}\n"

        # 更新数量统计
        summary += f"- 🟢 Commits: {len(data['commits'])}\n"
        summary += f"- 🐞 Issues: {len(data['issues'])}\n"
        summary += f"- 🔁 Pull Requests: {len(data['pulls'])}\n"

        # 版本发布信息
        release = data.get("release")
        if release:
            summary += "\n### 📦 Latest Release\n"
            summary += f"Repository: {repo}\n"
            summary += f"Latest Version: {release['tag_name']}\n"
            summary += f"Release Name: {release['name']}\n"
            summary += f"Published at: {release['published_at']}\n"
            summary += f"Release Notes:\n{release['body']}\n"
        else:
            summary += "\n❌ No Release information found.\n"

    return summary

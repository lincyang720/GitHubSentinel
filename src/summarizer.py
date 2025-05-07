def summarize_updates(updates):
    summary = ""
    for repo, data in updates.items():
        summary += f"\n## {repo}\n"
        summary += f"- 🟢 Commits: {len(data['commits'])}\n"
        summary += f"- 🐞 Issues: {len(data['issues'])}\n"
        summary += f"- 🔁 Pull Requests: {len(data['pulls'])}\n"
    return summary

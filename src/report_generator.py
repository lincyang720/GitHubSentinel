def generate_markdown_report(summary):
    with open("reports/latest_report.md", "w", encoding="utf-8") as f:
        f.write("# GitHub Sentinel 报告\n")
        f.write(summary)

import argparse
import shlex
from subscription import list_subscriptions, add_subscription, remove_subscription
from fetcher import fetch_all_updates
from summarizer import summarize_updates
from report_generator import generate_markdown_report, summarize_all_daily_reports
from github_client import export_all_repos_daily_md
from scheduler import start_scheduler
from config import OPENAI_API_KEY

def get_parser():
    parser = argparse.ArgumentParser(prog="github-sentinel", description="GitHub Sentinel CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="列出所有订阅").set_defaults(func=cmd_list)

    p_add = subparsers.add_parser("add", help="添加订阅仓库")
    p_add.add_argument("repo")
    p_add.set_defaults(func=cmd_add)

    p_rm = subparsers.add_parser("remove", help="移除订阅仓库")
    p_rm.add_argument("repo")
    p_rm.set_defaults(func=cmd_remove)

    subparsers.add_parser("fetch", help="生成 GitHub 项目简要更新报告").set_defaults(func=cmd_fetch)
    subparsers.add_parser("report", help="一键生成完整日报（导出+GPT汇总）").set_defaults(func=cmd_report)
    subparsers.add_parser("start", help="启动后台调度器").set_defaults(func=cmd_start)
    subparsers.add_parser("help", help="查看所有命令帮助").set_defaults(func=cmd_help)

    return parser

def cmd_help(args=None):
    print("""
GitHub Sentinel 是一款开源的 AI 工具，帮助你自动追踪 GitHub 仓库更新，并生成结构化项目日报。

命令列表：
  list                         查看当前所有订阅的仓库
  add <owner/repo>             添加订阅的 GitHub 仓库（如：add langchain-ai/langchain）
  remove <owner/repo>          移除订阅仓库
  fetch                        拉取 GitHub 最新提交/PR/Issue，生成简要文本报告（不使用 GPT）
  report                       一键生成完整项目日报（导出 issues/PR 并用 GPT 汇总成正式日报）
  start                        启动后台定时调度器，定期拉取并汇总日报
  help                         查看本帮助信息
  exit / quit                  退出程序

示例：
  add openai/openai-python
  fetch
  report
""")


def cmd_list(args):
    for r in list_subscriptions():
        print(f"- {r}")

def cmd_add(args):
    if add_subscription(args.repo):
        print(f"✅ 成功添加订阅：{args.repo}")
    else:
        print(f"⚠️ 已存在：{args.repo}")

def cmd_remove(args):
    if remove_subscription(args.repo):
        print(f"✅ 成功移除订阅：{args.repo}")
    else:
        print(f"⚠️ 不存在：{args.repo}")

def cmd_fetch(args):
    updates = fetch_all_updates()
    if not any(updates.values()):
        print("❌ 所有仓库更新失败")
        return
    summary = summarize_updates(updates)
    generate_markdown_report(summary)
    print("✅ 简报已生成：reports/latest_report.md")

def cmd_report(args):
    files = export_all_repos_daily_md()
    if not files:
        print("❌ 所有仓库拉取失败，跳过汇总。")
        return
    summarize_all_daily_reports(files, api_key=OPENAI_API_KEY)

def cmd_start(args):
    print("🔁 启动调度器中...")
    start_scheduler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("🛑 已退出")
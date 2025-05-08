import argparse
import shlex
from subscription import list_subscriptions, add_subscription, remove_subscription
from fetcher import fetch_all_updates
from summarizer import summarize_updates
from scheduler import start_scheduler
import os
from report_generator import summarize_all_daily_reports
from github_client import export_all_repos_daily_md
from config import OPENAI_API_KEY



# 全局解析器
parser = argparse.ArgumentParser(prog="github-sentinel", description="GitHub Sentinel - 开源仓库监控助手")
subparsers = parser.add_subparsers(dest="command")

# list
subparsers.add_parser("list", help="列出所有订阅仓库").set_defaults(func=lambda args: print_subscriptions())

# add <repo>
p_add = subparsers.add_parser("add", help="添加一个订阅仓库")
p_add.add_argument("repo")
p_add.set_defaults(func=lambda args: print_result(add_subscription(args.repo), f"添加成功：{args.repo}", f"仓库已存在：{args.repo}"))

# remove <repo>
p_rm = subparsers.add_parser("remove", help="移除一个订阅仓库")
p_rm.add_argument("repo")
p_rm.set_defaults(func=lambda args: print_result(remove_subscription(args.repo), f"移除成功：{args.repo}", f"仓库不存在：{args.repo}"))

# fetch
# subparsers.add_parser("fetch", help="立即拉取更新并生成报告").set_defaults(func=lambda args: fetch_and_report())

subparsers.add_parser("report", help="生成完整项目日报（导出 + GPT 汇总）").set_defaults(func=lambda args: report_handler())

# start
subparsers.add_parser("start", help="启动后台定时调度器，定期拉取并生成完整日报").set_defaults(func=lambda args: start_handler())



def print_help():
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




# 工具函数
def print_subscriptions():
    repos = list_subscriptions()
    if not repos:
        print("📭 当前没有任何订阅仓库")
    else:
        print("📦 当前订阅仓库：")
        for r in repos:
            print(f" - {r}")

def print_result(success, ok_msg, fail_msg):
    print(f"✅ {ok_msg}" if success else f"⚠️ {fail_msg}")

def report_handler():
    files = export_all_repos_daily_md()
    if not files:
        print("❌ 所有仓库拉取失败，跳过汇总。")
        return
    summarize_all_daily_reports(files, api_key=OPENAI_API_KEY)


def start_handler():
    print("🚀 GitHub Sentinel 定时器启动中（按 Ctrl+C 退出）")
    start_scheduler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n🛑 GitHub Sentinel 已手动停止")

def summarize_daily_handler():
    api_key = OPENAI_API_KEY
    if not api_key:
        print("❌ OPENAI_API_KEY 环境变量未设置。请在 .env 或环境中配置。")
        return
    summarize_all_daily_reports(api_key=api_key)

def export_daily_handler():
    export_all_repos_daily_md()



# 启动交互式 CLI
def main():
    print("🚀 GitHub Sentinel CLI 已启动，输入 help 查看命令，输入 exit / quit 退出。")
    print_help()  # 🆕 启动时展示帮助
    while True:
        try:
            raw = input("github-sentinel> ").strip()
            if not raw:
                continue

            if raw.lower() in {"exit", "quit"}:
                print("👋 再见！")
                break

            if raw.lower() == "help":
                print_help()
                continue

            # 所有其它命令走 argparse + shlex
            args = parser.parse_args(shlex.split(raw))
            if hasattr(args, "func"):
                args.func(args)
            else:
                parser.print_help()

        except Exception as e:
            print(f"⚠️ 命令执行失败：{e}")


if __name__ == "__main__":
    main()

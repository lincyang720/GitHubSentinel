import argparse
import shlex
from subscription import list_subscriptions, add_subscription, remove_subscription
from fetcher import fetch_all_updates
from summarizer import summarize_updates
from report_generator import generate_markdown_report
from scheduler import start_scheduler

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
subparsers.add_parser("fetch", help="立即拉取更新并生成报告").set_defaults(func=lambda args: fetch_and_report())

# start
subparsers.add_parser("start", help="启动后台调度器").set_defaults(func=lambda args: start_and_block())

def print_help():
    print("""
GitHub Sentinel 是一款开源的 AI 工具，用于自动追踪和汇总你订阅的 GitHub 仓库的更新信息。

命令列表：
  list                         查看当前所有订阅的仓库
  add <owner/repo>             添加订阅的 GitHub 仓库（例如：add langchain-ai/langchain）
  remove <owner/repo>          移除订阅仓库
  fetch                        立即拉取订阅仓库的更新，并生成 Markdown 报告
  start                        启动后台定时拉取任务（使用配置中设定的间隔）
  help                         查看本帮助信息
  exit / quit                  退出程序

示例：
  add openai/openai-python
  remove langchain-ai/langchain
  fetch
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

def fetch_and_report():
    print("🔍 正在拉取订阅仓库更新...")
    updates = fetch_all_updates()
    if not any(updates.values()):
        print("❌ 所有仓库更新失败，报告未生成。")
        return
    summary = summarize_updates(updates)
    generate_markdown_report(summary)
    print("✅ 报告已生成：reports/latest_report.md")

def start_and_block():
    print("🕒 启动调度器（每隔固定间隔自动拉取）")
    start_scheduler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n🛑 GitHub Sentinel 已停止")

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

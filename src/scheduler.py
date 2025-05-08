from apscheduler.schedulers.background import BackgroundScheduler
from fetcher import fetch_all_updates
from summarizer import summarize_updates
from report_generator import generate_markdown_report
from config import FETCH_INTERVAL

def scheduled_job():
    print("\n⏳ [Scheduler] 自动拉取仓库更新中...")
    updates = fetch_all_updates()
    if not any(updates.values()):
        print("❌ 所有仓库更新失败，跳过摘要和报告生成。\n")
        return
    summary = summarize_updates(updates)
    generate_markdown_report(summary)
    print("✅ [Scheduler] 报告已生成\n")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, "interval", seconds=FETCH_INTERVAL)
    scheduler.start()
    print(f"🕒 后台调度器已启动，每 {FETCH_INTERVAL} 秒执行一次拉取")

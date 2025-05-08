from apscheduler.schedulers.background import BackgroundScheduler
from report_generator import summarize_all_daily_reports
from github_client import export_all_repos_daily_md
from config import FETCH_INTERVAL, OPENAI_API_KEY

def run_export_and_summary():
    files = export_all_repos_daily_md()
    if not files:
        print("❌ 所有仓库拉取失败，跳过汇总。")
        return
    summarize_all_daily_reports(files, api_key=OPENAI_API_KEY)

def scheduled_job():
    print("\n⏳ [Scheduler] 正在执行自动日报任务...")
    try:
        run_export_and_summary()
        print("✅ [Scheduler] 自动日报生成完毕\n")
    except Exception as e:
        print(f"❌ [Scheduler] 执行失败：{e}\n")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, "interval", seconds=FETCH_INTERVAL)
    scheduler.start()
    print(f"🕒 后台调度器已启动，每 {FETCH_INTERVAL} 秒执行一次")

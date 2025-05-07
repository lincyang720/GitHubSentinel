from apscheduler.schedulers.background import BackgroundScheduler
from src.fetcher import fetch_all_updates
from src.summarizer import summarize_updates
from src.report_generator import generate_markdown_report

def job():
    updates = fetch_all_updates()
    summary = summarize_updates(updates)
    generate_markdown_report(summary)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", seconds=86400)
    scheduler.start()

from src.scheduler import start_scheduler
from src.database import init_db

if __name__ == "__main__":
    init_db()
    start_scheduler()
    print("✅ GitHub Sentinel 启动中... Ctrl+C 退出")
    import time
    while True:
        time.sleep(1)

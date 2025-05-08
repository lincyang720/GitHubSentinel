import json
import os

CONFIG_PATH = "config.json"

if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError("❌ config.json 文件未找到")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

# GitHub Token
GITHUB_TOKEN = CONFIG.get("github_token")
if not GITHUB_TOKEN:
    raise ValueError("❌ config.json 中缺少 github_token")

# OpenAI Token ✅ 新增
OPENAI_API_KEY = CONFIG.get("openai_api_key")
if not OPENAI_API_KEY:
    raise ValueError("❌ config.json 中缺少 openai_api_key")

# 通知设置（保留）
NOTIFICATION_SETTINGS = CONFIG.get("notification_settings", {})
NOTIFY_EMAIL = NOTIFICATION_SETTINGS.get("email")
SLACK_WEBHOOK_URL = NOTIFICATION_SETTINGS.get("slack_webhook_url")

# 仓库订阅文件路径
SUBSCRIPTIONS_FILE = CONFIG.get("subscriptions_file", "subscriptions.json")

# 更新间隔（秒）
FETCH_INTERVAL = CONFIG.get("update_interval", 86400)

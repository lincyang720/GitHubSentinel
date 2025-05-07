# 🚀 GitHub Sentinel

**GitHub Sentinel** is an open-source, AI-powered agent that automatically tracks, summarizes, and reports the latest updates from your subscribed GitHub repositories. Built for developers and project managers who want to stay informed without manually checking every repo.

> "Never miss a commit, issue, or pull request again."

---

## ✨ Features

- ✅ Subscribe to any public GitHub repository
- 🔁 Periodically fetch commits, issues, pull requests, and releases
- ✍️ Summarize updates (LLM-friendly)
- 📧 Send notifications via email or webhook (Slack support coming soon)
- 📄 Generate Markdown/HTML project update reports
- 🧱 Modular and extensible architecture

---

## 🖼️ Preview

![screenshot](https://your-screenshot-url.com) <!-- 替换为项目图示 -->

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/github-sentinel.git
cd github-sentinel
```

### 2.Create a virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3.Install dependencies

```
pip install -r requirements.txt
```

### 4.Configure environment variables

```
GITHUB_TOKEN=your_github_pat
EMAIL_SENDER=your_email@example.com
EMAIL_PASSWORD=your_email_password
DATABASE_URL=sqlite:///sentinel.db
FETCH_INTERVAL=86400
```

### 5.Getting Started

```
python main.py
```


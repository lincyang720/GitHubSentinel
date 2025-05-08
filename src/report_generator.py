import os
from datetime import datetime
from llm import LLMClient
import openai


def summarize_all_daily_reports(markdown_paths: list[str], api_key: str, output_dir="reports/daily_summary"):
    """
    汇总指定 Markdown 文件路径列表，调用 GPT 并生成结构化日报。
    """
    os.makedirs(output_dir, exist_ok=True)
    llm = LLMClient(api_key=api_key)

    for path in markdown_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw_md = f.read()

            filename = os.path.basename(path).replace(".md", "")
            repo_part, date_str = filename.rsplit("_", 1)
            repo_name = repo_part.replace("_", "/")

            summary = llm.summarize_markdown(raw_md, repo_name, date_str)

            output_path = os.path.join(output_dir, f"{repo_part}_{date_str}.md")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(summary)

            print(f"✅ 汇总完成：{output_path}")

        except Exception as e:
            error_path = os.path.join(output_dir, f"{repo_part}_{date_str}.error.txt")
            with open(error_path, "w", encoding="utf-8") as ef:
                ef.write(f"❌ 汇总失败：{type(e).__name__} — {e}")
            print(f"⚠️ 汇总失败：{path} — {type(e).__name__}: {e}")



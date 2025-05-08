import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt

class LLMClient:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    @retry(wait=wait_random_exponential(min=2, max=10), stop=stop_after_attempt(3))
    def summarize_markdown(self, markdown_text: str, repo_name: str, date_str: str) -> str:
        prompt = f"""You are an assistant that summarizes GitHub project updates.

Project: {repo_name}
Date: {date_str}

Below is a raw daily update in Markdown format containing open issues and pull requests.
Your job is to generate a concise, well-formatted project update report suitable for team sharing.

Format the output in Markdown, using sections like:
- Summary
- Key Issues
- Important PRs
- Notable Commits

Raw Input:
\"\"\"
{markdown_text}
\"\"\"
"""

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )

        return response.choices[0].message["content"]

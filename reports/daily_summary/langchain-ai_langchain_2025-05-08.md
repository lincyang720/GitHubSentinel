# Project Update for `langchain-ai/langchain` - 2025-05-08

## Summary
Today, we had a total of 5 commits, 3 open issues, and 10 open pull requests. The commits were primarily focused on updates and releases for the anthropic and huggingface modules. The open issues are related to streaming issues, client errors, and bugs in CharacterTextSplitter. The pull requests are mostly documentation updates and bug fixes.

## Key Issues
- Issue [#31145](https://github.com/langchain-ai/langchain/issues/31145): Streaming issues with LiteLLM router when tools are enabled (raised by fgiuba)
- Issue [#31141](https://github.com/langchain-ai/langchain/issues/31141): Client error 401: Unauthorized for URL (raised by ssklpp)
- Issue [#31136](https://github.com/langchain-ai/langchain/issues/31136): Bug in CharacterTextSplitter re-inserting regex separator when keep_separator=False (raised by suminnnnn)

## Important PRs
- PR [#31164](https://github.com/langchain-ai/langchain/pull/31164): Typing fix in how_to/custom_tools.ipynb (proposed by vhiairrassary)
- PR [#31156](https://github.com/langchain-ai/langchain/pull/31156): Documenting the move of the aerospike vector store integration to langchain-aerospike vec-595 (proposed by dwelch-spike)
- PR [#31137](https://github.com/langchain-ai/langchain/pull/31137): Fix for regex separator merge bug in CharacterTextSplitter (proposed by suminnnnn)

## Notable Commits
- Commit [d4555ac](https://github.com/langchain-ai/langchain/commit/d4555ac): Release 0.3.13 for anthropic (by @ccurme)
- Commit [e34f9fd](https://github.com/langchain-ai/langchain/commit/e34f9fd): Update streaming usage metadata for anthropic (by @ccurme)
- Commit [d7e016c](https://github.com/langchain-ai/langchain/commit/d7e016c): Release 0.2 for huggingface (by @ccurme)
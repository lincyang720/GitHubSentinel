# Project Update for `langchain-ai/langchain` - 2025-05-08

## Summary
Today's update includes 4 new open issues and 10 open pull requests. The issues range from streaming problems with LiteLLM router to a bug in CharacterTextSplitter. The pull requests are mainly focused on documentation updates and bug fixes.

## Key Issues
- Issue #31145: A problem with streaming using LiteLLM router when tools are enabled has been reported by user fgiuba.
- Issue #31141: User ssklpp reported a 401 Client Error: Unauthorized for URL in the documentation.
- Issue #31136: User suminnnnn found a bug in CharacterTextSplitter that re-inserts regex separator when keep_separator is set to False.
- Issue #31121: Custom Mistral model returns "content": null for a tool call, which fails pydantic mapping, reported by eddie-duvall-wwt.

## Important PRs
- PR #31156: User dwelch-spike is documenting the move of the aerospike vector store integration to langchain-aerospike vec-595.
- PR #31155: Geckosecurity has identified a Local File Inclusion bug in HTMLHeaderTextSplitter.
- PR #31137: User suminnnnn is working on a fix for the regex separator merge bug in CharacterTextSplitter.
- PR #31128: Mateencog is extending pyproject.toml check in create_api_rst.py to langchain/libs folder.
- PR #31117: Cosminacho is enabling true caching support for arbitrary message stacks in langgraph.
- PR #31114: Meirk-brd is adding Brightdata integration documentation.
- PR #31112: CtrlMj is fixing issue 31035 alias fields in base tool langchain core.
- PR #31111: AsifMehmood97 is using a callback to track the usage for embedding models in partners[openai].
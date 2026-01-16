---
slug: echokit-30-days-day-25-built-in-web-search
title: "Day 25: Built-in Web Search with LLM Providers | The First 30 Days with EchoKit"
tags: [echokit30days, web-search, responses-api]
---

On Day 15, we introduced EchoKit's ability to connect to MCP servers, giving your voice agent access to external tools and actions. We showed how to connect to Tavily for web search.

On Day 23, we added DuckDuckGo MCP for real-time web search.

Both approaches required **you to host or connect to an external search service**. That works great, but what if there was an even simpler way?

**Today, we're exploring a different approach: using the LLM provider's own built-in web search.**

No separate MCP servers to configure. No API keys for search services. No extra infrastructure.

Just enable a tool, and your EchoKit can search the web.

## Built-in vs. MCP Web Search

Before diving in, let's clarify the two approaches to web search we've covered:

| Approach | Setup | Infrastructure | Control |
|----------|-------|----------------|---------|
| **MCP Servers**) | You connect to external search APIs | Requires separate MCP servers | Full control over search source |
| **Built-in Tools** (Today) | Enable in config.toml | LLM provider handles everything | Provider manages search |

**Built-in tools** are simpler — the LLM provider (OpenAI, xAI, etc.) handles everything. When your EchoKit needs current information, it just asks the provider, which performs the search and returns results.

**MCP servers** give you more control — you choose the search engine, can customize results, and can host it yourself.

Both approaches work. Today is about the simpler path: built-in tools.

The EchoKit server now supports the **OpenAI Responses API** — a stateful API that enables advanced LLM features including built-in web search.




## Configure EchoKit for Built-in Web Search

Let's set up EchoKit with different LLM providers' built-in web search.

### OpenAI with Web Search Preview

OpenAI offers the `web_search_preview` tool:

```toml
[llm]
platform = "openai_responses"
url = "https://api.openai.com/v1/responses"
api_key = "sk_ABCD"
model = "gpt-5-nano"

[[llm.extra.tools]]
type = "web_search_preview"
"""
```

Key points:
- `platform = "openai_responses"` enables the Responses API
- `type = "web_search_preview"` enables OpenAI's built-in search

### xAI Grok with Web Search

xAI's Grok offers a `web_search` tool with optional filtering:

```toml
[llm]
platform = "openai_responses"
url = "https://api.x.ai/v1/responses"
api_key = "xai_ABCD"
model = "grok-4-1-fast-non-reasoning"

[[llm.extra.tools]]
type = "web_search"
# Optional: filters = { "allowed_domains" = ["wikipedia.org"] }
```

Grok also provides a `x_search` tool to search posts on x.com (Twitter).

### Groq with Browser Search

Groq's implementation calls it `browser_search`:

```toml
[llm]
platform = "openai_responses"
url = "https://api.groq.com/openai/v1/chat/responses"
api_key = "gsk_ABCD"
model = "openai/gpt-oss-20b"

[[llm.extra.tools]]
type = "browser_search"
"""
```

## Ask EchoKit: "What's the Weather?"

Once configured, restart your EchoKit server and try a question that requires current information:

**User:** *"What's the weather like in San Francisco right now?"*

Under the hood, here's what happens with the Responses API:

1. **EchoKit sends query** — Only the latest user message is sent
2. **LLM evaluates** — The provider determines this needs current information
3. **Web search performed** — The provider searches automatically
4. **Response generated** — The LLM synthesizes an answer from search results
5. **Context saved** — Search results are stored for follow-up questions

EchoKit might respond like this:

> *"Let me check the current weather...*
>
> *Currently in San Francisco, it's 62 degrees Fahrenheit with partly cloudy skies. The high today will be around 68 degrees, with a low of 55 tonight."*

## Try Follow-up Questions

Because the Responses API is stateful, follow-up questions work naturally:

**User:** *"What about tomorrow?"*

The LLM provider already has the weather context from the previous search, so it can answer immediately without searching again.

> *"Tomorrow in San Francisco, expect sunny skies with a high of 72 degrees and a low of 58. Perfect weather for being outdoors."*

This context awareness is one of the key advantages of the Responses API.


## Built-in Tools vs. MCP: Which to Use?

We've now covered two approaches to web search. When should you use each?

**Use Built-in Tools When:**
- You want the simplest possible setup
- You're already using an LLM provider that offers search
- You don't need to customize search behavior
- Performance and simplicity are priorities

**Use MCP Servers When:**
- You want to choose your own search engine
- You need to filter or customize results
- You want to host search infrastructure yourself
- You're in a region where built-in search isn't available

Both approaches are valid. The beauty of EchoKit is that you can mix and match — use built-in tools from your provider while also connecting to custom MCP servers for specialized capabilities.

## The Agentic Vision

Across Day 15, 23, and 25, we've seen EchoKit evolve from a simple chatbot into a true AI agent:

- **Day 15**: Connected to external tools via MCP (Tavily search)
- **Day 23**: Added DuckDuckGo for privacy-focused web search
- **Day 25**: Enabled built-in search from LLM providers

Each approach adds capabilities. Your EchoKit can now:
- **Retrieve** real-time information from the web
- **Reason** about current events and live data
- **Respond** with accurate, up-to-date answers
- **Act** on that information (as we saw on Day 24 with Google Calendar)

This is the vision of agentic AI — not just conversation, but action. Not just static knowledge, but real-time information. Not just a chatbot, but a tool that bridges your voice to the entire internet.

---

Ready to explore more integrations or share your own agent setups?

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**

Ready to get your own EchoKit?

* **EchoKit Box →** [https://echokit.dev/echokit_box.html](https://echokit.dev/echokit_box.html)
* **EchoKit DIY Kit →** [https://echokit.dev/echokit_diy.html](https://echokit.dev/echokit_diy.html)

**Start building your own voice AI agent today.**

---
slug: echokit-30-days-day-23-duckduckgo-mcp
title: "Day 23: Real-Time Web Search with DuckDuckGo MCP | The First 30 Days with EchoKit"
tags: [echokit30days, mcp, web-search]
---



On Day 15, we introduced EchoKit's ability to connect to MCP (Model Context Protocol) servers, which unlocks access to external tools and actions beyond simple conversation. We showed an example using a Tavily-based search MCP server.

**Today, we're diving deeper into real-time web search using DuckDuckGo.**

Why DuckDuckGo? It's privacy-focused, doesn't require API keys for basic usage, and provides a simple way to bring real-world, up-to-date information into your voice AI conversations.

## Why Real-Time Web Search Matters

LLMs have a knowledge cutoff — they only know what they were trained on. Ask about yesterday's news, today's stock prices, or events that happened after the model's training, and they'll simply... not know.

But when you connect EchoKit to a web search MCP server, something magical happens:

* The LLM recognizes it needs current information
* It automatically invokes the search tool
* Results are retrieved from the web in real-time
* The LLM synthesizes an answer citing actual sources

Suddenly, your EchoKit isn't just a chatbot anymore — it's an AI agent that can access the entire internet through voice.

## DuckDuckGo Web Search MCP Server

For today's demo, we're using a DuckDuckGo-based web search MCP server. DuckDuckGo is an excellent choice because:

* **No API key required** for basic usage — just point and go
* **Privacy-focused** — searches aren't tracked or profiled
* **Open ecosystem** — multiple open-source DuckDuckGo MCP implementations exist

The server exposes a simple search tool that queries DuckDuckGo and returns structured results with titles, URLs, and snippets.

DuckDuckGo doesn't provide an official MCP server. You can check out this GitHub repo for more details: https://github.com/nickclyde/duckduckgo-mcp-server

Remember that EchoKit supports MCP server in the SSE and HTTP-Streamable mode.

## Configure EchoKit for DuckDuckGo Search

Add the DuckDuckGo MCP server to your EchoKit `config.toml`:

```toml
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "YOUR_GROQ_API_KEY"
model = "llama-3.3-70b-versatile"  # Or any tool-capable model
history = 5

[[llm.mcp_server]]
server = "MCP Endpoint"
type = "http_streamable"
call_mcp_message = "Let me search the web for the latest information."
```

Key points:
* `server`: The DuckDuckGo MCP server endpoint
* `type`: `http_streamable` for streaming responses or SSE are supported
* `call_mcp_message`: What EchoKit says while searching (provides feedback during latency)

## Ask EchoKit: "What's New in CES 2026?"

Now for the fun part. Restart EchoKit server and ask a question that requires current information:

**User:** *"What's new in CES 2026?"*

Under the hood, here's what happens:

1. **LLM recognizes** it needs real-time data about CES 2026
2. **Tool call initiated** — the LLM invokes the DuckDuckGo search tool via MCP
3. **Search executed** — DuckDuckGo queries the web for CES 2026 news
4. **Results returned** — titles, URLs, and snippets come back through MCP
5. **Answer synthesized** — the LLM processes the results and generates a natural response

EchoKit might respond like this:

> *"Let me search the web for the latest information...*
>
> *CES 2026 highlights (as of the first week of the show) ...."*

And it would cite the actual sources it found.


## Beyond Web Search

Once you have MCP configured, you're not limited to web search. The same protocol lets EchoKit:

* **Manage Google Calendar** — add events, check schedules
* **Send messages** — Slack, email, Discord
* **Control smart home** — Home Assistant integration for lights, AC, security
* **Read and write files** — local file system access
* **Run code** — execute scripts and return results

Each MCP server adds a new capability. Mix and match to build the agent you need.



Today's DuckDuckGo web search demo shows how EchoKit breaks free from the LLM's training cutoff. It can now:

* Answer questions about **current events**
* Look up **live data** (sports scores, stock prices, weather)
* Provide **cited information** from real sources
* Act as a **research assistant** accessible by voice

This is the vision of agentic AI — not just conversation, but action. Not just static knowledge, but real-time information. Not just a chatbot, but a tool that bridges your voice to the entire internet.

---

Want to explore more MCP integrations or share your own agent setups?

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**

Ready to get your own EchoKit?

* **EchoKit Box →** [https://echokit.dev/echokit_box.html](https://echokit.dev/echokit_box.html)
* **EchoKit DIY Kit →** [https://echokit.dev/echokit_diy.html](https://echokit.dev/echokit_diy.html)

**Start building your own voice AI agent today.**

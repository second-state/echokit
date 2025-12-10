---
slug: echokit-30-days-day-15-mcp-web-search
title: "Day 15: EchoKit × MCP — Search the Web with Your Voice | The First 30 Days with EchoKit"
tags: [echokit30days]
---




Over the past few days in The First 30 Days with EchoKit, we’ve explored how EchoKit connects to various LLM providers—OpenAI, OpenRouter, Groq, Grok and even local models. But switching models only affects how smart EchoKit is. 

Next, we showed how changing the system prompt can transform EchoKit’s personality without touching any code—turning it into a coach, a cat, or a Shakespearean actor. Today, we’re going to extend what EchoKit can do by plugging into the broader ecosystem of tools through the Model Context Protocol (MCP). 

Recent industry news makes this especially timely: on December 9, 2025, Anthropic donated MCP to the Linux Foundation and co‑founded the Agentic AI Foundation (AAIF) with Block and OpenAI. MCP is now joined by Block’s Goose agent framework and OpenAI’s AGENTS.md spec as the founding projects of the AAIF.

## 🧠 What is MCP?

MCP acts like a “USB‑C port” for AI agents. It defines a client–server protocol that lets models call external tools, databases or APIs through standardised actions. MCP servers wrap services—such as file systems, web searches or device controls—behind simple JSON‑RPC endpoints. MCP Clients (like EchoKit or Anthropic’s Claude Code) connect to one or more MCP servers and dynamically discover available tools. When the model needs information or wants to perform an action, it sends a tool request; the server executes the tool and returns results for the model to use

MCP’s adoption has been rapid: within a year of its release there were over 10,000 public MCP servers and more than 97 million SDK downloads. It’s been integrated into major platforms like ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot and VS Code. By placing MCP under the AAIF, Anthropic and its partners ensure that this crucial infrastructure remains open, neutral and community‑driven.

## 🔧 Connect EchoKit to an MCP Server

To make EchoKit call external tools, we simply point it to an MCP server. Add a section like the following to your config.toml:

```
[[llm.mcp_server]]
server = "MCP_SERVER_URL"
type   = "http_streamable"
```

server – the URL of the MCP server (replace this with the server you want to use).

type – http_streamable and SSE mode are supported.

Once configured, EchoKit will automatically maintain a connection to the MCP server. When the LLM detects that it needs to call a tool, it issues a request via MCP and merges the response into the LLM. So, if you want to use MCP server, the LLM you used must support tool call. Here are some recommendations:

* Open source models: Qwen3, GPT-OSS, Llama 3.1
* Close source models: Gemini, OpenAI, Claude

## 🌐 Example: Adding a Web Search Tool

To demonstrate, let’s connect EchoKit to a web‑search MCP server. Many open‑source servers provide a search tool that scrapes public search engine results—often without requiring API keys. 

Adding the server to your configuration. Here I use the GPT-OSS-120B model hosted on Groq and the tavily MCP server:
```
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "YOUR API KEY"
model = "openai/gpt-oss-120b"
history = 5

[llm.mcp_server]]
server = "http://eu.echokit.dev:8011/mcp"
type = "http_streamable"
```


After that, save the file and restart EchoKit as usual.

Ask: “Tell me the latest update of MCP.”

Under the hood, EchoKit’s LLM recognises that it needs up‑to‑date information. It invokes the search tool on your MCP server, passing your query.

The MCP server performs the web search and returns structured results (titles, URLs and snippets). EchoKit then synthesises a natural‑language answer, summarising the findings and citing the sources.

You can also use other MCP sever tools like the Google Calendar MCP server to add and edit event, Slack MCP server to send an message to the Slack channel, Home Assistant MCP server to control the home device. All of these tools become accessible through your voice.

## 📌 Why This Matters

Integrating MCP gives EchoKit access to a rapidly expanding tool ecosystem. You’re no longer limited to predetermined voice commands; your agent can search the web, read files, run code, query databases or control smart devices—all through a the voice interface. The AAIF’s stewardship of MCP ensures that these capabilities remain open and interoperable, so EchoKit can continue to evolve alongside the broader agentic AI community.

---

Want to explore more or share what you’ve built with MCP servers?

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**

Ready to get your own EchoKit?

* **EchoKit Box →** [https://echokit.dev/echokit_box.html](https://echokit.dev/echokit_box.html)
* **EchoKit DIY Kit →** [https://echokit.dev/echokit_diy.html](https://echokit.dev/echokit_diy.html)

**Start building your own voice AI agent today.**

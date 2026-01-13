---
slug: echokit-30-days-day-24-google-calendar-mcp
title: "Day 24: CES 2026 in Practice — Voice Agents That Act | The First 30 Days with EchoKit"
tags: [echokit30days, mcp, google-calendar]
---



At CES 2026, the message was clear: **Smartphones are so 2025.**

The future isn't a bigger or foldable screen. It's AI pendants around your neck, holographic companions like Razer's Project AVA, robot pets that hug back, and always-on voice agents that act without touching any screen.

These aren't just "better assistants." They're proactive voice AI agents that listen, understand context, reason, act, and respond — all hands-free, no phone needed.

EchoKit is the open-source devkit showing how those AI devices work under the hood.

We've been building toward this. On Day 15, we introduced MCP (Model Context Protocol) as EchoKit's gateway to external tools. We showed how to connect to Tavily search. On Day 23, we added DuckDuckGo for real-time web search.

Those were about **information** — giving your voice agent the ability to retrieve knowledge from the web.

**Today is about action.**

Today, your EchoKit learns to **do things** for you.

We will show you how to integrate Zapier's Google MCP server and EchoKit to manage your Google Calendar via voice.

## Why Action Matters

Imagine this: You're rushing to get ready in the morning, hands full, and you remember you need to schedule a meeting with your team tomorrow at 2 PM.

Without action capability, your EchoKit could say, "You should schedule that meeting when you get to your computer." Helpful, but not helpful enough.

With action capability, you simply say:

*"Schedule a team meeting tomorrow at 2 PM for one hour"*

And your EchoKit **actually does it**.

No phone. No computer. No screens. Just voice.

That's the difference between a conversational AI that **talks about** your schedule and an agentic AI that **manages** it.

**Setup takes 5 minutes. Once configured, every calendar interaction becomes voice-controlled.**

## Zapier's Google Calendar MCP Server

For today's integration, we're using Zapier's Google Calendar MCP server. Zapier has built an excellent MCP implementation that provides:

* **Create events** — add calendar entries with title, time, and duration
* **List upcoming events** — see what's scheduled
* **Search events** — find specific appointments
* **Update events** — modify existing calendar entries

The Zapier MCP server handles all the OAuth authentication and API details, exposing clean tools that EchoKit can use to take action on your behalf.

**Remember that EchoKit supports MCP server in the SSE and HTTP-Streamable mode.**

## Setting Up Zapier MCP Server

Before configuring EchoKit, you'll need to set up the Zapier MCP server and get your endpoint URL:

1. **Go to [zapier.com/mcp](https://zapier.com/mcp)** — This is where you manage MCP integrations
3. **Click "+ New MCP Server"** — Zapier will walk you through creating the MCP server you want
4. **Click Rotate token to get the MCP server URL** — It looks like: `https://mcp.zapier.com/api/v1/connect?token=YOUR_TOKEN`

**Keep this URL handy — you'll need it for the next step.**

## Configure EchoKit for Google Calendar

Now add the Zapier Google Calendar MCP server to your EchoKit `config.toml`:

```toml
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "YOUR_GROQ_API_KEY"
model = "llama-3.3-70b-versatile"  # Or any tool-capable model
history = 5

[[llm.mcp_server]]
server = "https://mcp.zapier.com/api/v1/connect?token=YOUR_TOKEN"
type = "http_streamable"
call_mcp_message = "Hold on a second. Let me check your calendar."
```

Key points:
* `server`: Paste the Zapier MCP server endpoint URL you copied above
* `type`: `sse` for server-sent events or `http_streamable` for streaming HTTP
* `call_mcp_message`: What EchoKit says while accessing your calendar


## Ask EchoKit: "Schedule a Team Meeting"

Once configured, restart EchoKit server and try a voice command:

**User:** *"Schedule a team meeting tomorrow at 2 PM for one hour"*

Under the hood, here's what happens:

1. **LLM parses the request** — understands it's a calendar action with time and duration
2. **Tool call initiated** — invokes the Google Calendar `create_event` tool via MCP
3. **Action executed** — Zapier adds the event to your Google Calendar
4. **Confirmation returned** — EchoKit confirms the action was completed

EchoKit might respond like this:

> *"Let me check your calendar...*
>
> *I've scheduled your team meeting for tomorrow at 2 PM. The event will last one hour."*

Notice what happened: EchoKit didn't just **say** something. It **did** something.

## Try It Now

Restart your EchoKit server and test it:

1. **Say:** *"What's on my calendar today?"*
2. **Wait** for EchoKit to check
3. **Say:** *"Schedule a test meeting tomorrow at 10 AM"*
4. **Check your Google Calendar** — the event should appear, actually created

If it works, you're ready to go. If not, check the troubleshooting section below.

## More Voice Commands to Try

Once you have Google Calendar connected, here are some practical voice commands:

* **"What's on my calendar today?"** — Get a rundown of your schedule
* **"Schedule a dentist appointment next Tuesday at 3 PM"** — Create events with natural language
* **"When is my next meeting?"** — Check upcoming events
* **"Block out time for deep work tomorrow morning"** — Reserve focused time
* **"Move my team meeting to 3 PM"** — Reschedule existing events

The LLM understands natural language timing — "tomorrow morning," "next Tuesday," "in two hours" — and converts it into proper calendar entries.


What makes Zapier's MCP server powerful is that it's not just about calendars. Zapier connects to **5,000+ apps**, and through MCP, EchoKit can potentially interact with many of them:

* **Slack** — Send messages, check channels
* **Gmail** — Compose emails, search inbox
* **Trello/Asana** — Create tasks, update boards
* **Notion** — Add database entries, create pages
* **GitHub** — Create issues, check repositories

Each Zapier integration you enable adds a new action capability to your voice agent.

## From Voice to Action

Your EchoKit has evolved through these 24 days:

It started as a conversational AI that could **talk** with you.

Then it learned to **listen** and understand intent.

On Day 15 and 23, it learned to **search** and retrieve information.

Today, it learned to **act**.

This is the vision of agentic AI — not just conversation, but action. Not just talking about doing things, but actually doing them.

Your EchoKit isn't just answering questions anymore. It's getting things done.


---

Ready to give your voice agent action capabilities?

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)** to share your setup and get help

Want to get your own EchoKit?

* **EchoKit Box →** [https://echokit.dev/echokit_box.html](https://echokit.dev/echokit_box.html)
* **EchoKit DIY Kit →** [https://echokit.dev/echokit_diy.html](https://echokit.dev/echokit_diy.html)

**Start building your voice-powered productivity assistant today.**

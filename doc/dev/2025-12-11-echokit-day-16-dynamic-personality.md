---
slug: echokit-30-days-day-16-dynamic-personality
title: "Day 16: Dynamic Personality for EchoKit | The First 30 Days with EchoKit"
tags: [echokit30days]
---


In previous instalments we explored switching LLM providers and giving EchoKit different personalities through system prompts. Today let's learn a powerful new feature —**dynamic system prompt loading**.

## Why dynamic system prompts?

A system prompt sets EchoKit’s tone, role and behaviour. Thanks to the growing ecosystem of open‑source prompts, you can choose from thousands of prebuilt personalities—sites like LLMs.txt offer extensive collections. Previously, changing EchoKit’s character required editing a local file and restarting the server. Now the server can fetch a system prompt from a remote URL, insert it into the context and cache it. This lets you:

* **Update behaviour remotely.** Change the text at the URL and EchoKit adopts a new persona on the next restart.
* **Experiment without redeploying.** Quickly swap prompts or test new conversation flows without editing code.
* **Iterate on demos.** Focus on creativity rather than configuration while your EchoKit responds in new ways.

## How to use a remote prompt

Open your `config.toml` and find the `[[llm.sys_prompts]]` section. Instead of embedding the full text, wrap a plain‑text URL in double braces:

```toml
[[llm.sys_prompts]]
role = "system"
content = """
{{ https://raw.githubusercontent.com/alabulei1/echokit-dynamic-prompt/refs/heads/main/prompt.txt }}
"""
```

On startup, EchoKit will:

1. Fetch the content from that URL.
2. Insert it as the system prompt.
3. Cache it for later use.

Want to give it a try? GitHub raw files are convenient hosts because it's free and they can return plain text.

## When does EchoKit reload the prompt?

Dynamic prompts are fetched only during a **full restart**:

* When you power the device off and back on.
* When you press the **RST** hardware button.

Interrupting a conversation with the K0 button or a temporary Wi‑Fi reconnection will not reload the prompt. This ensures ongoing sessions remain consistent while still giving you the freedom to change behaviour by updating the remote file.

## Summary

Dynamic system prompt loading opens up a new level of flexibility for EchoKit. You no longer need to modify local files or restart the server to change your agent’s behaviour; instead, you can pull any prompt hosted on the web and swap personas at will.

---
Want to get your EchoKit Device and make it unique?
* [EchoKit Box](https://echokit.dev/echokit_box.html) 
* [EchoKit DIY](https://echokit.dev/echokit_diy.html)

Join the [EchoKit Discord](https://discord.gg/Fwe3zsT5g3) to share your creative welcome voices and see how others are personalizing their Voice AI agents!

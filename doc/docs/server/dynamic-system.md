---
sidebar_position: 5
---

# Dynamic System Prompt Loading

EchoKit supports **dynamic loading of system prompts** using a URL reference inside the configuration file `config.toml`. This feature allows the device to fetch the latest prompt text from the internet at runtime—**without restarting the EchoKit server**.

It’s truly *building the plane while flying it*.

## How to Use Dynamic Prompt URLs

You can reference an external prompt file inside your `[[llm.sys_prompts]]` configuration by embedding a URL.

Open the `config.toml` file, locate the `[[llm.sys_prompts]]` section and edit your prompt following the format below:

```
[[llm.sys_prompts]]
role = "system"
content = """
{{ https://raw.githubusercontent.com/alabulei1/echokit-dynamic-prompt/refs/heads/main/prompt.txt }}
"""
```

EchoKit will automatically:

1. Fetch the content from the provided URL
2. Insert it into the system prompt
3. Cache the result
4. Use it for all subsequent LLM interactions (until the next prompt reload)

> The URL must return **plain text** and GitHub repo is a suitable place to store your prompt.

Afterward, if you want to change the behavior of your EchoKit voice AI agent, simply update the prompt at the URL — no firmware update or server restart required.

## When the System Prompt Is Reloaded

EchoKit reloads the system prompt only during a **full restart**. A full restart clears the session and reinitializes all LLM state.

The system prompt **will be reloaded** in the following scenarios:

### ✔ Power-off / Power-on

If the device loses power or is manually restarted, EchoKit will reload the system prompt from the URL.

### ✔ Pressing the `RST` hardware button

The reset button triggers a full restart.


When a full restart happens, the following actions occur:

* Reload system prompts
* Clear conversation history
* Reinitialize LLM state

Your updated system prompt will take effect immediately after the restart.



## When the System Prompt Is **Not** Reloaded

EchoKit **does not reload** the system prompt after reconnections or conversation interruptions.

### ✘ Pressing the `K0` button to interrupt the conversation

Interrupting or stopping an in-progress conversation does **not** trigger a prompt reload.
History and LLM state remain intact.

### ✘ Temporary Wi-Fi or server reconnection

If network connectivity drops momentarily, EchoKit preserves:

* The currently loaded system prompt (cached)
* Conversation history
* LLM state

This ensures continuity and reduces unnecessary reloads.


## Summary

Dynamic prompt loading provides a flexible and efficient way to update EchoKit’s system-level behavior without touching firmware or restarting the server. The system prompt is reloaded only after the EchoKit device restarts.

* Power-on
* Pressing the RST button

It remains unchanged during normal interruptions or network reconnections.

This design allows you to update personalities, rules, and behaviors quickly—while preserving stable ongoing sessions when needed.

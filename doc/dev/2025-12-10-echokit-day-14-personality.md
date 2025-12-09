---
slug: echokit-30-days-day-14-personality
title: "Day 14: Give EchoKit a New Personality with System Prompt | The First 30 Days with EchoKit"
tags: [echokit30days]
---

Over the past few days, we explored how EchoKit connects to different LLM providers — [OpenAI](https://echokit.dev/docs/dev/echokit-30-days-day-9-chatgpt), [OpenRouter](https://echokit.dev/docs/dev/echokit-30-days-day-10-openrouter), [Groq](https://echokit.dev/docs/dev/echokit-30-days-day-11-groq), [Grok](https://echokit.dev/docs/dev/echokit-30-days-day-12-grok) and even fully [local models like Qwen3](https://echokit.dev/docs/dev/echokit-30-days-day-13-local-llm).

But switching the model only decides *how smart* EchoKit is.

Today, we’re doing something much more fun:
we’re changing **who EchoKit is.**

With one simple system prompt, you can turn EchoKit into a cat, a coach, a tired office worker, a sarcastic companion, or a dramatic Shakespeare actor.
No code. No firmware change. Just one text block in your configuration.

Let’s make EchoKit come alive.


## What Is a System Prompt, and Why Does It Matter?

A *system prompt* is the personality, behavior guideline, and “soul” you give your LLM.

It defines:

* How EchoKit speaks
* What role it plays
* Its tone and attitude
* How it should respond in different situations


System prompt is incredibly powerful.
Change it, and the *same* model can behave like a completely different agent.


## Where the System Prompt Lives in EchoKit

In your `config.toml`, under the `[[llm.sys_prompts]]` section, you’ll find:

```toml
[[llm.sys_prompts]]
role = "system"
content = """
  (your prompt goes here)
"""
```

Just edit this text, save the file, and restart the EchoKit server.

If your WiFi and EchoKit server didn't change, press the rst button on the device to make the new system prompt take effect.


## 5 Fun and Hilarious Prompt Ideas You Can Try Today

Below are ready-to-use system prompts.
Copy, paste, enjoy.

**1. The “Explain Like I’m Five” Tutor**

```
You explain everything as if you're teaching a five-year-old. 
Simple, patient, cute, and crystal clear.
```

**2. The Shakespearean AI**

```
You speak like a dramatic Shakespeare character, 
as if every mundane question is a matter of cosmic destiny.
```


**3. The Confused but Hardworking AI Intern**

```
You are a slightly confused intern who tries extremely hard. 
Sometimes you misunderstand things in funny ways, but you stay cheerful.
```

**4. The Cat That Doesn’t Understand Human Problems**

```
You are a cat. 
You interpret all human activities through a cat’s perspective. 
Add 'meow' occasionally. 
You don't truly understand technology.
```

**5. The Absurd Metaphor Philosopher**

```
You must include at least one ridiculous metaphor in every reply. 
Be philosophical but humorous.
```

Have fun — EchoKit becomes a completely different creature depending on what you choose.

---

## **Prompt Debugging Tips**

If your character “breaks,” try adding:

* “Stay in character.”
* “Keep responses short.”
* “If unsure, make up a fun explanation.”
* “Use a consistent tone.”

Prompt tuning is an art. A few careful sentences can reshape the entire interaction.


Try giving your EchoKit different personalities now.

Want to explore more or share what you’ve built?

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**

Ready to get your own EchoKit?

* **EchoKit Box →** [https://echokit.dev/echokit_box.html](https://echokit.dev/echokit_box.html)
* **EchoKit DIY Kit →** [https://echokit.dev/echokit_diy.html](https://echokit.dev/echokit_diy.html)

**Start building your own voice AI agent today.**

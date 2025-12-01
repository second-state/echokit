---
slug: echokit-30-days-day-9-chatgpt
title: "Day 9: Use OpenAI as Your EchoKit LLM Provider | The First 30 Days with EchoKit"
tags: [echokit30days]
---

**(And today, you’ll see how easy it is to use OpenAI as your LLM provider.)**

Hey everyone, and welcome back! We've covered a *ton* of ground over the past two weeks in "The First 30 Days with EchoKit." Seriously, look how much we've accomplished:

  * [Getting a quick start with the pre-set EchoKit server](https://echokit.dev/docs/dev/echokit-30-days-day-1).
  * [Figuring out how to change your EchoKit's **welcome voice**](https://echokit.dev/docs/dev/echokit-30-days-day-5-welcome-voice).
  * [Customizing the **boot screen**](https://echokit.dev/docs/dev/echokit-30-days-day-4-bootscreen)
  * [Learning to run the EchoKit server **locally** with Docker](https://echokit.dev/docs/dev/echokit-30-days-day-2-docker) and [from the Rust source](https://echokit.dev/docs/dev/echokit-30-days-day-3-rust).
  * Swapping out ASR (Speech-to-Text) providers like a pro, moving between [Groq Whisper](https://echokit.dev/docs/dev/echokit-30-days-day-6-groq), [OpenAI Whisper](https://echokit.dev/docs/dev/echokit-30-days-day-7-openai), and [Local Whisper](https://echokit.dev/docs/dev/echokit-30-days-day-8-local-whisper).

If you remember, everything inside EchoKit runs through that simple yet incredibly powerful pipeline: **ASR → LLM → TTS** so far.

Each piece plays a crucial part in the voice AI loop:

  * **ASR (The Ears):** Converts your spoken words into text.
  * **LLM (The Brain):** Interprets that text, thinks about it, and decides what the perfect response should be.
  * **TTS (The Mouth):** Turns the final text answer back into speech.

Last week, we were all about replacing Whisper and swapping out the "ears." For the next few days, we're putting the spotlight squarely on the **middle piece: the LLM.**

And today, we’re starting with the most common and powerful choice out there—**OpenAI**!

### ⭐ What Exactly Does the LLM Do in the EchoKit Server? (It's the Mastermind!)

The LLM is, quite literally, the **mastermind of your entire setup**. It's the engine that:

  * **Instantly grasps** what the user actually wants.
  * **Processes** all the conversational history (context).
  * **Generates** those helpful, natural, and human-like responses.
  * **Controls** how your EchoKit behaves during a conversation.
  * And, yes, it calls the necessary MCP servers to get things done!

EchoKit proudly **supports any provider that uses an OpenAI-compatible LLM API**. 

### Step 1 — Get Your Key Ready

Open up your trusted `config.toml` file and find the `[llm]` section. Replace it with this block:

```toml
[llm]
llm_chat_url = "https://api.openai.com/v1/chat/completions"
api_key = "YOUR_OPENAI_KEY" # Don't forget to replace this!
model = "gpt-5-mini-2025-08-07" # Choose your favorite model here (e.g., gpt-3.5-turbo)
history = 5
```

Here's the quick rundown on those settings, just so you know what you're tuning:

  * `[llm]`: We're configuring the Large Language Model section.
  * `llm_chat_url`: OpenAI’s chat completions endpoint.
  * `api_key`: Get your key from the [OpenAI API platform](https://platform.openai.com/docs/overview). 
  * `model`: Which OpenAI model should power your EchoKit's thoughts? Up to you!
  * `history`: How many previous turns of the conversation should your EchoKit remember for context?

### Step 2 — Time for a Quick Reboot!

Whether you’re running your EchoKit server via Docker or from the Rust code, **go ahead and restart it right now.** That’s it! You're completely done with the server configuration. Told you it was easy!

### Step 3 — Connect the New Brain to Your Device

The grand finale! Time to link up your physical EchoKit device to the server with its shiny new OpenAI brain:

1.  Head over to [https://echokit.dev/setup/](https://echokit.dev/setup/) and reconnect the server if you need to.
2.  **Pro Tip:** If you only changed your LLM configuration and nothing else (URL, WiFi), you can just hit the **RST button** on your EchoKit device. It will restart and sync the new settings instantly\!
3.  If your server URL or WiFi setup changed, you'll need to reconfigure them through the setup page, just like you did on [Day 1](https://echokit.dev/docs/dev/echokit-30-days-day-1).

Next, press that K0 button and start speaking. Every clever thing your EchoKit says back to you is now being powered by OpenAI!

---

If you want to share your experience or see what others are building with EchoKit + OpenAI:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)






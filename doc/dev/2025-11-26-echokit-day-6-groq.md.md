---
slug: echokit-30-days-day-6-groq
title: "Day 6: Integrate Groq as the ASR Engine for Your EchoKit | The First 30 Days with EchoKit"
tags: [echokit30days]
---

*(Today, your EchoKit learns to understand you—faster and sharper.)*

By now, you’ve powered up EchoKit, [run your own EchoKit server locally](https://echokit.dev/docs/dev/echokit-30-days-day-2-docker), [customized the boot screen](https://echokit.dev/docs/dev/echokit-30-days-day-4-bootscreen), [crafted your own welcome voice](https://echokit.dev/docs/dev/echokit-30-days-day-5-welcome-voice), and started shaping your very own voice AI companion.

Today, we’re upgrading something fundamental: **how your EchoKit listens to you.** In any voice AI agent, ASR is the very first step — it’s how your device hears you before it can think or speak back.

One of the best parts of EchoKit being **open source** voice AI agent is that you can plug in whatever ASR–LLM–TTS pipeline works best for your needs. And for many makers, developers, and tinkerers, **Groq** has become the go-to for ultra-fast voice recognition.

So on **Day 6**, you’ll learn how to **integrate Groq with EchoKit** and feel that speed boost every time you press the K0 button and start talking.

Let’s dive in.

## Why Groq? (And Why Today Feels Like a Power-Up)

If you’ve never tried Groq before, prepare to be surprised.
Groq is known for delivering **extremely low-latency inference**. When we tested it, the difference was obvious — conversations felt snappier, more natural, and closer to real-time.

Adding it to your EchoKit means:

* Faster voice-to-text recognition
* More responsive conversations
* A smoother ASR-LLM-TTS pipeline
* And honestly… it just feels good seeing your device level up

Today is about giving your device better ears.

## Step 1 — Get Your Groq API Key

Head to the Groq console ([https://console.groq.com/keys](https://console.groq.com/keys)) and sign up if you’re new.

Click **+ Create API Key**, give it a name, and copy it somewhere safe — it won’t be shown again.

This key is what lets your EchoKit talk to Groq securely.


## Step 2 — Apply the Groq ASR Settings to Your EchoKit Server

Open your `config.toml` file inside your **EchoKit Server** (Docker or Rust build).

We’re going to tell EchoKit: *“Hey, use Groq Whisper as my ASR engine.”*

Paste the following:

```
[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
lang = "en"
api_key = "gsk_1234"
model = "whisper-large-v3-turbo"
```

A quick breakdown:

* **[asr]** — we’re configuring the ASR section
* **url** — Groq’s Whisper endpoint
* **lang** — your preferred language (`en`, `zh`, `ja` etc.)
* **api_key** — the key you generated
* **model** — Groq’s supported Whisper models (`whisper-large-v3` or `whisper-large-v3-turbo`)

EchoKit follows OpenAI-style specs, so you’re free to replace Groq with other providers later if you want, which we will learn in the upcoming days. This flexibility is part of what makes EchoKit… EchoKit.

Now restart your EchoKit server using Docker or Rust code.
You’re done on the server side!


## Step 3 — Connect the Updated Server to Your EchoKit Device

Head to [https://echokit.dev/setup/](https://echokit.dev/setup/) and rebind the server if needed.

If nothing changed except your ASR configuration, you can simply **press the RST button** on your EchoKit to restart it and sync the new settings.

If your server URL or WiFi setup changed, you can reconfigure them through the setup page — just like you did on [Day 1](https://echokit.dev/docs/dev/echokit-30-days-day-1).

Now comes the fun part.

Press the **K0 button** and start speaking.

You’ll feel the difference immediately — the Groq Whisper model picks up your words almost as soon as you say them.

Your EchoKit just got better ears. Remember to check the logs to see how long Groq’s Whisper took to transcribe the audio.


Today’s upgrade brings more speed and responsiveness, setting the stage for a deeper dive into the EchoKit server in the upcoming days.

If you want to share your experience or see what others are building with EchoKit + Groq:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

---

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)

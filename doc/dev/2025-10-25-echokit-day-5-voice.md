---
slug: echokit-30-days-day-5-welcome-voice
title: "Day 5: Customize the Welcome Voice for Your EchoKit | The First 30 Days with EchoKit"
tags: [echokit30days]
---

*(And Today, Your EchoKit Greets You in Your Own Voice!)*

By now, you’ve powered up EchoKit, run the server (via [Docker](https://echokit.dev/docs/dev/echokit-30-days-day-2-docker) or [from source](https://echokit.dev/docs/dev/echokit-30-days-day-3-rust)), and even [customized the boot screen](https://echokit.dev/docs/dev/echokit-30-days-day-4-bootscreen).

Today, we’re taking it **one step further**: giving your EchoKit a **personalized welcome voice**.

It’s a simple tweak, but it instantly transforms your device into a **Voice AI agent** with its own character — a tiny **AI companion** that greets you the way you like.


## Create Your Own Voice

Your welcome sound can be anything you want:

* Your own recorded voice
* A short greeting phrase
* Even a favorite piece of music

Just make sure your audio file meets these requirements:

* **WAV format**
* **16 kHz sample rate**

You can quickly convert audio to 16 KHz using [the online tool](https://www.ezyzip.com/convert-wav-to-16kHz-online.html#) or **FFmpeg**:

```bash
ffmpeg -i input.mp3 -ar 16000 output.wav
```

💡 Pro Tip: This is a great opportunity to give your EchoKit a **special gift** — a voice that makes it uniquely yours!


## Set Up Your Custom Welcome Voice

To apply your custom sound, run your **EchoKit Server** (Docker or compiled binary). 

If your device was previously set up, reset it first:

* Press the RST button
* Immediately press the K0 button until the QR code shows

Then, open your `config.toml` file and look for:

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"
```

Replace `hello.wav` with your own file path, for example:

```toml
addr = "0.0.0.0:8080"
hello_wav = "my_welcome.wav"
```

Restart your EchoKit server using [Docker](https://echokit.dev/docs/dev/echokit-30-days-day-2-docker) or [from the Rust source code]((https://echokit.dev/docs/dev/echokit-30-days-day-3-rust).

Then, [connect the echokit server and the device](https://echokit.dev/docs/dev/echokit-30-days-day-1) via https://echokit.dev/setup/ page. 

> If your server URL and Wifi setting didn't change, you can simply restart the device by pressing the rst button.

After that, when you press the **K0 button** to start a conversation, **your EchoKit will greet you with your very own welcome sound.** 🎶


## Why This Matters

A custom welcome voice turns EchoKit from a generic device into your **personal AI companion**.
Every interaction feels more natural, more fun, and more expressive — like it really knows you.

Whether it’s a playful hello, a soothing greeting, or a quirky sound effect, this is a **special gift** you give to yourself and your device.


Want to get your EchoKit Device and make it unique?
* [EchoKit Box](https://echokit.dev/echokit_box.html) 
* [EchoKit DIY](https://echokit.dev/echokit_diy.html)

Join the [EchoKit Discord](https://discord.gg/Fwe3zsT5g3) to share your creative welcome voices and see how others are personalizing their Voice AI agents!

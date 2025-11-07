---
sidebar_position: 10
---

# Trouble shooting

You can debug and fix common issues with the EchoKit yourself!

## The response feels too slow

The EchoKit might take a long time (more than 5 seconds) to respond to the user. 
Or, the response speech might stutter -- there are long pauses between sentences.
You could try the folllowing to reduce latency.

### Option 1: Use an EchoKit server close to you

If you are using our public EchoKit servers, please be aware that we make no guarantee of performance. If a lot of people are using the public servers, they will respond slowly. That said, you should at least make sure that you can using a server that is close to your location [in the EchoKit device configuration](quick-start.md).

* North America: `ws://indie.echokit.dev/ws`
* Europe: `ws://eu.echokit.dev/ws`

If you are outside of north America or Europe, we highly recommend you to run your own EchoKit server on your own computer (see below).

### Option 2: Run your own EchoKit server locally

Running your own EchoKit server on your local (i.e., WiFi) network would drastically reduce latency.
First, please make sure that [your EchoKit device has the latest firmware](hardware/flash-firmware.md).

Then, [run the EchoKit server](server/quick-start.md) on a computer on your local network.

If you use the default `config.toml`, you will be running the EchoKit server at port 8080.
From the computer's network settings, locate its local network IP address (e.g., `192.168.2.201`).
In the EchoKit device configuration](quick-start.md), use the local EchoKit server -- replace the IP address with your own.

```
ws://192.168.2.201:8080/ws
```


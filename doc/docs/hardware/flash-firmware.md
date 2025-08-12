---
sidebar_position: 1
---

# Flash the Hardware

Each EchoKit comes pre-flashed with the ESP32 firmware.
If your device isn’t working as expected, you can manually re-flash it by following these steps.

Here’s a polished, native-sounding, and clearer version of your tutorial:

---

## sidebar\_position: 1

# Flashing the Hardware

Each EchoKit comes pre-flashed with the ESP32 firmware.
If your device isn’t working as expected, you can manually re-flash it by following these steps.



## 1. Install the Rust Toolchain

First, make sure you have the Rust toolchain installed. If not, follow [the official Rust installation guide](https://www.rust-lang.org/tools/install).

## 2. Install `espflash` and Dependencies

Run the following command to install `espflash` and related tools:

```bash
cargo install cargo-espflash espflash ldproxy
```

## 3. Download the Precompiled Firmware

Fetch the latest precompiled EchoKit firmware:

```bash
curl -L -o echokit https://echokit.dev/firmware/echokit-boards
```


## 4. Flash the Firmware to EchoKit

Use the command below to flash your device:

```bash
espflash flash --monitor --flash-size 16mb echokit
```

You should see output similar to this:

```
[2025-04-28T16:51:43Z INFO ] Detected 2 serial ports
[2025-04-28T16:51:43Z INFO ] Ports which match a known common dev board are highlighted
[2025-04-28T16:51:43Z INFO ] Please select a port
✔ Remember this serial port for future use? · no
[2025-04-28T16:52:00Z INFO ] Serial port: '/dev/cu.usbmodem2101'
[2025-04-28T16:52:00Z INFO ] Connecting...
[2025-04-28T16:52:00Z INFO ] Using flash stub
Chip type:         esp32s3 (revision v0.2)
Crystal frequency: 40 MHz
Flash size:        8MB
Features:          WiFi, BLE
... ...
I (705) boot: Loaded app from partition at offset 0x10000
I (705) boot: Disabling RNG early entropy source...
I (716) cpu_start: Multicore app
```

## 5. Configure and Connect EchoKit

After flashing, you’ll need to:

1. **Set up and run an EchoKit server.**
2. **Configure your device** to connect to the server.

Once both steps are complete, your EchoKit will be ready for use.




---
sidebar_position: 3
---

# Connect EchoKit Server with the Device

In this guide, we'll walk through connecting your EchoKit device to the EchoKit server.

## Prerequisites

Before starting, make sure you have:  

* Successfully [flashed the EchoKit hardware](../hardware/flash-firmware.md)
* A [running EchoKit server](echokit-server.md)
* Powered up your EchoKit

## Steps to Connect

1. Open [https://echokit.dev/setup/](https://echokit.dev/setup/) in your browser.  
2. Click **Connect to EchoKit**.  
3. Find the device named **`nimble`** and click **Pair**.  
4. Enter the following details:  
   * **Wi-Fi name (SSID)**  Only support 2.4G WiFi.
   * **Wi-Fi password**  
   * **EchoKit server URL**  

👉 Remember to click **Write** to save the settings.  

![Set up EchoKit server](connect-echokit.png)

5. Press the **K0 button** (on the left-hand side of the device) on the device to apply the new settings.  

## Expected Outcome

Once the connection is successful: 

* The device will greet you with an audio message: **“Hi there”**   

Your EchoKit is now connected and ready to use.

## Next

Press the **K0 button** to start your conversation with EchoKit.

![](../echokit-quick-start-05.jpg)

## Re-connect the Echokit server

If you need to update your Wi-Fi settings, you’ll have to reconnect the EchoKit device to the server.

1. Press the **RST** (reset) button to restart the device.
2. Immediately press and hold the **K0** button until the QR code appears.
3. Repeat the steps above to pair the device and re-enter your Wi-Fi and server details.

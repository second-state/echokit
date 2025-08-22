---
sidebar_position: 7
---

# Test Your EchoKit Server

Once you have your EchoKit server running successfully, you can test it using a web-based interface to verify that voice interactions work properly.

## Prerequisites

Before testing, ensure:
- Your EchoKit server is running and accessible
- You know your server's IP address and port
- Your browser supports WebSocket connections
- Your microphone is working and accessible to the browser

## Testing Steps

### 1. Access the Test Interface

Go to **https://echokit.dev/chat/** in your web browser.

### 2. Download the Test Client

1. Download the `index.html` file to your local computer
2. Save it in a location you can easily find (e.g., Desktop or Downloads folder)

### 3. Open the Test Client

1. **Double-click** the downloaded `index.html` file
2. It will open in your default web browser
3. Allow microphone access when prompted by your browser

### 4. Connect to Your Server

1. **Enter your EchoKit server's WebSocket URL** in the connection field
   - Format: `ws://[your-server-ip]:[port]/ws/`
   - Examples: `ws://192.168.1.100:9090/ws/`

2. **Click "Connect"** to establish the WebSocket connection
   - You should see a "Connected" status message

### 5. Test Voice Interaction

1. **Click "Start Listening"** to begin voice capture
2. **Start speaking** your question or command
   - Speak clearly and at normal volume
   - Wait for the system to process your speech
3. **Click "Stop Listening"** when you finish speaking
4. **Wait for the response** - EchoKit will process and respond with voice

## Expected Behavior

**Successful Test Flow:**
1. Connection established ✅
2. Speech captured and sent to server ✅
3. Server processes speech → text → LLM → text → speech ✅
4. Audio response plays in your browser ✅


✅ **Success!** Once you can successfully have a voice conversation through the web interface, your EchoKit server is ready for real-world use.
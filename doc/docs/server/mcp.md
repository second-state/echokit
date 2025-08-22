---
sidebar_position: 6
---

# Add Actions for EchoKit

EchoKit supports **MCP (Model Context Protocol)**, which allows LLMs to call external tools and services.  
With actions, you can extend EchoKit beyond conversation—for example:  

- Manage your Google Calendar  
- Send emails  
- Perform web searches  
- Connect to **Home Assistant** to control lights, AC, and other smart devices 
- And many others 


## 1. Prerequisites

Before adding actions, make sure you have:  

- An **MCP server** running. This can be either:  
  - **SSE MCP server**, or  
  - **HTTP streamable MCP server**  
- You can use a public MCP server or run one locally on your machine.  


## 2. Configure MCP server in EchoKit

Add the following section to your `config.toml` file:  

```toml
[[llm.mcp_server]]
server = "http://localhost:8000/mcp"
type = "http_streamable"
````

* `server`: The MCP server address.
* `type`: The type of MCP server. Supported values:

  * `sse`
  * `http_streamable`

👉 You can add multiple `[[llm.mcp_server]]` blocks if you want to connect EchoKit to more than one MCP server.

## 3. Model requirements

Not all LLMs support tool use.
When you add actions, make sure you select a model with **tool-calling capability**, such as:

* **Qwen**
* **Gemma**
* **Any model from OpenAI**

## 4. Run the server

Once your MCP server is set and the configuration updated, restart EchoKit following [Running EchoKit server](./echokit-server.md).

EchoKit will now be able to call external actions via MCP.


✅ With this setup, your EchoKit is no longer just a voice assistant—it can interact with external systems and become a **programmable AI agent**.




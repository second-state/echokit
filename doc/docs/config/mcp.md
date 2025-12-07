---
sidebar_position: 5
---

# Tool calls and actions

EchoKit supports **MCP (Model Context Protocol)**, which allows LLMs to call external tools and actions.  
With actions, you can extend EchoKit beyond conversation—for example:  

- Manage your Google Calendar  
- Send emails  
- Perform web searches  
- Connect to **Home Assistant** to control lights, AC, and other smart devices 
- And many others 


## 1. Prerequisites

Before adding MCP tools, make sure that you 

- Have access to an **MCP server**. You can use a public MCP server or run one locally on your machine. The MCP server can be either:  
  - **SSE MCP server**, or  
  - **HTTP streamable MCP server**  
- Use an LLM model that is capable of **tool use** (or, **tool calling**)

## 2. Add MCP servers to EchoKit

Add the following section to your `config.toml` file:  

```toml
[[llm.mcp_server]]
server = "http://localhost:8000/mcp"
type = "http_streamable"
call_mcp_message = "Please hold on a few seconds while I am searching for an answer!"
````

* `server`: The MCP server address.
* `type`: The type of MCP server. Supported values:
  * `sse`
  * `http_streamable`
* `call_mcp_message`: A message the EchoKit device will read aloud when the server calls the MCP tool. It is often needed since the MCP tool call could introduce signaificant latency in the response.

👉 You can add multiple `[[llm.mcp_server]]` blocks if you want to connect EchoKit to more than one MCP server.

## 3. Example

Here is an example of using Tavily to add "web search" functions to an EchoKit server.

```toml
[[llm.mcp_server]]
server = "https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR-API-KEY"
type = "http_streamable"
call_mcp_message = "It seems that I need to search the web for an answer. Please hold on!"
```

## 4. Run the server

Once your MCP server is set and the configuration updated, restart EchoKit following [Running EchoKit server](../server/echokit-server.md).

EchoKit will now be able to call external actions via MCP.


✅ With this setup, your EchoKit is no longer just a voice assistant—it can interact with external systems and become a **programmable AI agent**.




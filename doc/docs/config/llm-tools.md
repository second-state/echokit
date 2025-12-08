---
sidebar_position: 4
---

# LLM with tools

The [responses API](https://platform.openai.com/docs/api-reference/responses) is pioneered by OpenAI
to support advanced LLM features such as tool use and code interpreter. 
It is recommened to use the LLM provider's built-in tools with the responses API.

## A simple example

The following `config.toml` example shows how to use OpenAI's responses API.
Since it is a stateful API, the EchoKit server only needs to send the last user query. The LLM prrovider (OpenAI in this case) manages the conversation history.

```toml
[llm]
llm_chat_url = "https://api.openai.com/v1/responses"
api_key = "sk_ABCD"
model = "gpt-5-nano"

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.

- NEVER use bullet points
- NEVER use tables
- Answer in complete English sentences as if you are in a conversation.

"""
```

## Web search

With the OpenAI provider, you can use the built-in `web_search_preview` tool. 
OpenAI will first determine is the current user query requires a web search. If so, it will
perform the search first, and then use the LLM to generate the response based on the search results.
THe search results will also be included in the LLM history for subsequent user queries.

Below is an example for OpenAI. It adds an extra tool called `web_search_preview`, and instructs the LLM to use it.
The actual implementation of the `web_search_preview` tool is provided by OpenAI itself.

```toml
[llm]
llm_chat_url = "https://api.openai.com/v1/responses"
api_key = "sk_ABCD"
model = "gpt-5-nano"

[[llm.extra.tools]]
type = "web_search_preview"

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.

- NEVER use bullet points
- NEVER use tables
- Answer in complete English sentences as if you are in a conversation.
- Use the web_search tool if you need information about current events such as news, political figures, stock prices, and crypto prices.

"""
```

Other providers offer similar web search tools that you can pass in `[[llm.extra.tools]]`.
Below is an example for xAI Grok's responses API. As you can see, it could also support search filters. Grok also
provides a `x_search` tool to specifically search for posts in x.com.

```toml
[llm]
llm_chat_url = "https://api.x.ai/v1/responses"
api_key = "xai_ABCD"
model = "grok-4-1-fast-non-reasoning"

[[llm.extra.tools]]
type = "web_search"
# filters = { "allowed_domains" = ["wikipedia.org"] }

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.

- NEVER use bullet points
- NEVER use tables
- Answer in complete English sentences as if you are in a conversation.
- Use the web_search tool if you need information about current events such as news, political figures, stock prices, and crypto prices.

"""
```

Below is an example of Groq's responses API.
Again the name of the build-in search tool is different. It is called `browser_search` in Groq.

```toml
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/responses"
api_key = "gsk_ABCD"
model = "openai/gpt-oss-20b"

[[llm.extra.tools]]
type = "browser_search"

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.

- NEVER use bullet points
- NEVER use tables
- Answer in complete English sentences as if you are in a conversation.
- Use the browser_search tool if you need information about current events such as news, political figures, stock prices, and crypto prices.

"""
```

## MCP tools

The web search functionalities are supported as built-in LLM tools. In fact, you could add your own tools
through custom [MCP servers](https://modelcontextprotocol.io/).

Here is an example `config.toml` for xAI Grok to use custom MCP servers. All the tools in that MCP server will
be added to the LLM request. When the LLM returns a tool call for any of these tools, Grok will call the MCP
server to execute the tool call. The tool call results are then sent to the LLM, and Grok will generate 
a response based on those tool call results.

```toml
[llm]
llm_chat_url = "https://api.x.ai/v1/responses"
api_key = "xai_ABCD"
model = "grok-4-1-fast-non-reasoning"

[[llm.extra.tools]]
type = "mcp"
server_url = "https://mcp.deepwiki.com/mcp"
server_label = "deepwiki"

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.

- NEVER use bullet points
- NEVER use tables
- Answer in complete English sentences as if you are in a conversation.

"""
```

## Next step

The `[[llm.extra.tools]]` can only call MCP servers that are accessible to the cloud provider. In the case of
EchoKit server, we sometimes would like to call tools that are local to the edge server, such as home automation APIs.
That would require us to support local MCP servers.



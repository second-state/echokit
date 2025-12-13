---
sidebar_position: 3
---

# LLM services

The EchoKit server utilizes LLM services to generate responses to user queries. 
Most popular LLM services support OpenAI API.

| Platform  | URL example | Notes |
| ------------- | ------------- | ---- |
| `openai_chat`  | `https://api.openai.com/v1/chat/completions`  | The stateless `/chat/completions` API. It is the most widely supported LLM API. |
| `openai_responses`  | `https://api.openai.com/v1/responses`  | The stateful `/responses` API. Alpha feature. |


## Simple example

The following example configures the EchoKit server to use the OpenAI LLM service.

```toml
[llm]
platform = "openai_chat"
url = "https://api.openai.com/v1/chat/completions"
api_key = "sk_ABCD"
model = "gpt-5-nano"
history = 5
```

Since the `/v1/chat/completions` API is stateless, the EchoKit server must send the complete chat history
together with the new user query in every request. The `history` parameter specifies how many conversation
turns it should include.

## System prompt

A key feature of modern LLMs is the system prompt, which instructs the LLM how to respond to the user query.
You can specify the speaking style and backgriund knowledge into the system prompt. You can also
specify the available tools (e.g., web search) and actions in the system prompt.

In `config.toml`, you can give the LLM system prompt in the `[[llm.sys_prompts]]` field.

```toml
[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.

- NEVER use bullet points
- NEVER use tables
- Answer in complete English sentences as if you are in a conversation.

"""
```

## Dynamic prompt

EchoKit server can dynamically load web-based content into the system prompt. It is a great tool
for updating the system prompt without having to restart the server itself. In the following example,
the server will load the content from the URL and then replace the `{{ url }}` placeholder.

```toml
[[llm.sys_prompts]]
role = "system"
content = """
{{ https://raw.githubusercontent.com/alabulei1/echokit-dynamic-prompt/refs/heads/main/prompt.txt }}
"""
```

The dynamic system prompt is reloaded only after the EchoKit device restarts with the following events.

* Power-on
* Pressing the RST button

It remains unchanged after normal interruptions or network reconnections.

## Qwen web search

Some LLM service providers support additional JSON structures in the request to accomplish
additional tasks. A good example is Qwen's web search functions. When the additional JSON
data is passed in, the Ali Cloud provider will use the LLM to decide if it needs a web search to
answer the user query. If so, it will perform the web search and have the LLM generate a response 
based on the search results.

In the following example, we are passing the `enable_search = true` parameter to each LLM request. 
We also tells the LLM to use the search tool when needed in the system prompt.

```toml
[llm]
platform = "openai_chat"
url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
api_key = "sk-API-KEY"
model = "qwen-plus"
history = 5

[llm.extra]
enable_search = true

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely.

- NEVER use bullet points
- NEVER use tables
- Answer in complete sentences as if you are in a conversation.
- Use the web_search tool if you need information about current events such as news, political figures, stock prices, and crypto prices.

"""
```

You can pass any JSON parameter supported by the LLM API provider in the `[llm.extra]` field.

## Next step

While the stateless `/v1/chat/completions` API is widely supported, 
OpenAI and many providers in the ecosystem have shifted their focus to the new stateful
`/v1/responses` API. The new responses API makes it easier to support tools, including web searches,
in LLM applications. 


---
sidebar_position: 1
---

# USA civics exam

Immigrants applying for the US citizenship must pass an oral exam to confirm that they have basic knowledge about the US political system. Your EchoKit could act as the immigration officer conducting this exam! **[Get your EchoKit now!](https://echokit.dev/)**

[Watch a video demo](https://x.com/secondstateinc/status/1965544729334218786)

> **Fun fact:** The greatest logician in the 20th centry, Kurt Gödel, discovered a "loophole" in the U.S. Constitution that could allow for dictatorship, which he mentioned during his 1947 *citizenship exam* despite the best efforts of his sponsors, Albert Einstein and Oskar Morgenstern.

Do not have an [EchoKit](https://echokit.dev/) yet? You can try the [text chat version](http://usa.cardea.cc/) for free. :)

## Use our pre-configured EchoKit server

We have an EchoKit server setup to conduct the US Citizenship Civics oral exam. Just [change the EchoKit server config](../server/setup.md) on your device to the following.

```
ws://usa.cardea.cc/ws/
```

## Use your own EchoKit server

You can also configure your own EchoKit server to ask civics QAs and then connect it to your EchoKit device. Please do the following if you have not done so.

* [Run your own EchoKit server](../server/echokit-server.md)
* [Connect EchoKit server to device](../server/setup.md)

Next, configure your EchoKit server to search for QAs when asked.

First, you need to use an MCP server that provides a "tool" for the AI to lookup questions and answers from the official US Citizenship Civics test bank. [Checkout this instructions here](https://github.com/cardea-mcp/ExamPrepAgent). Once you have it setup, add it to the `llm.mcp_server` section in `config.toml`.

```
[[llm.mcp_server]]
server = "http://localhost:8003/mcp"
type = "http_streamable"
```

Then, configure your system prompt to use the MCP tool.

```
[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful test prep expert that asks the user mock exam questions and then helps the user understand the correct answer.

If the user requests a new question, you MUST call the get_random_question() tool. The tool will fetch a JSON structure that contains a question, the answer, and explanation of the answer. You MUST only return the question in the JSON to the user. Respond with the question text only. Do NOT add text before or after the question. Do NOT re-write the question in any way!

After the user answers, you must evaluate whether his answer is correct, and then provide an explanation of the correct answer. The correct answer is contained in the JSON structure from the most recent tool call response. If the user requires more explanation or clarification, you should patiently explain.

When you are finished with a question and explanation session, ask if the user wants to get another question. If the user answer is affirmative, call the get_random_question() tool again for the next question and answer. You could pass a keyword to the get_random_question() tool call to get a new question that is similiar to a past one if the user needs improvement on that subject.

User messages that should trigger the get_random_question() tool call include:
- ask me
- hit me
- next
- next question
- ask me a question
- I got it
- ok
- show me a question
- show me
- hello
- howdy
- start
- sure
- correct
- get started
- I understand
- understood
- alright
"""
```




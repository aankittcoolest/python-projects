import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

f = open("content.org")
content = f.read()
f.close()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
    model="gpt-4o",
)

with open("results.org", "w") as f:
    f.write(chat_completion.choices[0].message.content)

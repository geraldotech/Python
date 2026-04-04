import os

from openai import OpenAI


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


response = client.responses.create(
    model="gpt-5.1",
    input="o que é webhooks?",
    reasoning={
        "effort": "none"
    }
)

print(response)

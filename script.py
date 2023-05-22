from config.config_files import APIkeys
import openai

openai.api_key = APIkeys.APIKey

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Create 10 simple creative sentences for 5-7 year olds:Jack playing with his toy bus.",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

text = response["choices"][0]["text"]

with open("sentences.txt", "a+") as f:
    f.write(text.lstrip() + "\n")

from config.config_files import APIkeys
import openai

openai.api_key = APIkeys.APIKey

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Topic: Breakfast\nTwo-Sentence Horror Story: He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton.\n    \nTopic: Wind\nTwo-Sentence Horror Story:",
    temperature=0.8,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
)
print(response["choices"][0]["text"])

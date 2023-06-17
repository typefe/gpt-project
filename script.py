from config.config_files import APIkeys
import openai

openai.api_key = APIkeys.APIKey


def sentences(n="12", age="5-7"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create {n} simple creative sentences for {age} year olds:Jack playing with his toy bus.",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    text = response["choices"][0]["text"]

    with open("./outputs/sentences.txt", "a+") as f:
        f.write(text.lstrip() + "\n")


def stories(topic):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create a 10-12 sentence story for 5-8 age children about '{topic}' and give a title to your story.",
        temperature=0.8,
        max_tokens=360,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
    )
    story = response["choices"][0]["text"]
    header, story = (
        story.strip().split("\n", 1)[0][7:],
        story.strip().split("\n", 1)[1].strip(),
    )

    file_header = header.replace(" ", "_").lower() + ".txt"

    with open(rf"./outputs/{file_header}", "a+") as f:
        f.write(header + "\n" + story)


if __name__ == "__main__":
    with open("./outputs/sentences.txt", "r") as file:
        contents = file.readlines()
        for i in contents:
            stories(i)

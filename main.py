import os, openai
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5000/v1", api_key="lm-studio")


def send_msg_to_gpt(msg):
    completion = client.chat.completions.create(
        model="model-identifier",
        messages=[
            {"role": "system",
             "content": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability."},
            {"role": "user",
             "content": f"Analyze filedate and identify any suspicous text related to treasure hunt, gift, secret, award or prize.Basically any hidden words related to prize. Start the message with True if keywords are found or False if not found and make it concise.Below is the content of the files.\n\n\n{msg}"}
        ],
        temperature=0.0,
    )

    print(completion.choices[0].message.content)


files_list = []
dir_name = input("Enter directory name: ")
for root, dirs, files in os.walk(dir_name):
    for file in files:
        print(os.path.join(root, file))
        file_content = open(os.path.join(root, file), "r").read()
        send_msg_to_gpt(file_content)

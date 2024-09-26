import argparse
import json
import ollama
from backend.prompt.CareerPromptGenerator import CareerPromptGenerator



def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("usr_answer", type=str, help="The answer of the user")
    parser.add_argument("chat", type=str, help="The whole conversation")
    
    args = parser.parse_args()
    usr_answer = args.usr_answer
    
    chat = [args.chat]

    flattened = []

    if args.chat != "":
        chat_json = [json.loads(msg) for msg in chat]
        flattened = [item for sublist in chat_json for item in sublist]

    i = 0
    for i in range(CareerPromptGenerator.QUESTIONS + 1):
        flattened = predict(flattened, i, usr_answer)

        i += 1
        if i <= CareerPromptGenerator.QUESTIONS:
            usr_answer = input("\n----\n")

    

def predict(chat, count, usr_answer):
    system_prompt = ""
    user_prompt =  ""

    user_prompt = CareerPromptGenerator.generate_prompt("user", count, usr_answer)

    if count == 1:
        system_prompt = CareerPromptGenerator.generate_prompt("system", count)

        chat = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    else:
        chat.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

    return ask_llm(chat)


def ask_llm(chat):
    response = ollama.chat(model='llama3', messages=chat)
    
    chat.append({
        "role": "assistant", 
        "content": response['message']['content']
    })
    print("----\n")
    print(response['message']['content'])
    
    return chat, response['message']['content']


if __name__ == "__main__":
    main()

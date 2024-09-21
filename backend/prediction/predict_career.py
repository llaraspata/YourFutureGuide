import argparse
from langchain_community.llms.ollama import Ollama

from backend.data.utility import get_embedding_function
from backend.prompt.CareerPromptGenerator import CareerPromptGenerator



def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("usr_answer", type=str, help="The answer of the user")
    parser.add_argument("chat", type=str, help="The whole conversation")
    
    args = parser.parse_args()
    usr_answer = args.usr_answer
    chat = args.chat

    print(usr_answer, chat)
    
    generate_question(chat, usr_answer)
    

def generate_question(chat, usr_answer):
    system_prompt = ""
    user_prompt =  ""

    user_prompt = CareerPromptGenerator.generate_prompt("user", len(chat), usr_answer)
    print(user_prompt)

    if len(chat) == 0:
        system_prompt = CareerPromptGenerator.generate_prompt("system", 1)
        print(system_prompt)

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
        print(chat)

    predict(chat)

def predict(chat):
    model = Ollama(model="llama3")
    response_text = model.invoke(chat)
    
    print(response_text)
    
    return response_text


if __name__ == "__main__":
    main()

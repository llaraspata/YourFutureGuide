import argparse
import json
import ollama
from langchain.vectorstores.chroma import Chroma
from backend.data.utility import get_embedding_function
from backend.prompt.DegreePromptGenerator import DegreePromptGenerator


CHROMA_PATH = "/home/llaraspata3/YourFutureGuide/chroma"

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
    for i in range(DegreePromptGenerator.QUESTIONS + 1):
        flattened = generate_question(flattened, i, usr_answer)

        i += 1
        if i <= DegreePromptGenerator.QUESTIONS:
            usr_answer = input("\n----\n")


def generate_question(chat, count, usr_answer):
    system_prompt = ""
    user_prompt =  ""

    sources = []

    if count == 0:
        system_prompt = DegreePromptGenerator.generate_prompt("system", 1)

        chat = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    elif count == 5:
        context, sources = retreive_docs(chat, usr_answer)
        user_prompt = DegreePromptGenerator.generate_prompt("user", count, usr_answer, rag_context=context)

    else:
        user_prompt = DegreePromptGenerator.generate_prompt("user", count, usr_answer)
        chat.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

    return predict(chat, sources)


def predict(chat, sources):
    response = ollama.chat(model='llama3', messages=chat)
    
    chat.append({
        "role": "assistant", 
        "content": response['message']['content']
    })
    print("----\n")
    output_msg = response['message']['content']

    if len(sources) > 0:
        output_msg += f"\n-----------\nSources: {sources}"

    print(output_msg)
    
    return chat


def retreive_docs(chat, last_answer, k=5):
    formatted_query = ""

    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())

    for msg in chat:
        if msg["role"] != "system":
            formatted_query += msg["content"]
    formatted_query += last_answer
    
    results = db.similarity_search_with_score(formatted_query, k)

    context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    sources = [doc.metadata.get("id", None) for doc, _score in results]

    return context, sources


if __name__ == "__main__":
    main()

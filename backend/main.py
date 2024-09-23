import json
from functools import wraps
from http import HTTPStatus
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.ChatPayload import ChatPayload
from prediction import predict_career, predict_degree
from backend.prompt.CareerPromptGenerator import CareerPromptGenerator
from backend.prompt.DegreePromptGenerator import DegreePromptGenerator



tags_metadata = [
    {
        "name": "Root",
        "description": "Explore the root endpoint for essential details, including version, authors, and external links.",
    },
    {
        "name": "Data",
        "description": "Upload documents in the Chroma DB to perform the retreival augmented generation.",
    },
    {
        "name": "Prediction",
        "description": "Chat with LLaMa3 to find either the best educational path or the career one.",
    }
]

APP_DESCRIPTION_MESSAGE = (
    "YourFutureGuide is an LLM-based application to discover what's the best degree or career for a person. The system is currently powered by LLaMa3-7B."
    )


app = FastAPI(
    title="YourFutureGuide",
    description=APP_DESCRIPTION_MESSAGE,
    version="v01",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def construct_response(f):
    """Construct a JSON response for an endpoint's results."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs):
        results = f(request, *args, **kwargs)

        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
        }

        # Additional data in the response
        if "chat_messages" in results:
            response["chat_messages"] = results["chat_messages"]

        if "llm_output" in results:
            response["llm_output"] = results["llm_output"]
            
        if "end_of_chat" in results:
            response["end_of_chat"] = results["end_of_chat"]

        if "version" in results:
            response["version"] = results["version"]

        if "authors" in results:
            response["authors"] = results["authors"]

        if "github" in results:
            response["github"] = results["github"]

        return response

    return wrap


# pylint: disable=unused-argument
@app.get("/", tags=["Root"])
@construct_response
def index(request: Request):
    """Root endpoint.

    **Parameters**
    - No parameters needed

    **Output**
    - A **JSON object** containing the **HTTP message**,
    the **HTTP status code**, a **welcome message*
      and the **names of the system's authors**
    """

    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"message": "Welcome to YourFutureGuide! Please, read the `/docs` if you want to use our system!"},
        "version": "Current: 1.0",
        "authors": ['Laraspata Lucrezia'],
        'github': 'https://github.com/llaraspata/YourFutureGuide.git',
    }

    return response

@app.post('/predict/career', tags=["Prediction"])
@construct_response
def ask_llm(request: Request, chat_payload: ChatPayload):
    """
    TODO
    """

    chat_messages = []

    if chat_payload.chat != "":
        chat_json = [json.loads(msg) for msg in chat_payload.chat]
        chat_messages = [item for sublist in chat_json for item in sublist]
        
    chat_messages, llm_output = predict_career.predict(chat_messages, chat_payload.qst_count, chat_payload.usr_answer)

    response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "chat_messages": chat_messages,
            "llm_output": llm_output,
            "end_of_chat": chat_payload.qst_count >= CareerPromptGenerator.QUESTIONS
        }

    return response


@app.post('/predict/degree', tags=["Prediction"])
@construct_response
def ask_llm(request: Request, chat_payload: ChatPayload):
    """
    TODO
    """
    chat_messages, llm_output = predict_degree.predict(chat_payload.chat, chat_payload.qst_count, chat_payload.usr_answer)

    response = {
            "message": HTTPStatus.OK.phrase,
            "status-code": HTTPStatus.OK,
            "chat_messages": chat_messages,
            "llm_output": llm_output,
            "end_of_chat": chat_payload.qst_count >= DegreePromptGenerator.QUESTIONS
        }

    return response
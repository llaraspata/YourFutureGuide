from pydantic import BaseModel

class ChatPayload(BaseModel):
    """
        Chat Payload
    """
    usr_answer: str
    chat: list
    qst_count: int
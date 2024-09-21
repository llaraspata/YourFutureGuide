"""
TODO
"""
from backend.prompt.degree_prompts import BestDegreeSystemPrompt as SystemPrompt
from backend.prompt.degree_prompts import BestDegreeUserPrompt as UserPrompt


class DegreePromptGenerator:
    QUESTIONS = 5

    # ------------
    # Prompt generation
    # ------------
    def generate_prompt(role, qst_count, usr_answer="", rag_context=""):
        """
            TODO
        """
        prompt = ""

        if role == "system":
            prompt = SystemPrompt.ROLE_DEFINITION
            prompt += SystemPrompt.CHAT_FLOW_DEFINITION
            prompt += SystemPrompt.OUTPUT_WITH_RAG_DEFINITION

        elif role == "user":
            if usr_answer:
                if qst_count < DegreePromptGenerator.QUESTIONS:
                    prompt = UserPrompt.ANSWER % (usr_answer)
                else:
                    prompt = UserPrompt.LAST_ANSWER % (usr_answer, rag_context)

        return prompt

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
    def generate_prompt(role, qst_count=-1, usr_answer="", rag_context="", ask_for_interest=False):
        """
            TODO
        """
        prompt = ""

        if role == "system":
            prompt += SystemPrompt.ROLE_DEFINITION
            prompt += SystemPrompt.CHAT_FLOW_DEFINITION
            prompt += SystemPrompt.OUTPUT_WITH_RAG_DEFINITION

        elif role == "user":
            if usr_answer:
                if ask_for_interest:
                    prompt = UserPrompt.ASK_INTERESTS % (usr_answer)
                elif qst_count < DegreePromptGenerator.QUESTIONS:
                    prompt = UserPrompt.ANSWER % (usr_answer)
                else:
                    prompt = UserPrompt.LAST_ANSWER % (usr_answer, rag_context)

        return prompt

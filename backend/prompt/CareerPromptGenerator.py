"""
TODO
"""
from backend.prompt.career_prompts import BestCareerSystemPrompt as SystemPrompt
from backend.prompt.career_prompts import BestCareerUserPrompt as UserPrompt


class CareerPromptGenerator:
    QUESTIONS = 5

    # ------------
    # Prompt generation
    # ------------
    def generate_prompt(role, qst_count, usr_answer=""):
        """
            TODO
        """
        prompt = ""

        if role == "system":
            prompt = SystemPrompt.ROLE_DEFINITION
            prompt = SystemPrompt.CHAT_FLOW_DEFINITION
            prompt = SystemPrompt.OUTPUT_DEFINITION

        elif role == "user":
            if usr_answer:
                if qst_count < CareerPromptGenerator.QUESTIONS:
                    prompt = UserPrompt.ANSWER % (usr_answer)
                else:
                    prompt = UserPrompt.LAST_ANSWER % (usr_answer)
    
        return prompt
        
"""
TODO
"""
from backend.prompt.career_prompts import BestCareerSystemPrompt as SystemPrompt
from backend.prompt.career_prompts import BestCareerUserPrompt as UserPrompt


class CareerPromptGenerator:
    QUESTIONS = 5

    # ------------
    # Constructor
    # ------------
    def __init__(self, role):
        self.role = role
        self.prompt = ""


    # ------------
    # Prompt generation
    # ------------
    def generate_prompt(self, qst_count, usr_answer=""):
        """
            TODO
        """

        if self.role == "system":
            self._generate_system_prompt()

        elif self.role == "user":
            self._generate_user_prompt(qst_count, usr_answer)

        return self.prompt


    def _generate_system_prompt(self):
        """
        TODO
        """
        self.prompt = SystemPrompt.ROLE_DEFINITION
        self.prompt = SystemPrompt.CHAT_FLOW_DEFINITION
        self.prompt = SystemPrompt.OUTPUT_DEFINITION
        

    def _generate_user_prompt(self, qst_count, usr_answer):
        """
        TODO
        """
        if qst_count < 5:
            self.prompt = UserPrompt.ANSWER % (usr_answer)
        else:
            self.prompt = UserPrompt.LAST_ANSWER % (usr_answer)

"""
TODO
"""

class BestCareerSystemPrompt:
    ROLE_DEFINITION = """Sei un assistente che aiuta le persone a scegliere il miglior percorso professionale."""

    CHAT_FLOW_DEFINITION = """Dovrai fare 5 domande alla persona per capire quali sono i suoi interessi, le sue passioni, e le sue aspirazioni."""

    OUTPUT_DEFINITION = """Quando la persona te lo chiederà, dovrai suggerire il lavoro e dare una spiegazione per quella scleta."""


class BestCareerUserPrompt:
    ANSWER = ""

    LAST_ANSWER = """%s
    
    In base a quello che ci siamo detti, mi sapresti dire quale lavoro si addice a me?"""

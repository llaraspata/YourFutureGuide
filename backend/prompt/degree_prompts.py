"""
TODO
"""

class BestDegreeSystemPrompt:
    ROLE_DEFINITION = """Sei un assistente che aiuta gli studenti a scegliere il miglior percorso di studi. """

    CHAT_FLOW_DEFINITION = """Dovrai fare 5 domande allo studente per capire quali sono i suoi interessi e le sue passioni. """

    OUTPUT_WITH_RAG_DEFINITION = """Quando lo studente te lo chiederà, dovrai suggerire il corso di laurea in base al contesto che ti verrà fornito e dare una spiegazione per quella scleta."""


class BestDegreeUserPrompt:
    ANSWER = ""

    LAST_ANSWER = """%s
    
    In base a quello che ci siamo detti e al seguente contesto, mi sapresti dire quale percorso di studi si addice a me?
    
    ### CONTESTO
    %s"""

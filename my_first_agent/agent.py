from google.adk.agents.llm_agent import Agent

root_agent = LlmAgent(
    model='gemini-3.6-flash', #Modelo do agente LLMS
    name='support_specialist', #Name do agente
    description='Agente de suporte ao cliente profissional com definição e limites claros do papel', #Resumo da função do agente
    instruction="""
    # Sua identidade
    # (Padrão 1: identidade – estabelece a persona e a experiência)
    Você é Alex Chen, especialista sênior em suporte técnico com 5 anos de experiência.


    

    
    """
)

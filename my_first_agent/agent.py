from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    # Modelo escolhido para (LLM) - resposnãvel pela tomada de decisões do agente.
    name='root_agent',
    # Identificador de string do agente.
    description='A helpful assistant for user questions.',
    # Resumo do objetivo do agente, utilizado melhor para multiagente.
    instruction='Answer user questions to the best of your knowledge',
    # Plano comportamental descrito de como o agente age.

)

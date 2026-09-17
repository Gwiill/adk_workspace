from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',

    # Modelo escolhido para (LLM) - resposnãvel pela tomada de decisões do agente.
    name='math_tutor_agent',

    # Identificador de string do agente.
    description='Ajuda estudantes a aprender álgebra com orientação pelas etapas de solução de problemas.'

    # Resumo do objetivo do agente, utilizado melhor para multiagente.
    instruction='Você é um orientador de matemática paciente. Ajude os estudantes a resolver problemas de álgebra.'

    # Plano comportamental descrito de como o agente age.



)

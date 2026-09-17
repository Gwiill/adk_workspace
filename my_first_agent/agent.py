from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.6-flash', #Modelo do agente LLMS
    name='math_tutor_agent', #Name do agente
    description='Ajuda estudantes a aprender álgebra com gírias e falta de profissionalismo.', #Resumo da função do agente
    instruction='Você é um orientador de matemática sem empatia, estúpido e arrogante. Ajude os estudantes a resolver problemas de álgebra.', #É o tipo de comportamento do agente
)


#- ✅ Definição específica do papel (orientador de matemática)
#- ✅ Personalidade clara (paciente)
#- ✅ Definição do escopo da tarefa (problemas de álgebra)
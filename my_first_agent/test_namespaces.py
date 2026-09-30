"""
Script de Teste Programático para o Agente Alex Chen.
Demonstra a injeção e ciclo de vida dos Namespaces de Estado (app, user, session, temp).
Execute no terminal com: python test_namespaces.py
"""
import json
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# 1. Configurar o Serviço de Sessão e o Runner
session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="helpdesk_system",
    user_id="cliente_123", # ID único do usuário
    session_id="ticket_001" # ID desta conversa específica
)

runner = Runner(
    agent=root_agent,
    app_name="helpdesk_system",
    session_service=session_service
)

# 2. Populando os Namespaces de Estado ANTES da execução
print("=== PREENCHENDO O ESTADO INICIAL ===")
session.state["app:company_name"] = "Google Brasil" # Global para todos
session.state["user:name"] = "Guilherme"            # Persiste para o usuário
session.state["user:support_tier"] = "VIP"          # Persiste para o usuário
session.state["user:language"] = "Português"        # Persiste para o usuário
session.state["session_topic"] = "Problema de Login"# Morre quando o ticket fechar
session.state["temp:current_step"] = "Triagem"      # Morre assim que o agente responder

print(f"Estado antes do turno: {session.state}\n")

# 3. Executando o Agente
print("=== EXECUTANDO O AGENTE (TURNO 1) ===")
mensagem_usuario = Content(parts=[Part(text="Não estou conseguindo acessar minha conta no painel.")])

resultado = runner.run(
    user_id="cliente_123",
    session_id="ticket_001",
    new_message=mensagem_usuario
)

# Exibindo a resposta final
for event in resultado:
    if event.is_final_response():
        # Como exigimos JSON via Pydantic, vamos formatar bonitinho na tela
        resposta_json = json.loads(event.content.parts[0].text)
        print(f"Mensagem para o cliente: {resposta_json['resposta_cliente']}")
        print(f"Status Interno: {resposta_json['status_resolucao']}\n")

# 4. Verificando a sobrevivência dos Estados
print("=== VERIFICAÇÃO DE PERSISTÊNCIA (PÓS-TURNO 1) ===")
print(f"temp:current_step: {session.state.get('temp:current_step')} (PERDIDO - Escopo temp:)")
print(f"session_topic: {session.state.get('session_topic')} (PERSISTIU - Escopo da sessão)")
print(f"user:name: {session.state.get('user:name')} (PERSISTIU - Escopo do usuário)")
print(f"app:company_name: {session.state.get('app:company_name')} (PERSISTIU - Escopo do app)")

print(f"\nVariável gerada automaticamente pelo output_key do agente:")
print(f"support_ticket_result: {session.state.get('support_ticket_result')[:50]}... (JSON salvo no estado!)")
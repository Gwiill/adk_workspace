import os
from dotenv import load_dotenv

# Carrega a chave de API do arquivo .env ANTES de iniciar o agente
load_dotenv(override=True)

from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from pydantic import BaseModel, Field
from google.genai import types
from typing import Optional

# 1. DEFINIÇÃO DO CONTRATO DE DADOS (PYDANTIC)
class SupportTicketResponse(BaseModel):
    resposta_cliente: str = Field(description="A mensagem empática (OBRIGATORIAMENTE EM PORTUGUÊS) que será exibida para o cliente, seguindo os 4 passos da metodologia.")
    status_resolucao: str = Field(description="Status final do atendimento: 'resolvido', 'aguardando_cliente' ou 'escalonado'.")
    equipe_escalonamento: Optional[str] = Field(default=None, description="Se o ticket foi escalonado, informe a equipe (ex: faturamento, produtos, engenharia, segurança). Caso contrário, retorne null.")

# 2. CONFIGURAÇÃO DO AGENTE
root_agent = LlmAgent(
    model="gemini-3.8-flash", 
    name="support_specialist",
    description="Agente de suporte ao cliente profissional com definição e limites claros do papel",
    
    # 3. CONFIGURAÇÃO DE RACIOCÍNIO (PLANNER)
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True, 
            thinking_budget=1024 
        )
    ),
    
    # 4. CONFIGURAÇÃO DO MODELO (TEMPERATURA)
    generate_content_config=types.GenerateContentConfig(
        temperature=0.5, 
    ),
    
    # 5. APLICAÇÃO DO ESQUEMA DE SAÍDA E ESTADO
    output_schema=SupportTicketResponse,
    output_key="support_ticket_result", # Salvará o JSON final no estado da sessão

    # 6. INSTRUÇÃO COM INJEÇÃO DINÂMICA DE ESTADO (TEMPLATES)
    instruction="""
    # Sua identidade
    Você é Alex Chen, especialista sênior em suporte técnico da empresa {app:company_name?TechCorp Enterprise}.

    # Informações do Cliente (Persiste em todas as sessões)
    - Nome do Cliente: {user:name?Cliente VIP}
    - Nível de Suporte: {user:support_tier?Standard}
    - Idioma de preferência: {user:language?Português}

    # Contexto Atual (Persiste apenas nesta sessão)
    - Tópico do Atendimento: {session_topic?Não categorizado}
    - Fase atual do processamento (Temporário): {temp:current_step?Analisando solicitação inicial}

    # Sua missão 
    Ajudar o cliente a resolver problemas técnicos com eficiência e profissionalismo.
    Se o 'Nível de Suporte' for Premium ou VIP, ofereça um atendimento ainda mais prioritário.

    # Como você trabalha
    1. **Reconhecer**: demonstre empatia pela situação do cliente. Sempre chame-o pelo nome ({user:name?Cliente VIP}).
    2. **Esclarecer**: faça perguntas específicas para entender o problema
    3. **Resolver**: ofereça soluções claras e detalhadas
    4. **Verificar**: confirme se o problema foi totalmente solucionado

    # Estilo de comunicação
    - Profissional, mas amigável
    - Claro e sem jargões
    - Paciente e empático
    - Responda obrigatoriamente em: {user:language?Português}
    
    # Seus limites
    - Nunca forneça acesso a conta, senhas ou redefinições de senha
    - Nunca dê conselhos jurídicos, financeiros ou médicos
    - Nunca adivinhe as soluções. Sempre peça esclarecimentos primeiro

    # FORMATO DE SAÍDA (IMPORTANTE)
    Você deve extrair as informações do atendimento e responder APENAS com um objeto JSON válido.
    NUNCA inclua texto explicativo fora do JSON.
    """
)
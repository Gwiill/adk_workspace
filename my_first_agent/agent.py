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
    resposta_cliente: str = Field(description="A mensagem profissional e empática que será exibida para o cliente, seguindo os 4 passos da metodologia.")
    status_resolucao: str = Field(description="Status final do atendimento: 'resolvido', 'aguardando_cliente' ou 'escalonado'.")
    equipe_escalonamento: Optional[str] = Field(default=None, description="Se o ticket foi escalonado, informe a equipe (ex: faturamento, produtos, engenharia, segurança). Caso contrário, retorne null.")

# 2. CONFIGURAÇÃO DO AGENTE
root_agent = LlmAgent(
    model="gemini-3.8-flash", # Corrigido para 2.5-flash conforme recomendado para produção e velocidade
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
    
    # 5. APLICAÇÃO DO ESQUEMA DE SAÍDA
    output_schema=SupportTicketResponse,
    output_key="support_ticket_result", 

    instruction="""
    # Sua identidade
    Você é Alex Chen, especialista sênior em suporte técnico com 5 anos de experiência.

    # Sua missão 
    Ajudar os clientes a resolver problemas técnicos com eficiência e profissionalismo.

    # Como você trabalha
    1. **Reconhecer**: demonstre empatia pela situação do cliente
    2. **Esclarecer**: faça perguntas específicas para entender o problema
    3. **Resolver**: ofereça soluções claras e detalhadas
    4. **Verificar**: confirme se o problema foi totalmente solucionado

    # Estilo de comunicação
    - Profissional, mas amigável
    - Claro e sem jargões
    - Paciente e empático
    - Conciso (menos de 200 palavras, a menos que os detalhes sejam fundamentais)
    
    # Seus limites
    **Importante**: os limites funcionam em conjunto com as configurações de segurança integradas do modelo para garantir respostas adequadas e úteis.

    ## O que você nunca deve fazer
    - Nunca forneça acesso a conta, senhas ou redefinições de senha
    - Nunca compartilhe informações sobre outros clientes
    - Nunca faça promessas sobre recursos, cronogramas ou reembolsos
    - Nunca dê conselhos jurídicos, financeiros ou médicos

    ## Como você mantém a qualidade
    - Sempre embase as respostas em fatos e informações disponíveis
    - Nunca invente detalhes técnicos ou estatísticas
    - Se você não souber algo, admita e se ofereça para encaminhar o problema
    - Nunca adivinhe as soluções. Sempre peça esclarecimentos primeiro

    ## Quando encaminhar
    Direcione imediatamente as seguintes questões para a equipe apropriada:
    - Perguntas sobre faturamento - equipe de faturamento
    - Solicitações de recursos - equipe de produtos
    - Relatórios de bugs - equipe de engenharia
    - Segurança da conta - equipe de segurança

    # FORMATO DE SAÍDA (IMPORTANTE)
    Você deve extrair as informações do atendimento e responder APENAS com um objeto JSON válido.
    NUNCA inclua texto explicativo fora do JSON.
    """
)
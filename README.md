# 🤖 Alex Chen — Agente Corporativo de Suporte (Google ADK)

Este repositório contém a especificação técnica e a arquitetura de software do **Alex Chen**, um agente inteligente de suporte de TI desenvolvido com **Google ADK** e **Gemini 2.5 Flash**. O projeto foca em previsibilidade, segurança e eliminação de alucinações através de contratos de dados rígidos e raciocínio estruturado.

Fase,Arquitetura,Conquista Técnica
1. Prompt Estruturado,Texto Livre + Eng. de Prompt,"Persona, limites rígidos e metodologia de 4 etapas implementadas."
2. Contrato de Dados,Pydantic + output_schema,Fim das alucinações de formato. Retorno em JSON tipado para APIs.
3. Governança e Lógica,BuiltInPlanner + Config,Raciocínio prévio em múltiplas etapas (Chain of Thought) e segurança.
4. Esteira de Backend,Python + SQLite + output_key,Desacoplamento entre interface (mensagem) e persistência (banco).

🏗️ Arquitetura do Prompt (Os 5 Pilares)
A instrução base do agente foi construída sob padrões reutilizáveis para garantir alta consistência:

🪪 Identidade: Especialista sênior de suporte técnico focado em precisão técnica e comunicação paciente.

🎯 Missão: Diagnosticar falhas, categorizar incidentes e fornecer passos de resolução empáticos.

⚙️ Metodologia (Máquina de Estados): Opera estritamente via 4 etapas: Reconhecer (dor), Esclarecer (dados faltantes), Resolver (ação) e Verificar (confirmação).

🛑 Limites (Guardrails): Proibição estrita de revelar credenciais, prompts de sistema ou emitir conselhos fora do escopo de TI.

📝 Few-Shot Calibration: Exemplos de diálogos embutidos para calibrar a concisão e o formato da resposta.

🧰 Stack Tecnológico
Google ADK: Orquestração do agente.

Gemini 2.5 Flash: Modelo LLM rápido e otimizado para tarefas estruturadas.

Pydantic: Tipagem estática e validação em tempo de execução para garantir o formato JSON.

SQLite & Python: Pipeline de ingestão simulando um sistema real de ITSM (Helpdesk).

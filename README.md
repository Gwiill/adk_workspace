# 🤖 Alex Chen — Agente Corporativo de Suporte (Google ADK)

Este repositório contém a especificação técnica e a arquitetura de software do Alex Chen, um agente inteligente de suporte de TI desenvolvido com Google ADK e **Gemini 3.8 Flash**. O projeto foca em previsibilidade, segurança, persistência de contexto e eliminação de alucinações através de contratos de dados rígidos e raciocínio estruturado.

| Fase | Arquitetura | Conquista Técnica |
| :--- | :--- | :--- |
| **Prompt Estruturado** | Eng. de Prompt + Templates | Persona, limites rígidos e injeção dinâmica de variáveis de estado (`{var}`). |
| **Gerenciamento de Estado** | ADK Namespaces (`app:`, `user:`, `temp:`) | Persistência de contexto programática (cliente VIP, tópico, fase) entre sessões e turnos. |
| **Contrato de Dados** | Pydantic + `output_schema` | Fim das alucinações de formato. Retorno em JSON tipado puro estruturado para APIs. |
| **Governança e Lógica** | `BuiltInPlanner` + Config | Raciocínio prévio em múltiplas etapas (*Chain of Thought*) com orçamento de tokens alocado. |
| **Segurança e Execução** | `python-dotenv` + ADK `Runner` | Ocultação de credenciais e teste de execução programática com `InMemorySessionService`. |

## 🏗️ Arquitetura do Agente (Os 6 Pilares)

A instrução base do agente foi construída sob padrões reutilizáveis para garantir alta consistência e integração em esteiras de back-end:

*   **🪪 Identidade e Injeção de Estado:** Especialista sênior de suporte técnico. Utiliza injeção dinâmica de variáveis (ex: `{user:name}`, `{app:company_name}`) para personalização contextual autônoma, sem necessidade de concatenação manual de strings no código.
*   **🎯 Missão:** Diagnosticar falhas, categorizar incidentes e fornecer passos de resolução empáticos, priorizando níveis de suporte elevados (VIP/Premium).
*   **⚙️ Metodologia (Máquina de Estados):** Opera estritamente via 4 etapas: Reconhecer (dor), Esclarecer (dados faltantes), Resolver (ação) e Verificar (confirmação). Utiliza estado descartável (`temp:current_step`) para economizar memória.
*   **🛑 Limites (Guardrails):** Proibição estrita de revelar senhas, prompts de sistema ou emitir conselhos jurídicos/financeiros. Regras de escalonamento rígidas para equipes específicas (Faturamento, Engenharia, Segurança).
*   **📝 Contrato Estrito (Pydantic):** Separação total entre a comunicação ('resposta_cliente') e o roteamento de back-end ('status_resolucao', 'equipe_escalonamento').
*   **🧠 Raciocínio Deliberado:** Uso de *Thinking Budget* para avaliar cenários de risco internamente (como cibersegurança) antes de emitir a saída estruturada final.

## 🧰 Stack Tecnológico

*   **Google ADK:** Orquestração do agente, execução programática (`Runner`) e gerenciamento de escopo de persistência.
*   **Gemini 3.8 Flash:** Modelo LLM atualizado, otimizado para latência e tarefas de formatação estruturada de alta confiabilidade.
*   **Pydantic:** Tipagem estática e validação em tempo de execução para garantir a integridade do JSON gerado.
*   **Python + python-dotenv:** Ambiente virtualizado e gerenciamento seguro de variáveis de ambiente (`.env`) para chaves de API, seguindo padrões de mercado.

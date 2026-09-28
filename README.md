# 🤖 Alex Chen — Agente Corporativo de Suporte (Google ADK)

Este repositório contém a especificação técnica e a arquitetura de software do **Alex Chen**, um agente inteligente de suporte de TI desenvolvido com **Google ADK** e **Gemini 2.5 Flash**. O projeto foca em previsibilidade, segurança e eliminação de alucinações através de contratos de dados rígidos e raciocínio estruturado.

Fase,Arquitetura,Conquista Técnica
1. Prompt Estruturado,Texto Livre + Eng. de Prompt,"Persona, limites rígidos e metodologia de 4 etapas implementadas."
2. Contrato de Dados,Pydantic + output_schema,Fim das alucinações de formato. Retorno em JSON tipado para APIs.
3. Governança e Lógica,BuiltInPlanner + Config,Raciocínio prévio em múltiplas etapas (Chain of Thought) e segurança.
4. Esteira de Backend,Python + SQLite + output_key,Desacoplamento entre interface (mensagem) e persistência (banco).

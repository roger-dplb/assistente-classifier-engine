# 💡 Explicação (Explanation)

Documentação conceitual para entender como o sistema funciona.

## O que são Explicações?

Explicações são **discussões** que aprofundam o entendimento:
- 🧠 **Contexto e background** - por que algo existe
- 🔗 **Conexões** - como diferentes partes se relacionam
- 📖 **História** - evolução e decisões de design
- 💡 **Insights** - compreensão profunda do sistema

> ⚠️ **Não são tutoriais nem referência!** Leia quando quiser *entender*, não quando quiser *fazer*.

## 📚 Tópicos Disponíveis

### Arquitetura & Design
- **[arquitetura.md](./arquitetura.md)** - Visão geral da arquitetura do sistema
- **[pipeline-llm.md](./pipeline-llm.md)** - Como o processamento com LLM funciona
- **[fluxo-dados.md](./fluxo-dados.md)** - Jornada dos dados pelo sistema

### Conceitos do Domínio
- **[taxonomia.md](./taxonomia.md)** - Entenda a estrutura de classificação
- **[metricas-qualidade.md](./metricas-qualidade.md)** - Como avaliamos a qualidade
- **[golden-dataset.md](./golden-dataset.md)** - Propósito e uso do dataset de validação

### Decisões Técnicas
- **[escolha-modelo-llm.md](./escolha-modelo-llm.md)** - Por que usamos GPT-4
- **[prompt-versioning.md](./prompt-versioning.md)** - Estratégia de versionamento de prompts
- **[api-vs-streamlit.md](./api-vs-streamlit.md)** - Separação backend/frontend

## 📝 Template para Novas Explicações

```markdown
# Título da Explicação

## 💡 Conceito Central
O que é este conceito em uma frase

## 📖 Contexto
Por que isso existe? Qual problema resolve?

## 🔍 Como Funciona
Explicação detalhada do funcionamento

## 🌐 Relações
Como isso se conecta com outras partes:
- [Link para conceito relacionado]
- [Link para implementação]

## 📚 História/Evolução
Como chegamos até aqui (se relevante)

## 🎯 Implicações
O que isso significa para:
- Usuários
- Desenvolvedores
- Sistema

## 📚 Leituras Relacionadas
- [Link para tutoriais]
- [Link para referência]
```

---

**⬅️ Voltar para [Documentação Principal](../README.md)**

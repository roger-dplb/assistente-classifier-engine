# PRD — Sistema de Autoetiquetagem Inteligente de Atendimentos

**Versão:** 1.0  
**Status:** Em definição  
**Escopo:** Camada de processamento e inteligência (sem integração com sistemas externos)

---

## 1. Visão Geral

Desenvolver um motor de autoetiquetagem baseado em LLM capaz de classificar atendimentos automaticamente, avaliar a qualidade do atendimento humano, gerar resumos executivos, extrair tópicos estruturados e produzir relatórios analíticos.

---

## 2. Problema

A análise manual de atendimentos é lenta, custosa e não escala. Os principais impactos são:

- Falta de padronização nas avaliações
- Alto esforço operacional sem retorno proporcional
- Dificuldade de gerar insights estratégicos a partir do volume de interações

---

## 3. Objetivos

### 3.1 Objetivos Principais

- Automatizar a etiquetagem de atendimentos
- Padronizar a avaliação de qualidade
- Gerar inteligência acionável para times de operação e gestão
- Criar base estruturada para analytics contínuo

### 3.2 Métricas de Sucesso

| Métrica | Meta |
|---|---|
| Concordância com dataset validado | ≥ 85% |
| Redução do esforço manual de análise | ≥ 70% |
| Tempo médio de processamento por atendimento | < 5 segundos |
| Consistência de output estruturado | ≥ 99% |

---

## 4. Escopo



- Definição de taxonomia
- Processamento via LLM
- Geração de etiquetas e score de qualidade
- Resumos automáticos e extração de tópicos
- Processamento individual e em lote
- Relatórios estruturados
- Interface simples de validação humana
- Documentação técnica

---

## 5. Funcionalidades

### 5.1 Taxonomia de Etiquetas

**Classificação Principal**

| Dimensão | Descrição |
|---|---|
| Categoria | Tema principal do atendimento |
| Intenção | O que o cliente deseja |
| Sentimento | Positivo, neutro ou negativo |
| Criticidade | Nível de urgência / impacto |
| SLA / Urgência | Prazo esperado de resolução |

**Avaliação de Qualidade** *(escala 0–10)*

| Critério | Descrição |
|---|---|
| Empatia | Capacidade de se colocar no lugar do cliente |
| Clareza | Qualidade da comunicação |
| Objetividade | Foco e precisão nas respostas |
| Resolutividade | Efetividade na resolução do problema |
| **Score Consolidado** | **Média ponderada dos critérios acima** |

---

### 5.2 Geração Automática

Para cada atendimento processado, o sistema gera:

- **Resumo executivo** — máximo 5 linhas
- **Lista de tópicos principais** — itens-chave abordados
- **Justificativa da classificação** — raciocínio do modelo
- **Output estruturado em JSON** — pronto para integração

**Exemplo de saída:**

```json
{
  "categoria": "Financeiro",
  "intencao": "Solicitação de reembolso",
  "sentimento": "Negativo",
  "criticidade": "Alta",
  "sla_urgencia": "24h",
  "qualidade": {
    "empatia": 7,
    "clareza": 8,
    "objetividade": 9,
    "resolutividade": 6,
    "score_final": 7.5
  },
  "resumo": "Cliente solicitou reembolso por cobrança duplicada...",
  "topicos": ["Cobrança duplicada", "Solicitação de reembolso", "Prazo de retorno"]
}
```

---

### 5.3 Processamento

- **Entrada:** Texto bruto do atendimento
- **Modo individual:** Processamento de atendimento único
- **Modo em lote:** Upload de arquivo CSV ou JSON
- **Saída:** Retorno padronizado em JSON

---

### 5.4 Humano no Loop

- Interface para revisão e correção manual de etiquetas
- Registro de divergências entre classificação automática e humana
- Log de auditoria completo das ações realizadas

---

### 5.5 Relatórios Analíticos

**Conteúdo dos relatórios:**

- Distribuição por categoria
- Tendência de sentimento ao longo do tempo
- Índice médio de qualidade
- Tópicos mais recorrentes
- Ranking de criticidade

**Formatos de exportação:** JSON, CSV e PDF *(opcional)*

---

## 6. Arquitetura

```
┌─────────────────────┐
│  Ingestão de Texto  │  ← Texto bruto / CSV / JSON
└────────┬────────────┘
         │
┌────────▼────────────┐
│  Processamento LLM  │  ← Classificação + Qualidade + Resumo
└────────┬────────────┘
         │
┌────────▼────────────┐
│ Validação Humana    │  ← Revisão, correção, log de auditoria
└────────┬────────────┘
         │
┌────────▼────────────┐
│ Consolidação Analít.│  ← Relatórios, tendências, exportação
└─────────────────────┘
```

---

## 7. Requisitos Não Funcionais

| Requisito | Detalhe |
|---|---|
| Tempo de resposta | < 5 segundos por atendimento |
| Consistência de estrutura | Alta — output JSON padronizado |
| Auditabilidade | Logs completos de todas as operações |
| Escalabilidade | Suporte a processamento em lote |
| Versionamento | Controle de versão de prompts |

---

## 8. Riscos e Mitigações

| Risco | Mitigação |
|---|---|
| Inconsistência de classificação | Golden dataset para validação contínua |
| Ambiguidade em atendimentos curtos | Regras de fallback e flags de baixa confiança |
| Dependência da qualidade do input | Pré-processamento e normalização de texto |
| Drift sem validação contínua | Revisão periódica e ajuste iterativo de prompts |

---

## 9. Entregáveis

- [ ] Motor funcional de autoetiquetagem
- [ ] Dataset validado (golden dataset)
- [ ] Relatórios analíticos estruturados
- [ ] Interface básica de revisão humana
- [ ] Documentação técnica completa
- [ ] Guia para futura integração com sistemas externos

---

## 10. Roadmap

```
Fase 1 → Definição de taxonomia
Fase 2 → Construção do dataset base
Fase 3 → Implementação do pipeline LLM
Fase 4 → Validação humano no loop
Fase 5 → Consolidação analítica
Fase 6 → Documentação e entrega
```
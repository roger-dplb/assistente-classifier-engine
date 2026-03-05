# 📚 Documentação do Projeto

Esta pasta contém toda a documentação do Sistema de Autoetiquetagem Inteligente, organizada seguindo o **Padrão Diátaxis**.

## 🏛️ Padrão Diátaxis

O Diátaxis é uma estrutura de documentação técnica que organiza o conteúdo em 4 quadrantes:

```
                    +------------------+------------------+
                    |                  |                  |
      PRÁTICA       │    Tutoriais     │   Como Fazer     │
      (Practical)   │   (Tutorials)    │  (How-To Guides) │
                    │                  │                  |
                    +------------------+------------------+
      TEORIA        │    Explicação    │    Referência    │
      (Theoretical) │  (Explanation)   │   (Reference)    │
                    │                  │                  |
                    +------------------+------------------+
                    
                    ESTUDO ←─────────→ TRABALHO
                    (Learning)       (Doing)
```

## 📁 Estrutura de Pastas

```
docs/
├── README.md              # Este arquivo - guia da documentação
├── PRD.md                 # Product Requirements Document
├── tutorials/             # 🎓 Tutoriais - aprendizado passo a passo
│   ├── README.md
│   ├── 01-setup.md      # Configuração inicial
│   ├── 02-primeira-classificacao.md
│   └── 03-validacao-humana.md
├── how-to/               # 🛠️ Como Fazer - guias práticos
│   ├── README.md
│   ├── adicionar-categoria.md
│   ├── atualizar-prompts.md
│   ├── processar-lote-csv.md
│   └── avaliar-metricas.md
├── explanation/          # 💡 Explicação - entendimento conceitual
│   ├── README.md
│   ├── arquitetura.md
│   ├── taxonomia.md
│   ├── pipeline-llm.md
│   └── metricas-qualidade.md
└── reference/            # 📖 Referência - informações técnicas
    ├── README.md
    ├── api-endpoints.md
    ├── models-pydantic.md
    ├── config-env.md
    └── comandos-cli.md
```

## 🎯 Quando Usar Cada Tipo

| Tipo | Use quando | Exemplo |
|------|-----------|---------|
| **Tutorial** | Aprender algo novo do zero | "Primeiros passos com a API" |
| **Como Fazer** | Resolver um problema específico | "Como adicionar uma nova categoria" |
| **Explicação** | Entender como algo funciona | "Como o pipeline de LLM processa atendimentos" |
| **Referência** | Consultar detalhes técnicos | "Lista de endpoints da API" |

## 📝 Convenções de Escrita

### Tutoriais
- Orientação passo a passo
- Resultado garantido no final
- Foco no aprendizado, não na explicação
- Começar do zero

### Como Fazer
- Problema → Solução
- Sem contexto desnecessário
- Passos práticos e diretos
- Assume conhecimento prévio

### Explicação
- Contexto e background
- Por que algo funciona assim
- Conexões entre conceitos
- História e evolução

### Referência
- Factual e preciso
- Organizado para consulta rápida
- Sem narrativa
- Completo e exaustivo

## 🔗 Links Úteis

- [Site oficial Diátaxis](https://diataxis.fr/)
- [PRD do Projeto](./PRD.md)
- [README principal](../README.md)

---

**💡 Dica:** Se você está começando no projeto, vá para [tutorials/01-setup.md](./tutorials/01-setup.md)

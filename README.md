# Sistema de Autoetiquetagem Inteligente de Atendimentos

Motor de classificação automática de atendimentos usando LLM, com avaliação de qualidade, geração de resumos e interface de validação humana.

## 🚀 Tecnologias

- **Backend:** FastAPI + Python 3.11+
- **Frontend:** Streamlit
- **LLM:** OpenAI GPT-4 ou superior
- **Processamento:** Pandas, NumPy
- **Relatórios:** JSON, CSV

## 📁 Estrutura do Projeto

```
.
├── api/                    # Backend FastAPI
│   ├── __init__.py
│   ├── main.py            # Entry point da API
│   ├── routes/            # Endpoints
│   │   ├── __init__.py
│   │   ├── classify.py    # Classificação de atendimentos
│   │   ├── batch.py       # Processamento em lote
│   │   └── reports.py     # Relatórios analíticos
│   ├── services/          # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── llm.py         # Integração com LLM
│   │   ├── classifier.py  # Motor de classificação
│   │   └── reports.py     # Geração de relatórios
│   ├── models/            # Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── classification.py
│   │   └── requests.py
│   └── core/              # Configurações
│       ├── __init__.py
│       └── config.py
├── frontend/              # Aplicação Streamlit
│   ├── app.py             # Entry point
│   ├── pages/             # Páginas
│   │   ├── classify.py    # Classificação individual
│   │   ├── batch.py       # Processamento em lote
│   │   ├── validation.py  # Validação humana
│   │   └── reports.py     # Dashboard analítico
│   └── components/        # Componentes reutilizáveis
│       ├── __init__.py
│       └── ui_helpers.py
├── core/                  # Código compartilhado
│   ├── __init__.py
│   ├── taxonomy.py        # Definições da taxonomia
│   └── prompts.py         # Prompts do LLM
├── data/                  # Dados
│   ├── samples/           # Amostras para teste
│   └── golden/            # Golden dataset
├── tests/                 # Testes
│   ├── __init__.py
│   ├── test_api.py
│   └── test_classifier.py
├── prompts/               # Versionamento de prompts
│   └── v1/               # Versão 1 dos prompts
├── requirements.txt       # Dependências
├── .env.example          # Template de variáveis de ambiente
└── README.md             # Este arquivo
```

## ⚙️ Configuração do Ambiente

### 🔄 Guia Git para Equipes

Este projeto será desenvolvido por **duas equipes diferentes**. Siga o fluxo abaixo conforme sua situação:

#### Opção A: Fazer Fork (Recomendado para equipes separadas)

Se você faz parte de uma equipe independente e vai trabalhar em um repositório separado:

```bash
# 1. Faça o fork pelo GitHub (botão "Fork" na página do repositório)
# Isso cria uma cópia do repo na sua conta/organização

# 2. Clone o SEU fork
# git clone https://github.com/SUA-CONTA/assistente-classifier-engine.git
cd assistente-classifier-engine

# 3. Configure o upstream (repo original) para receber atualizações
git remote add upstream https://github.com/ORIGINAL-OWNER/assistente-classifier-engine.git

# 4. Verifique os remotes
git remote -v
# origin    -> seu fork
# upstream  -> repo original
```

**Para atualizar seu fork com mudanças do original:**
```bash
# Buscar atualizações do upstream
git fetch upstream

# Ir para sua branch main
git checkout main

# Mesclar mudanças do upstream
git merge upstream/main

# Enviar para seu fork
git push origin main
```

#### Opção B: Clonar Diretamente (Se tiver acesso ao repo original)

```bash
# Clone o repositório original
git clone https://github.com/ORIGINAL-OWNER/assistente-classifier-engine.git
cd assistente-classifier-engine
```

#### Fluxo de Trabalho Diário (Pull + Branch + PR)

```bash
# 1. Antes de começar, atualize sua branch main
git checkout main
git pull origin main        # ou git pull upstream main se usando fork

# 2. Crie uma branch para sua feature/task
git checkout -b feat/nome-da-feature
# Exemplos:
# git checkout -b feat/taxonomia-categorias
# git checkout -b feat/integracao-openai
# git checkout -b fix/corrige-validacao

# 3. Faça suas alterações e commits
git add .
git commit -m "feat: descrição do que foi feito"

# 4. Envie para o repositório remoto
git push origin feat/nome-da-feature

# 5. Abra um Pull Request pelo GitHub
# - Vá para a página do repositório
# - Clique em "Compare & pull request"
# - Descreva suas mudanças
# - Solicite review
```

#### Convenções de Commit

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Documentação |
| `test:` | Testes |
| `refactor:` | Refatoração |

**Exemplos:**
```bash
git commit -m "feat: implementa lista de categorias da taxonomia"
git commit -m "fix: corrige cálculo do score final ponderado"
git commit -m "docs: adiciona instruções de configuração"
```

### 1. Pré-requisitos

- Python 3.11 ou superior
- pip ou poetry
- Chave de API da OpenAI
- Git configurado

### 2. Instalação

```bash
# Clone o repositório (se aplicável)
git clone <repo-url>
cd assistente-classifier-engine

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
```

### 3. Configuração de Variáveis de Ambiente

```bash
# Copie o template
cp .env.example .env

# Edite o arquivo .env com suas credenciais
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
API_PORT=8000
FRONTEND_PORT=8501
```

## 🎯 Como Executar

### Modo 1: Apenas API (Backend)

```bash
# Terminal 1 - API FastAPI
uvicorn api.main:app --reload --port 8000
```

Acesse: http://localhost:8000/docs (Swagger UI)

### Modo 2: Apenas Frontend (Streamlit)

```bash
# Terminal 2 - Frontend Streamlit
streamlit run frontend/app.py --server.port 8501
```

Acesse: http://localhost:8501

### Modo 3: Ambos (Desenvolvimento Completo)

```bash
# Terminal 1 - API
uvicorn api.main:app --reload --port 8000

# Terminal 2 - Frontend (nova aba)
streamlit run frontend/app.py --server.port 8501
```

## 📋 Funcionalidades por Fase

### Fase 1: Definição de Taxonomia (Implementar)
- [ ] Definir taxonomia de etiquetas no `core/taxonomy.py`
- [ ] Categorias: Financeiro, Técnico, Comercial, etc.
- [ ] Critérios de qualidade: Empatia, Clareza, Objetividade, Resolutividade
- [ ] Implementar `calcular_score_final()` com média ponderada
- [ ] Implementar `validar_classificacao()`
- [ ] Ver PRD Seção 5.1 para especificações

### Fase 2: Dataset Base (Implementar)
- [ ] Criar samples de atendimentos em `/data/samples/`
- [ ] Definir golden dataset para validação
- [ ] Criar scripts de avaliação de concordância

### Fase 3: Pipeline LLM (Implementar)
- [ ] Integrar com API OpenAI
- [ ] Implementar `core/prompts.py` com prompts versionados
- [ ] Criar `services/classifier.py` com lógica de classificação
- [ ] Implementar saída JSON estruturada

### Fase 4: Validação Humano no Loop (Implementar)
- [ ] Interface Streamlit para revisão
- [ ] Sistema de log de divergências
- [ ] Auditoria de decisões

### Fase 5: Consolidação Analítica (Implementar)
- [ ] Dashboard com métricas
- [ ] Exportação JSON/CSV
- [ ] Relatórios de tendências

## 🔧 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/classify` | Classifica um atendimento |
| POST | `/batch` | Processa lote de atendimentos |
| GET | `/reports/distribution` | Distribuição por categoria |
| GET | `/reports/quality` | Índice de qualidade médio |
| GET | `/health` | Health check |

## 📊 Exemplo de Uso

### Classificação Individual

```python
import requests

response = requests.post("http://localhost:8000/classify", json={
    "texto": "Cliente solicitou reembolso por cobrança duplicada no cartão..."
})

print(response.json())
```

**Saída esperada:**
```json
{
  "categoria": "Financeiro",
  "intencao": "Solicitação de reembolso",
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
  "resumo": "Cliente solicitou reembolso por cobrança duplicada...",
  "topicos": ["Cobrança duplicada", "Solicitação de reembolso"]
}
```

### Processamento em Lote

```bash
curl -X POST http://localhost:8000/batch \
  -F "file=@atendimentos.csv" \
  -F "format=json"
```

## 🧪 Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Testes específicos
pytest tests/test_classifier.py -v
```

## 📈 Métricas de Sucesso

| Métrica | Meta | Como Medir |
|---------|------|------------|
| Concordância com golden dataset | ≥ 85% | Script em `tests/` |
| Redução esforço manual | ≥ 70% | Logs de validação |
| Tempo de processamento | < 5s | Timestamp nas requisições |
| Consistência de output | ≥ 99% | Validação de schema |

## 📝 Versionamento de Prompts

Os prompts do LLM são versionados em `/prompts/v{N}/`:

```
prompts/
├── v1/
│   ├── classify.txt      # Prompt de classificação
│   ├── quality.txt       # Prompt de avaliação de qualidade
│   └── summarize.txt     # Prompt de resumo
└── v2/                   # Futuras iterações
```

Para trocar a versão, altere `PROMPT_VERSION` no `.env`.

## 🤝 Contribuindo

1. Crie uma branch: `git checkout -b feat/nome-da-feature`
2. Faça commits: `git commit -m "feat: descrição"`
3. Push: `git push origin feat/nome-da-feature`
4. Abra um Pull Request

## 📚 Recursos Úteis

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação Streamlit](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [PRD do Projeto](./prd.md)

## ❓ Troubleshooting

**Problema:** API não inicia  
**Solução:** Verifique se `OPENAI_API_KEY` está configurada no `.env`

**Problema:** Frontend não conecta na API  
**Solução:** Confirme que a API está rodando na porta 8000 e `API_URL` no `.env` está correto

**Problema:** Timeout no processamento  
**Solução:** Ajuste `LLM_TIMEOUT` no `.env` (padrão: 30s)



**Dúvidas?** Entre em contato via discord ou consulte o PRD em `prd.md`.
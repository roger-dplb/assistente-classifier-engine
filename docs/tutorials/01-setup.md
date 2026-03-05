# 🚀 Tutorial 01: Configuração do Ambiente

Bem-vindo! Este tutorial vai guiá-lo na configuração inicial do Sistema de Autoetiquetagem Inteligente.

## 🎯 O que você vai conseguir

Ao final deste tutorial, você terá:
- ✅ Ambiente virtual Python configurado
- ✅ Dependências instaladas
- ✅ API FastAPI rodando localmente
- ✅ Frontend Streamlit executando
- ✅ Primeira classificação de teste realizada

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.11+** → [Download](https://www.python.org/downloads/)
- **Git** → [Download](https://git-scm.com/downloads)
- **Chave de API da OpenAI** → [Obter aqui](https://platform.openai.com/api-keys)

Verifique suas versões:
```bash
python --version  # Deve mostrar 3.11.x ou superior
git --version
```

---

## 🚀 Passo a Passo

### Passo 1: Clone o Repositório

```bash
# Clone o repositório
git clone https://github.com/roger-dplb/assistente-classifier-engine.git

# Entre na pasta do projeto
cd assistente-classifier-engine
```

**✅ Verificação:** Você deve ver a pasta do projeto no terminal.

---

### Passo 2: Crie o Ambiente Virtual

O ambiente virtual isola as dependências do projeto.

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**✅ Verificação:** Seu terminal deve mostrar `(venv)` no início da linha:
```
(venv) user@machine:~/assistente-classifier-engine$
```

---

### Passo 3: Instale as Dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- FastAPI (backend)
- Streamlit (frontend)
- OpenAI (integração LLM)
- Pandas, NumPy (processamento)
- Pytest (testes)

**✅ Verificação:** Ao final, você verá `Successfully installed ...`

---

### Passo 4: Configure as Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env
# Linux/Mac:
nano .env
# ou
code .env

# Windows:
notepad .env
```

Adicione sua chave da OpenAI:
```env
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-4
API_PORT=8000
FRONTEND_PORT=8501
```

> ⚠️ **Importante:** Nunca compartilhe sua `OPENAI_API_KEY` ou commit o arquivo `.env`!

**✅ Verificação:** O arquivo `.env` existe na raiz do projeto.

---

### Passo 5: Inicie a API (Backend)

Em um terminal, execute:

```bash
# Certifique-se que o venv está ativado
source venv/bin/activate  # Linux/Mac
# ou
# venv\Scripts\activate   # Windows

# Inicie a API
uvicorn api.main:app --reload --port 8000
```

**✅ Verificação:** Você verá:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

Teste no navegador: http://localhost:8000/docs

Deixe este terminal rodando e abra um **novo terminal** para o próximo passo.

---

### Passo 6: Inicie o Frontend (Streamlit)

No novo terminal:

```bash
# Ative o venv novamente
source venv/bin/activate  # Linux/Mac
# ou
# venv\Scripts\activate   # Windows

# Inicie o Streamlit
streamlit run frontend/app.py --server.port 8501
```

**✅ Verificação:** Seu navegador abrirá automaticamente em http://localhost:8501

Você verá a página inicial do sistema! 🎉

---

### Passo 7: Teste sua Primeira Classificação

1. No navegador (Streamlit), clique em **"🏷️ Classificar"** no menu lateral
2. Cole o texto de teste abaixo:

```
Cliente: Olá, fui cobrado duas vezes no meu cartão de crédito pela mesma compra. 
Preciso de um reembolso urgente!

Atendente: Olá! Sinto muito pelo inconveniente. Vou verificar sua fatura 
imediatamente e solicitar o estorno. O reembolso será processado em até 48 horas.
```

3. Clique em **"🔍 Classificar"**

**✅ Verificação:** Você verá:
- Categorias classificadas (ex: Financeiro)
- Scores de qualidade
- Resumo gerado
- Lista de tópicos

---

## 🎉 Parabéns!

Você configurou com sucesso o Sistema de Autoetiquetagem! 🚀

### O que você aprendeu:
- Como clonar e navegar no repositório
- Como criar e ativar ambiente virtual Python
- Como instalar dependências
- Como configurar variáveis de ambiente
- Como iniciar API e Frontend
- Como fazer uma classificação de teste

---

## 📚 Próximos Passos

- **[Tutorial 02: Primeira Classificação](./02-primeira-classificacao.md)** - Explore todas as funcionalidades de classificação
- **[Como Fazer: Adicionar Categoria](../how-to/adicionar-categoria.md)** - Customize a taxonomia
- **[Explicação: Arquitetura](../explanation/arquitetura.md)** - Entenda como o sistema funciona

---

## ❌ Resolução de Problemas

### Erro: "ModuleNotFoundError"
**Causa:** Dependências não instaladas  
**Solução:**
```bash
pip install -r requirements.txt
```

### Erro: "OPENAI_API_KEY not found"
**Causa:** Chave da API não configurada  
**Solução:**
1. Verifique se criou o arquivo `.env`
2. Confirme que adicionou `OPENAI_API_KEY=sk-...`
3. Reinicie a API

### Erro: "Address already in use"
**Causa:** Porta 8000 ou 8501 ocupada  
**Solução:**
```bash
# Mude a porta da API
uvicorn api.main:app --reload --port 8001

# Ou atualize no .env
API_PORT=8001
```

### Erro: "Connection refused" no Streamlit
**Causa:** API não está rodando  
**Solução:** Verifique se o terminal da API está aberto e rodando.

---

**⬅️ Voltar para [Tutoriais](../README.md)**

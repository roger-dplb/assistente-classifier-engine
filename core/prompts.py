"""
LLM prompts for classification system.
Prompts are versioned externally in /prompts/v{N}/ directory.
"""
from pathlib import Path
from api.core.config import settings


def load_prompt_file(filename: str) -> str:
    """
    Load a prompt file from the prompts version directory.
    
    Args:
        filename: Name of the prompt file
        
    Returns:
        Prompt text content
    """
    prompt_dir = Path(__file__).parent.parent / "prompts" / settings.PROMPT_VERSION
    prompt_file = prompt_dir / filename
    
    if prompt_file.exists():
        return prompt_file.read_text(encoding="utf-8")
    
    # Fallback to built-in prompts
    return get_builtin_prompt(filename)


def get_builtin_prompt(filename: str) -> str:
    """Get a built-in prompt when file is not found."""
    prompts = {
        "classify.txt": """Você é um classificador especializado em atendimento ao cliente.

Analise o seguinte atendimento e retorne um JSON estruturado:

ATENDIMENTO:
{texto}

Classifique conforme a taxonomia:
- Categoria: Financeiro, Técnico, Comercial, Suporte, Reclamação, Dúvida, Sugestão, Outros
- Intenção: Solicitação de reembolso, Dúvida sobre cobrança, Problema técnico, Troca de produto, Cancelamento, Informação de preço, Solicitação de orçamento, Reclamação de serviço, Elogio, Outros
- Sentimento: Positivo, Neutro, Negativo
- Criticidade: Baixa, Média, Alta, Crítica
- SLA/Urgência: 4h, 8h, 24h, 48h, 72h

Avalie a qualidade do atendimento (0-10):
- Empatia
- Clareza
- Objetividade
- Resolutividade
- Score Final (média ponderada)

Gere também:
- Resumo executivo (máximo 5 linhas)
- Lista de tópicos principais abordados

Responda APENAS com JSON válido no formato:
{{
  "categoria": "...",
  "intencao": "...",
  "sentimento": "...",
  "criticidade": "...",
  "sla_urgencia": "...",
  "qualidade": {{
    "empatia": 0,
    "clareza": 0,
    "objetividade": 0,
    "resolutividade": 0,
    "score_final": 0.0
  }},
  "resumo": "...",
  "topicos": ["..."]
}}""",
        "quality.txt": """Avalie a qualidade do atendimento abaixo nos critérios (0-10):

ATENDIMENTO:
{texto}

Critérios:
- Empatia: Capacidade de se colocar no lugar do cliente
- Clareza: Qualidade da comunicação
- Objetividade: Foco e precisão nas respostas
- Resolutividade: Efetividade na resolução do problema

Retorne apenas JSON com os scores.""",
        "summarize.txt": """Gere um resumo executivo do atendimento abaixo (máximo 5 linhas) e liste os tópicos principais.

ATENDIMENTO:
{texto}

Retorne apenas JSON no formato:
{{
  "resumo": "...",
  "topicos": ["..."]
}}"""
    }
    
    return prompts.get(filename, "")


def get_classification_prompt(texto: str) -> str:
    """
    Get the full classification prompt with the interaction text.
    
    Args:
        texto: Customer service interaction text
        
    Returns:
        Complete prompt ready for LLM
    """
    template = load_prompt_file("classify.txt")
    return template.format(texto=texto)


def get_quality_prompt(texto: str) -> str:
    """Get quality assessment prompt."""
    template = load_prompt_file("quality.txt")
    return template.format(texto=texto)


def get_summarize_prompt(texto: str) -> str:
    """Get summarization prompt."""
    template = load_prompt_file("summarize.txt")
    return template.format(texto=texto)

"""
Taxonomy definitions for classification system.

TODO: Definir taxonomia conforme especificado no PRD Seção 5.1

Dimensões a implementar:
- Categoria: Tema principal do atendimento
- Intenção: O que o cliente deseja
- Sentimento: Positivo, neutro ou negativo
- Criticidade: Nível de urgência/impacto
- SLA/Urgência: Prazo esperado de resolução

Critérios de Qualidade (escala 0-10):
- Empatia
- Clareza
- Objetividade
- Resolutividade
"""

# TODO: Definir listas de categorias, intenções, sentimentos, criticidades e SLAs
# CATEGORIAS = []
# INTENCOES = []
# SENTIMENTOS = []
# CRITICIDADES = []
# SLAS = []


def calcular_score_final(empatia: int, clareza: int, objetividade: int, resolutividade: int) -> float:
    """
    Calculate weighted final quality score.
    
    TODO: Implementar média ponderada conforme critérios do PRD
    
    Args:
        empatia: Score 0-10
        clareza: Score 0-10
        objetividade: Score 0-10
        resolutividade: Score 0-10
        
    Returns:
        Weighted average score 0-10
    """
    pass


def validar_classificacao(categoria: str, intencao: str, sentimento: str, criticidade: str) -> bool:
    """
    Validate if classification values are within taxonomy.
    
    TODO: Implementar validação contra as listas definidas
    
    Args:
        categoria: Category to validate
        intencao: Intent to validate
        sentimento: Sentiment to validate
        criticidade: Priority level to validate
        
    Returns:
        True if all values are valid
    """
    pass


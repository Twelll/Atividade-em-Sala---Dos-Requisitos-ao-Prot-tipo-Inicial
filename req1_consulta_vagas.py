# Primeira implementacao

"""
Módulo responsável pelo Requisito 1: Consulta de Vagas Disponíveis.
Atende aos Critérios de Aceitação CA 1.1 e CA 1.2.
"""

DADOS_ESTACIONAMENTO = {
    "Bloco Central": [
        {"id": "C01", "ocupada": False, "tipo": "aluno"},
        {"id": "C02", "ocupada": True,  "tipo": "aluno"},
        {"id": "C03", "ocupada": False, "tipo": "aluno"},
    ],
    "Biblioteca": [
        {"id": "B01", "ocupada": False, "tipo": "funcionario"},
        {"id": "B02", "ocupada": True,  "tipo": "funcionario"},
        {"id": "B03", "ocupada": False, "tipo": "aluno"},
        {"id": "B04", "ocupada": True,  "tipo": "aluno"},
    ]
}

def consultar_resumo_por_setor() -> dict:
    """CA 1.1: Exibe a contagem numérica de vagas disponíveis por setor."""
    resumo = {}
    for setor, vagas in DADOS_ESTACIONAMENTO.items():
        total_livres = sum(1 for v in vagas if not v["ocupada"])
        resumo[setor] = {
            "total_vagas": len(vagas),
            "disponiveis": total_livres
        }
    return resumo

def detalhar_status_vagas(setor: str) -> list:
    """CA 1.2: Apresenta o status individual de cada vaga do setor."""
    return DADOS_ESTACIONAMENTO.get(setor, [])
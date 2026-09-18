"""
Módulo responsável pelo Requisito 2: Identificação de Vagas de Funcionários.
Atende aos Critérios de Aceitação CA 2.1, CA 2.2 e CA 2.3.
"""
from req1_consulta_vagas import DADOS_ESTACIONAMENTO

def formatar_vagas_biblioteca() -> list[str]:
    """CA 2.1 e CA 2.2: Destaque visual e aviso textual de exclusividade."""
    linhas = []
    vagas_bib = DADOS_ESTACIONAMENTO.get("Biblioteca", [])
    for vaga in vagas_bib:
        status = "OCUPADA" if vaga["ocupada"] else "DISPONÍVEL"
        if vaga["tipo"] == "funcionario":
            linhas.append(f"[{vaga['id']}] {status} -> [EXCLUSIVA FUNCIONÁRIOS]")
        else:
            linhas.append(f"[{vaga['id']}] {status} (Estudante)")
    return linhas

def filtrar_vagas_livres_alunos() -> list[dict]:
    """CA 2.3: Filtra e oculta vagas de funcionários, mantendo só vagas de alunos livres."""
    resultado = []
    for setor, vagas in DADOS_ESTACIONAMENTO.items():
        for vaga in vagas:
            if vaga["tipo"] == "aluno" and not vaga["ocupada"]:
                resultado.append({"setor": setor, "id": vaga["id"]})
    return resultado
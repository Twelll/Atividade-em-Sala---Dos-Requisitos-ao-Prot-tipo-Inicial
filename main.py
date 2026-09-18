"""
==============================================================================
PASSO 1: PLANO DE EXECUÇÃO (Critério do Roteiro)
==============================================================================
Requisitos escolhidos:
1. Requisito 1: Consulta de Vagas Disponíveis (contagem e status individual)
2. Requisito 2: Identificação de Vagas de Funcionários (destaque e filtro de alunos)

Ordem de implementação e tempo estimado:
- Requisito 1 (req1_consulta_vagas.py): 10 minutos 
- Requisito 2 (req2_vagas_funcionarios.py): 10 minutos
- Integração CLI (main.py): 10 minutos
- Testes, README e Autoavaliação: 10 minutos

Uso de IA:
- Utilizei a IA para programar em Python, pois eu não domino essa linguagem de programação e também para
me lembrar como usa o github(fazia tempo que não usei)
==============================================================================
"""

import req1_consulta_vagas as req1
import req2_vagas_funcionarios as req2

def main():
    print("=" * 60)
    print("SISTEMA DE CONTROLE DE VAGAS - PROTÓTIPO CLI")
    print("=" * 60)

    # --- EXECUÇÃO REQUISITO 1 ---
    print("\n--- REQUISITO 1: CONSULTA DE DISPONIBILIDADE ---")
    print("[CA 1.1] Resumo numérico por setor:")
    resumo = req1.consultar_resumo_por_setor()
    for setor, info in resumo.items():
        print(f"  * {setor}: {info['disponiveis']} disponíveis de {info['total_vagas']}")

    print("\n[CA 1.2] Detalhamento do setor 'Bloco Central':")
    for vaga in req1.detalhar_status_vagas("Bloco Central"):
        status = "Ocupada" if vaga["ocupada"] else "Livre"
        print(f"  - Vaga {vaga['id']}: {status}")

    # --- EXECUÇÃO REQUISITO 2 ---
    print("\n--- REQUISITO 2: VAGAS EXCLUSIVAS DE FUNCIONÁRIOS ---")
    print("[CA 2.1 e 2.2] Mapeamento do setor da Biblioteca:")
    for linha in req2.formatar_vagas_biblioteca():
        print(f"  {linha}")

    print("\n[CA 2.3] Filtro aplicado: 'Apenas vagas livres para alunos':")
    vagas_livres = req2.filtrar_vagas_livres_alunos()
    for vaga in vagas_livres:
        print(f"  * Setor {vaga['setor']} -> Vaga {vaga['id']} [Livre]")

    print("\n" + "=" * 60)
    print("PROTÓTIPO EXECUTADO COM SUCESSO.")
    print("=" * 60)

if __name__ == "__main__":
    main()

"""
==============================================================================
PASSO 3: AUTOAVALIAÇÃO
==============================================================================
Critérios Atingidos:
- [X] Critério 1: Lista de requisitos documentada em REQUISITOS.md.
- [X] Critério 2: Cada requisito em arquivo separado (req1 e req2).
- [X] Critério 3: Ponto de entrada único funcional (python main.py).
- [X] Critério 4: Histórico Git estruturado com commits atômicos por requisito.
- [X] Critério 5: README conciso com menos de 10 linhas.
- [X] Critério 6: Execução limpa sem dependências externas via terminal.

Requisito mais difícil:
- Requisito 2: A separação do filtro excluindo vagas de funcionários mantendo o 
  escopo de múltiplos setores exigiu padronizar a estrutura do mock de dados.

Uso de IA:
Ajudou: Me ajudou a programar e lembrar github
Atrapalhou: Fez coisas que não precisava,
então tive trocar algumas coisas. Também tive que conferir tudo, para ter certeza que realmente cumpria os requisitos
==============================================================================
"""
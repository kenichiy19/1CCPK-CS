"""
Citizen Assist AI - Módulo de decisão lógica (Computer Science - GS26_2)
Situação: emissão da 1ª via da Carteira de Identidade Nacional (CIN) em São Paulo.

Variáveis de entrada (1 = sim, 0 = não):
    A = possui CPF
    B = possui certidão de nascimento ou de casamento
    C = tem 16 anos ou mais
    D = está acompanhado do responsável legal ou tem a autorização assinada por ele
Saída:
    S = pode comparecer ao atendimento com a documentação necessária

Expressão simplificada (álgebra booleana e mapa de Karnaugh): S = AB(C + D)
"""

FONTE = ("Poupatempo SP - Carteira de Identidade Nacional (CIN): 1ª via. "
         "https://www.poupatempo.sp.gov.br/carta/D97C3844-A2D9-4C9E-B364-CB4FEB26A1FB "
         "(acesso em 13/11/2026)")

AVISO = """
==================================================================
  CITIZEN ASSIST AI - Orientação para a 1ª via da CIN (SP)
==================================================================
  AVISO: este é um protótipo acadêmico. Ele NÃO é um canal oficial
  e NÃO confirma a emissão do documento nem a concessão de direitos.
  Nenhum dado pessoal é coletado: responda apenas sim ou não.
  Em caso de dúvida, consulte o site oficial do Poupatempo.
==================================================================
"""

RESPOSTAS_SIM = {"s", "sim"}
RESPOSTAS_NAO = {"n", "nao", "não"}


def perguntar(texto):
    """Faz uma pergunta de sim/não e repete até receber uma resposta válida.
    Retorna 1 para sim e 0 para não."""
    while True:
        resposta = input(f"{texto} (s/n): ").strip().lower()
        if resposta in RESPOSTAS_SIM:
            return 1
        if resposta in RESPOSTAS_NAO:
            return 0
        print("  Resposta inválida. Digite apenas 's' para sim ou 'n' para não.")


def decidir(a, b, c, d):
    """Lógica simplificada do módulo: S = AB(C + D)."""
    return a and b and (c or d)


def pendencias(a, b, c, d):
    """Lista o que falta para o cidadão, quando S = 0."""
    faltas = []
    if not a:
        faltas.append("Informar o número do CPF ou levar um documento oficial que o contenha.")
    if not b:
        faltas.append("Levar a certidão de nascimento ou de casamento (original ou cópia autenticada).")
    if not c and not d:
        faltas.append("Por ter menos de 16 anos, comparecer com o responsável legal "
                      "ou levar a autorização assinada por ele.")
    return faltas


def consultar():
    """Executa uma consulta completa: perguntas, decisão e orientação."""
    a = perguntar("1. Você possui CPF?")
    b = perguntar("2. Você possui certidão de nascimento ou de casamento?")
    c = perguntar("3. Você tem 16 anos ou mais?")
    d = perguntar("4. Você estará acompanhado do responsável legal ou tem a autorização assinada por ele?")

    s = decidir(a, b, c, d)
    print(f"\nEntradas: A={a} B={b} C={c} D={d}  ->  Saída S={int(s)}")

    if s:
        print("Orientação: você pode comparecer ao atendimento com a documentação necessária.")
        print("Lembre-se de agendar pelo site, aplicativo ou WhatsApp do Poupatempo.")
    else:
        print("Orientação: ainda falta algum requisito antes de comparecer ao atendimento:")
        for item in pendencias(a, b, c, d):
            print(f"  - {item}")

    print(f"\nFonte: {FONTE}")


def main():
    print(AVISO)
    while True:
        consultar()
        if not perguntar("\nDeseja fazer uma nova consulta?"):
            print("Encerrando. Obrigado por usar o Citizen Assist AI.")
            break
        print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nConsulta interrompida. Até logo!")
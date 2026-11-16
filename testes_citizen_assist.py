"""
Testes do módulo de decisão lógica - Citizen Assist AI (Etapa 7)
Valida as 16 combinações de entrada, comparando:
  1. a tabela-verdade construída manualmente (regra original);
  2. a expressão canônica: S = ABC'D + ABCD' + ABCD  (Σm(13, 14, 15));
  3. a expressão simplificada: S = AB(C + D);
  4. o resultado executado pelo programa (função decidir).
"""

from itertools import product

from citizen_assist_cin import decidir

# Saída S da tabela-verdade feita à mão (linhas 0 a 15, ABCD de 0000 a 1111)
TABELA_VERDADE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]


def canonica(a, b, c, d):
    """S = ABC'D + ABCD' + ABCD"""
    return int((a and b and not c and d) or
               (a and b and c and not d) or
               (a and b and c and d))


def simplificada(a, b, c, d):
    """S = AB(C + D)"""
    return int(a and b and (c or d))


def main():
    print(f"{'m':>2} | A B C D | Tabela | Canônica | Simplificada | Programa | Resultado")
    print("-" * 74)

    aprovados = 0
    for m, (a, b, c, d) in enumerate(product([0, 1], repeat=4)):
        esperado = TABELA_VERDADE[m]
        s_can = canonica(a, b, c, d)
        s_simp = simplificada(a, b, c, d)
        s_prog = int(decidir(a, b, c, d))

        ok = esperado == s_can == s_simp == s_prog
        aprovados += ok
        print(f"{m:>2} | {a} {b} {c} {d} |   {esperado}    |    {s_can}     |"
              f"      {s_simp}       |    {s_prog}     | {'OK' if ok else 'FALHA'}")

    print("-" * 74)
    print(f"Combinações aprovadas: {aprovados}/16")
    if aprovados == 16:
        print("Conclusão: a regra original, a expressão canônica, a expressão "
              "simplificada e o programa são equivalentes.")
    else:
        print("Atenção: há divergências. Verifique as linhas marcadas com FALHA.")


if __name__ == "__main__":
    main()



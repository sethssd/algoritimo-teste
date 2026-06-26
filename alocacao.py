"""
Simulador de Alocação de Blocos no Disco — Estratégia Contígua
Sistemas Operacionais — Trabalho em Grupo 2
"""

def criar_disco(total_blocos):
    return [None] * total_blocos   # None = livre


def encontrar_espaco(disco, tamanho):
    """Busca First-Fit: retorna índice do primeiro espaço contíguo suficiente."""
    n = len(disco)
    i = 0
    while i < n:
        if disco[i] is None:
            # conta blocos livres contíguos a partir de i
            j = i
            while j < n and disco[j] is None:
                j += 1
            if j - i >= tamanho:
                return i        # espaço encontrado
            i = j               # pula para depois do bloco ocupado
        else:
            i += 1
    return -1                   # sem espaço suficiente


def alocar_arquivo(disco, nome, tamanho):
    inicio = encontrar_espaco(disco, tamanho)
    if inicio == -1:
        return False, -1
    for i in range(inicio, inicio + tamanho):
        disco[i] = nome
    return True, inicio


def imprimir_mapa(disco):
    linha = ""
    for bloco in disco:
        if bloco is None:
            linha += "[ ]"
        else:
            linha += f"[{bloco}]"
    # quebra em linhas de 20 blocos
    tamanho_linha = 20
    total = len(disco)
    print()
    for inicio in range(0, total, tamanho_linha):
        segmento = disco[inicio:inicio + tamanho_linha]
        print("  " + "".join("[ ]" if b is None else f"[{b}]" for b in segmento))


def imprimir_tabela(alocacoes, disco):
    print("\n" + "="*60)
    print("  MAPA DE ALOCAÇÃO DO DISCO")
    print("="*60)

    livres = disco.count(None)
    usados = len(disco) - livres

    if alocacoes:
        print(f"\n  {'Arquivo':<10} {'Início':>8} {'Tamanho':>9} {'Blocos':>30}")
        print("  " + "-"*58)
        for nome, inicio, tamanho in alocacoes:
            blocos = f"{inicio}–{inicio + tamanho - 1}"
            print(f"  {nome:<10} {inicio:>8} {tamanho:>9} {blocos:>30}")

    print(f"\n  Disco: {usados} blocos usados, {livres} livres "
          f"({len(disco)} total)")
    print("\n  Mapa visual ([ ] = livre):")
    imprimir_mapa(disco)
    print("\n" + "="*60 + "\n")


def ler_inteiro(prompt, minimo=1):
    while True:
        try:
            v = int(input(prompt))
            if v < minimo:
                print(f"    [!] Deve ser >= {minimo}.")
                continue
            return v
        except ValueError:
            print("    [!] Apenas inteiro.")


def main():
    print("\n" + "="*60)
    print("   SIMULADOR — ALOCAÇÃO CONTÍGUA DE BLOCOS NO DISCO")
    print("="*60)

    total_blocos = ler_inteiro("\n  Total de blocos no disco: ", minimo=1)
    disco        = criar_disco(total_blocos)
    alocacoes    = []   # lista de (nome, inicio, tamanho)

    print("\n  (digite 'sair' para encerrar)\n")

    while True:
        print("-"*60)
        nome = input("  Nome do arquivo (ou 'sair'): ").strip()
        if nome.lower() == "sair":
            break
        if not nome:
            print("  [!] Nome não pode ser vazio.")
            continue
        if any(a[0] == nome for a in alocacoes):
            print(f"  [!] Arquivo '{nome}' já existe no disco.")
            continue

        tamanho = ler_inteiro(f"  Tamanho de '{nome}' em blocos: ", minimo=1)

        ok, inicio = alocar_arquivo(disco, nome, tamanho)
        if ok:
            alocacoes.append((nome, inicio, tamanho))
            print(f"  OK — '{nome}' alocado nos blocos {inicio}–{inicio+tamanho-1}.")
            imprimir_tabela(alocacoes, disco)
        else:
            print(f"  FALHA — sem {tamanho} blocos contíguos livres.")
            imprimir_tabela(alocacoes, disco)

    # mapa final
    print("\n  === ESTADO FINAL DO DISCO ===")
    imprimir_tabela(alocacoes, disco)
    print("  Simulação encerrada.\n")


if __name__ == "__main__":
    main()

"""
Simulador do Algoritmo do Banqueiro
Sistemas Operacionais — Trabalho em Grupo 2
"""

def ler_matriz(nome, linhas, colunas):
    print(f"\n  {nome} ({linhas} processos x {colunas} recursos):")
    matriz = []
    for i in range(linhas):
        while True:
            try:
                linha = list(map(int, input(f"    P{i}: ").split()))
                if len(linha) != colunas:
                    print(f"    [!] Informe exatamente {colunas} valores.")
                    continue
                matriz.append(linha)
                break
            except ValueError:
                print("    [!] Apenas números inteiros.")
    return matriz


def ler_vetor(nome, colunas):
    print(f"\n  {nome} ({colunas} recursos):")
    while True:
        try:
            v = list(map(int, input("    > ").split()))
            if len(v) != colunas:
                print(f"    [!] Informe exatamente {colunas} valores.")
                continue
            return v
        except ValueError:
            print("    [!] Apenas números inteiros.")


def verificar_seguro(alocacao, necessidade, disponivel, n, r):
    trabalho  = disponivel[:]
    concluido = [False] * n
    sequencia = []

    for _ in range(n):
        encontrou = False
        for i in range(n):
            if not concluido[i] and all(necessidade[i][j] <= trabalho[j] for j in range(r)):
                for j in range(r):
                    trabalho[j] += alocacao[i][j]
                concluido[i] = True
                sequencia.append(i)
                encontrou = True
                break
        if not encontrou:
            break

    if all(concluido):
        return True, sequencia
    return False, []


def imprimir_estado(alocacao, necessidade, disponivel, maximo, n, r):
    print("\n" + "="*55)
    print("  ESTADO ATUAL DA MEMÓRIA")
    print("="*55)
    print(f"\n  {'Processo':<10} {'Alocação':<{r*3+2}} {'Máximo':<{r*3+2}} {'Necessidade'}")
    print("  " + "-"*50)
    for i in range(n):
        al = " ".join(f"{alocacao[i][j]:>2}"    for j in range(r))
        mx = " ".join(f"{maximo[i][j]:>2}"       for j in range(r))
        ne = " ".join(f"{necessidade[i][j]:>2}"  for j in range(r))
        print(f"  P{i:<9} [{al}]   [{mx}]   [{ne}]")
    disp = " ".join(f"{disponivel[j]:>2}" for j in range(r))
    print(f"\n  Disponível: [{disp}]")
    print("="*55)


def main():
    print("\n" + "="*55)
    print("   SIMULADOR — ALGORITMO DO BANQUEIRO")
    print("="*55)

    # Configuração
    print("\n[1] CONFIGURAÇÃO DO SISTEMA")
    while True:
        try:
            n = int(input("\n  Número de processos: "))
            r = int(input("  Número de tipos de recurso: "))
            if n > 0 and r > 0:
                break
            print("  [!] Valores devem ser positivos.")
        except ValueError:
            print("  [!] Apenas inteiros.")

    maximo   = ler_matriz("Matriz de Máximo", n, r)
    alocacao = ler_matriz("Matriz de Alocação atual", n, r)

    for i in range(n):
        for j in range(r):
            if alocacao[i][j] > maximo[i][j]:
                print(f"\n  [!] ERRO: Alocação de P{i} excede o máximo declarado.")
                return

    necessidade = [[maximo[i][j] - alocacao[i][j] for j in range(r)] for i in range(n)]
    disponivel  = ler_vetor("Vetor de Recursos Disponíveis", r)

    # Estado inicial
    print("\n[2] VERIFICAÇÃO DO ESTADO INICIAL")
    imprimir_estado(alocacao, necessidade, disponivel, maximo, n, r)

    seguro, seq = verificar_seguro(alocacao, necessidade, disponivel, n, r)
    if seguro:
        print(f"\n  Estado inicial: SEGURO")
        print(f"  Sequência segura: {' → '.join(f'P{p}' for p in seq)}")
    else:
        print("\n  Estado inicial: INSEGURO — sistema já em deadlock potencial.")
        return

    #  Loop de requisições 
    print("\n[3] SIMULAÇÃO DE REQUISIÇÕES")
    print("  (digite 'sair' para encerrar)\n")

    while True:
        print("-"*55)
        proc_str = input("  Processo que requisita (ex: 0 para P0) ou 'sair': ").strip()
        if proc_str.lower() == "sair":
            break
        try:
            pid = int(proc_str)
            if pid < 0 or pid >= n:
                print(f"  [!] Processo deve ser entre 0 e {n-1}.")
                continue
        except ValueError:
            print("  [!] Digite um número de processo ou 'sair'.")
            continue

        req = ler_vetor(f"Requisição de P{pid}", r)
        print(f"\n  >> P{pid} solicita: [{' '.join(str(x) for x in req)}]")

        # Passo 1: req <= necessidade[pid]
        if any(req[j] > necessidade[pid][j] for j in range(r)):
            print("  NEGADO: Requisição excede a Necessidade declarada do processo.")
            continue

        # Passo 2: req <= disponivel
        if any(req[j] > disponivel[j] for j in range(r)):
            print("  NEGADO: Recursos insuficientes — processo deve aguardar.")
            continue

        # Passo 3: concessão provisória
        for j in range(r):
            disponivel[j]       -= req[j]
            alocacao[pid][j]    += req[j]
            necessidade[pid][j] -= req[j]

        # Passo 4: verifica segurança
        seguro, seq = verificar_seguro(alocacao, necessidade, disponivel, n, r)
        if seguro:
            print(f"  CONCEDIDO — Estado permanece SEGURO.")
            print(f"  Sequência segura: {' → '.join(f'P{p}' for p in seq)}")
            imprimir_estado(alocacao, necessidade, disponivel, maximo, n, r)
        else:
            # Reverte
            for j in range(r):
                disponivel[j]       += req[j]
                alocacao[pid][j]    -= req[j]
                necessidade[pid][j] += req[j]
            print("  NEGADO — Concessão levaria a estado INSEGURO (risco de deadlock).")

    print("\n" + "="*55)
    print("  Simulação encerrada.")
    print("="*55 + "\n")


if __name__ == "__main__":
    main()

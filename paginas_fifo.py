"""
Simulador de Escalonamento de Braço de Disco — FCFS
Sistemas Operacionais — Trabalho em Grupo 2
"""

def simular_fcfs(posicao_inicial, requisicoes):
    ordem      = requisicoes[:]
    historico  = []
    pos_atual  = posicao_inicial
    total      = 0

    for destino in ordem:
        deslocamento = abs(destino - pos_atual)
        total += deslocamento
        historico.append({
            "de"          : pos_atual,
            "para"        : destino,
            "deslocamento": deslocamento,
            "acumulado"   : total,
        })
        pos_atual = destino

    return total, historico


def imprimir_resultado(posicao_inicial, requisicoes, total, historico):
    print("\n" + "="*60)
    print("  SIMULADOR FCFS — ESCALONAMENTO DE DISCO")
    print("="*60)
    print(f"  Posição inicial : {posicao_inicial}")
    print(f"  Fila de pedidos : {requisicoes}")
    print("="*60)

    print(f"\n  {'Passo':<7} {'De':>6} {'Para':>6} {'Deslocamento':>14} {'Acumulado':>11}")
    print("  " + "-"*50)

    for i, h in enumerate(historico, 1):
        print(f"  {i:<7} {h['de']:>6} {h['para']:>6} {h['deslocamento']:>14} {h['acumulado']:>11}")

    print("\n" + "="*60)
    print(f"  Ordem de atendimento : {posicao_inicial} → " +
          " → ".join(str(h['para']) for h in historico))
    print(f"  Total de cilindros percorridos : {total}")
    print("="*60 + "\n")


def ler_inteiros(prompt):
    while True:
        try:
            vals = list(map(int, input(prompt).split()))
            if not vals:
                print("    [!] Informe ao menos um valor.")
                continue
            if any(v < 0 for v in vals):
                print("    [!] Valores devem ser não-negativos.")
                continue
            return vals
        except ValueError:
            print("    [!] Apenas números inteiros.")


def ler_inteiro(prompt):
    while True:
        try:
            v = int(input(prompt))
            if v < 0:
                print("    [!] Deve ser não-negativo.")
                continue
            return v
        except ValueError:
            print("    [!] Apenas inteiro.")


def main():
    print("\n" + "="*60)
    print("   SIMULADOR — ESCALONAMENTO DE DISCO (FCFS)")
    print("="*60)

    while True:
        posicao_inicial = ler_inteiro("\n  Posição inicial do braço: ")
        requisicoes     = ler_inteiros("  Fila de requisições (separadas por espaço): ")

        total, historico = simular_fcfs(posicao_inicial, requisicoes)
        imprimir_resultado(posicao_inicial, requisicoes, total, historico)

        resp = input("  Rodar outra simulação? (s/n): ").strip().lower()
        if resp != "s":
            break

    print("\n  Simulação encerrada.\n")


if __name__ == "__main__":
    main()

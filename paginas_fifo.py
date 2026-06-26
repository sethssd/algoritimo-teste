"""
Simulador de Substituição de Páginas — Algoritmo FIFO
Sistemas Operacionais — Trabalho em Grupo 2
"""

from collections import deque


def simular_fifo(referencias, n_frames):
    frames   = deque()          # páginas na RAM (ordem de chegada)
    conjunto = set()            # acesso O(1) para verificar presença
    faults   = 0
    historico = []              # para imprimir passo a passo

    for pagina in referencias:
        hit = pagina in conjunto

        if not hit:
            faults += 1
            if len(frames) == n_frames:
                removida = frames.popleft()
                conjunto.remove(removida)
            else:
                removida = None
            frames.append(pagina)
            conjunto.add(pagina)
        else:
            removida = None

        historico.append({
            "pagina"  : pagina,
            "frames"  : list(frames),
            "fault"   : not hit,
            "removida": removida,
        })

    return faults, historico


def imprimir_resultado(referencias, n_frames, faults, historico):
    total = len(referencias)
    hits  = total - faults

    print("\n" + "="*60)
    print("  SIMULADOR FIFO — SUBSTITUIÇÃO DE PÁGINAS")
    print("="*60)
    print(f"  Referências : {referencias}")
    print(f"  Frames (RAM): {n_frames}")
    print("="*60)

    # cabeçalho da tabela passo a passo
    col_ref   = 6
    col_frame = n_frames * 4 + 2
    print(f"\n  {'Ref':>{col_ref}}  {'Frames na RAM':<{col_frame}}  Evento")
    print("  " + "-"*55)

    for h in historico:
        frames_str = "[" + ", ".join(f"{p:>2}" for p in h["frames"]) + "]"
        if h["fault"]:
            if h["removida"] is not None:
                evento = f"PAGE FAULT  (removeu pág. {h['removida']})"
            else:
                evento = "PAGE FAULT  (frame livre)"
        else:
            evento = "hit"

        print(f"  {h['pagina']:>{col_ref}}  {frames_str:<{col_frame}}  {evento}")

    print("\n" + "="*60)
    print(f"  Total de referências : {total}")
    print(f"  Page faults          : {faults}  ({faults/total*100:.1f}%)")
    print(f"  Hits                 : {hits}  ({hits/total*100:.1f}%)")
    print("="*60 + "\n")


def ler_referencias():
    print("\n  Sequência de referências (números separados por espaço):")
    while True:
        try:
            entrada = input("    > ").split()
            refs = list(map(int, entrada))
            if len(refs) == 0:
                print("    [!] Informe ao menos uma referência.")
                continue
            if any(r < 0 for r in refs):
                print("    [!] Páginas devem ser números não-negativos.")
                continue
            return refs
        except ValueError:
            print("    [!] Apenas números inteiros.")


def ler_frames():
    print("\n  Número de frames (quadros de RAM disponíveis):")
    while True:
        try:
            n = int(input("    > "))
            if n <= 0:
                print("    [!] Deve ser maior que zero.")
                continue
            return n
        except ValueError:
            print("    [!] Apenas inteiro positivo.")


def main():
    print("\n" + "="*60)
    print("   SIMULADOR — SUBSTITUIÇÃO DE PÁGINAS (FIFO)")
    print("="*60)

    while True:
        referencias = ler_referencias()
        n_frames    = ler_frames()

        faults, historico = simular_fifo(referencias, n_frames)
        imprimir_resultado(referencias, n_frames, faults, historico)

        resp = input("  Rodar outra simulação? (s/n): ").strip().lower()
        if resp != "s":
            break

    print("\n  Simulação encerrada.\n")


if __name__ == "__main__":
    main()

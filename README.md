# Simuladores Didáticos de Sistemas Operacionais
Trabalho · Sistemas Operacionais · UFOPA

## Simuladores

| Arquivo | Tema | Algoritmo |
|---|---|---|
| `banqueiro.py` | Deadlocks | Algoritmo do Banqueiro |
| `fifo.py` | Memória Virtual | Substituição de Páginas FIFO |
| `fcfs_disco.py` | Escalonamento de Disco | FCFS |
| `alocacao_contigua.py` | Sistemas de Arquivos | Alocação Contígua |

Requer Python 3.6+. Sem dependências externas.

## Como executar

```bash
python3 banqueiro.py
python3 fifo.py
python3 fcfs_disco.py
python3 alocacao_contigua.py
```

## Exemplos de entrada

### Banqueiro (5 processos, 3 recursos)
```
Máximo:  P0:7 5 3 / P1:3 2 2 / P2:9 0 2 / P3:2 2 2 / P4:4 3 3
Alocação: P0:0 1 0 / P1:2 0 0 / P2:3 0 2 / P3:2 1 1 / P4:0 0 2
Disponível: 3 3 2
```

### FIFO
```
Referências: 1 2 3 4 1 2 5 1 2 3 4 5
Frames: 3
→ 9 page faults (75%)
```

### FCFS Disco
```
Posição inicial: 53
Fila: 98 183 37 122 14 124 65 67
→ 640 cilindros percorridos
```

### Alocação Contígua
```
Disco: 20 blocos
Arquivos: A(4), B(3), C(6), D(2)
→ [A][A][A][A][B][B][B][C][C][C][C][C][C][D][D][ ][ ][ ][ ][ ]
```

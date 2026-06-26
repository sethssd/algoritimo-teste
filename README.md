# Simuladores Didáticos de Sistemas Operacionais

Trabalho em Grupo 2 · Sistemas Operacionais · UFOPA

## Simuladores

### 1. Algoritmo do Banqueiro (`banqueiro.py`)
Prevenção dinâmica de deadlocks.

```bash
python3 banqueiro.py
```

**Entrada:**
1. Número de processos e tipos de recurso
2. Matriz de Máximo (linha por processo)
3. Matriz de Alocação atual (linha por processo)
4. Vetor de Recursos Disponíveis
5. Requisições interativas

**Exemplo rápido (5 processos, 3 recursos):**
```
Processos: 5   Recursos: 3

Máximo:        Alocação:      Disponível:
P0: 7 5 3      P0: 0 1 0      3 3 2
P1: 3 2 2      P1: 2 0 0
P2: 9 0 2      P2: 3 0 2
P3: 2 2 2      P3: 2 1 1
P4: 4 3 3      P4: 0 0 2

Sequência segura: P1 → P3 → P0 → P2 → P4
```

---

### 2. Substituição de Páginas FIFO (`fifo.py`)
Algoritmo First-In, First-Out para memória virtual.

```bash
python3 fifo.py
```

**Entrada:**
1. Sequência de referências de páginas (ex: `1 2 3 4 1 2 5`)
2. Número de frames disponíveis na RAM

**Exemplo:**
```
Referências: 1 2 3 4 1 2 5 1 2 3 4 5
Frames: 3
→ Page faults: 9 (75.0%)   Hits: 3 (25.0%)
```

## Requisitos

Python 3.6+. Sem dependências externas.

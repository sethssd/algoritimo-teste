# Simulador — Algoritmo do Banqueiro

Trabalho em Grupo 2 · Sistemas Operacionais · UFOPA

## Como executar

```bash
python banqueiro.py
```

Requer Python 3.6+. Sem dependências externas.

## Entrada esperada

1. Número de processos e de tipos de recurso
2. Matriz de Máximo (linha por processo)
3. Matriz de Alocação atual (linha por processo)
4. Vetor de Recursos Disponíveis
5. Requisições interativas (processo + vetor de pedido)

## Exemplo rápido (3 processos, 3 recursos)

```
Processos: 3   Recursos: 3

Máximo:        Alocação:      Disponível:
P0: 7 5 3      P0: 0 1 0      3 3 2
P1: 3 2 2      P1: 2 0 0
P2: 9 0 2      P2: 3 0 2

Sequência segura inicial: P1 → P0 → P2

Requisição P1: 1 0 2  → CONCEDIDO
Requisição P0: 0 2 0  → CONCEDIDO
```

## Lógica do algoritmo

- **Necessidade** = Máximo − Alocação  
- **Verificação de segurança**: simula execução de processos em ordem qualquer; se todos podem terminar, o estado é seguro.  
- **Concessão**: só ocorre se a concessão provisória mantiver o estado seguro.
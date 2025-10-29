# 🔎 Comparativo: Linear Search vs Binary Search

Este projeto demonstra, na prática, a diferença de desempenho entre **Linear Search** (busca linear) e **Binary Search** (busca binária) em Python, utilizando medições reais de tempo de execução.

---

## 🧠 Objetivo

O objetivo é **comparar a eficiência** dos dois algoritmos de busca e visualizar como o **tempo de execução cresce** conforme o tamanho da lista aumenta — relacionando com suas **complexidades de tempo (Big O)**:

| Algoritmo       | Complexidade | Descrição |
|-----------------|---------------|------------|
| **Linear Search** | O(n) | Percorre todos os elementos até encontrar o alvo |
| **Binary Search** | O(log n) | Divide a lista ordenada ao meio a cada iteração |

---

## ⚙️ Estrutura do Projeto

- `LinearSearch.py` → Implementa a busca linear e mede o tempo de execução.  
- `BinarySearch.py` → Implementa a busca binária e mede o tempo de execução.  
- `compare.py` → Executa ambos os algoritmos com diferentes tamanhos de lista e exibe os resultados.

---

| 🧩 Tamanho da lista | ⚡ Linear Search (O(n)) | 🚀 Binary Search (O(log n)) |
|---------------------:|------------------------:|-----------------------------:|
| 10                  | 0.0000040s             | 0.0000011s                  |
| 100                 | 0.0000102s             | 0.0000015s                  |
| 1.000               | 0.0000945s             | 0.0000021s                  |
| 100.000             | 0.0102431s             | 0.0000067s                  |


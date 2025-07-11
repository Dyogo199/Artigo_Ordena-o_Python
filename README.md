# Benchmark de Algoritmos de Ordenação – Python

Este projeto realiza a análise comparativa dos algoritmos de ordenação **Bucket Sort**, **Merge Sort** e **Bubble Sort** utilizando a linguagem Python. O código executa 10 testes para cada tamanho de vetor (100, 1.000, 10.000 e 100.000 elementos) e exibe os tempos de execução em milissegundos.

## 📌 Algoritmos implementados
- Bucket Sort
- Merge Sort
- Bubble Sort

## 🧪 Estrutura dos testes
Para cada tamanho de vetor:
- São gerados 10 vetores aleatórios com números reais entre 0 e 1000;
- Os três algoritmos são aplicados a cada vetor;
- O tempo de execução é medido individualmente;
- São exibidas duas tabelas:
  - **Tabela 1**: Tempos individuais por execução;
  - **Tabela 2**: Estatísticas (média, desvio padrão, mínimo e máximo).

## ▶️ Como executar

1. Instale a dependência:

```bash
pip install tabulate
Execute o script:

bash
Copiar
Editar
python sort_benchmark.py

📊 Exemplo de saída
📌 Testando com vetor de tamanho 1000...

🔎 Tabela 1 – Tempos individuais de execução (ms):
| Execução | Bucket Sort | Merge Sort | Bubble Sort |
|----------|--------------|------------|--------------|
| 1ª       | 0.51         | 0.73       | 13.25        |
...

📊 Tabela 2 – Estatísticas dos tempos de execução:
| Algoritmo   | Média | Desvio | Mínimo | Máximo |
|-------------|-------|--------|--------|--------|
| Bucket Sort | 0.48  | 0.05   | 0.40   | 0.59   |

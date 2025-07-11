import random
import time
import statistics
from tabulate import tabulate

# ---------- Algoritmos de Ordenação ----------

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int((num - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# ---------- Função de Benchmark ----------

def medir_tempo(func, arr):
    inicio = time.time()
    func(arr.copy())
    fim = time.time()
    return (fim - inicio) * 1000  # ms

# ---------- Função Principal ----------

def executar_testes(tamanhos, num_execucoes):
    for n in tamanhos:
        print(f"\n📌 Testando com vetor de tamanho {n}...\n")

        resultados = {
            "Bucket Sort": [],
            "Merge Sort": [],
            "Bubble Sort": []
        }

        for i in range(num_execucoes):
            vetor_base = [random.uniform(0, 1000) for _ in range(n)]

            resultados["Bucket Sort"].append(medir_tempo(bucket_sort, vetor_base))
            resultados["Merge Sort"].append(medir_tempo(merge_sort, vetor_base))
            resultados["Bubble Sort"].append(medir_tempo(bubble_sort, vetor_base))

        # Tabela Detalhada
        tabela_detalhada = []
        for i in range(num_execucoes):
            linha = [
                f"{i+1}ª Execução",
                f"{resultados['Bucket Sort'][i]:.2f}",
                f"{resultados['Merge Sort'][i]:.2f}",
                f"{resultados['Bubble Sort'][i]:.2f}"
            ]
            tabela_detalhada.append(linha)

        headers_detalhado = ["Execução", "Bucket Sort (ms)", "Merge Sort (ms)", "Bubble Sort (ms)"]
        print("🔎 Tabela 1 – Tempos individuais de execução (ms):\n")
        print(tabulate(tabela_detalhada, headers=headers_detalhado, tablefmt="grid"))

        # Tabela Resumo Estatístico
        tabela_resumo = []
        for nome in resultados:
            media = statistics.mean(resultados[nome])
            desvio = statistics.stdev(resultados[nome])
            minimo = min(resultados[nome])
            maximo = max(resultados[nome])
            tabela_resumo.append([
                nome,
                f"{media:.2f}",
                f"{desvio:.2f}",
                f"{minimo:.2f}",
                f"{maximo:.2f}"
            ])

        headers_resumo = ["Algoritmo", "Média (ms)", "Desvio Padrão", "Mínimo (ms)", "Máximo (ms)"]
        print("\n📊 Tabela 2 – Estatísticas dos tempos de execução:\n")
        print(tabulate(tabela_resumo, headers=headers_resumo, tablefmt="grid"))
        print("\n" + "-"*80 + "\n")

# ---------- Execução ----------

tamanhos_de_entrada = [10, 100, 1000, 10000, 100000]
num_execucoes = 10

executar_testes(tamanhos_de_entrada, num_execucoes)

import matplotlib.pyplot as plt
import numpy as np

# Dados
tamanhos_array = [1_000, 1_000, 5_000, 5_000, 10_000, 10_000, 50_000, 50_000, 100_000, 100_000]
tempos_ms = [1.81, 21.66, 8.69, 202.84, 16.25, 433.31, 89.35, 2386.84, 168.68, 5485.74]

# Dados dos percentuais (do arquivo resultados.json)
percentuais_ordenacao = [50.82, 95.84, 49.07, 97.9, 48.22, 97.99, 48.44, 98.14, 48.98, 98.42]
percentuais_primos = [19.91, 1.71, 21.03, 0.87, 21.38, 0.83, 22.0, 0.77, 21.11, 0.66]

# Separar dados por tipo
tamanhos_desordenados = [tamanhos_array[i] for i in range(0, len(tamanhos_array), 2)]  # Índices pares: C1, C3, C5, C7, C9
tempos_desordenados = [tempos_ms[i] for i in range(0, len(tempos_ms), 2)]

tamanhos_ordenados = [tamanhos_array[i] for i in range(1, len(tamanhos_array), 2)]    # Índices ímpares: C2, C4, C6, C8, C10
tempos_ordenados = [tempos_ms[i] for i in range(1, len(tempos_ms), 2)]

# Separar percentuais
perc_ord_desordenados = [percentuais_ordenacao[i] for i in range(0, len(percentuais_ordenacao), 2)]
perc_primos_desordenados = [percentuais_primos[i] for i in range(0, len(percentuais_primos), 2)]

perc_ord_ordenados = [percentuais_ordenacao[i] for i in range(1, len(percentuais_ordenacao), 2)]
perc_primos_ordenados = [percentuais_primos[i] for i in range(1, len(percentuais_primos), 2)]

# Criar figura com subplots
fig = plt.figure(figsize=(16, 10))

# Gráfico de linha
ax1 = plt.subplot(2, 2, (1, 2))
ax1.plot(tamanhos_desordenados, tempos_desordenados, 'o-', color='blue', linewidth=2, 
         markersize=8, label='Array Desordenado', alpha=0.8)
ax1.plot(tamanhos_ordenados, tempos_ordenados, 'o-', color='red', linewidth=2, 
         markersize=8, label='Array Já Ordenado', alpha=0.8)

ax1.set_xlabel('Tamanho do Array', fontsize=12)
ax1.set_ylabel('Tempo de Execução (ms)', fontsize=12)
ax1.set_title('Comparação de Performance: Array Desordenado vs Ordenado', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_yscale('log')
ax1.ticklabel_format(style='plain', axis='x')
ax1.set_xticks(tamanhos_desordenados)
ax1.set_xticklabels([f'{x:,}' for x in tamanhos_desordenados])

# Calcular médias dos percentuais para os gráficos de pizza
media_ord_desordenado = np.mean(perc_ord_desordenados)
media_primos_desordenado = np.mean(perc_primos_desordenados)
outros_desordenado = 100 - media_ord_desordenado - media_primos_desordenado

media_ord_ordenado = np.mean(perc_ord_ordenados)
media_primos_ordenado = np.mean(perc_primos_ordenados)
outros_ordenado = 100 - media_ord_ordenado - media_primos_ordenado

# Gráfico de pizza - Arrays Desordenados
ax2 = plt.subplot(2, 2, 3)
labels_desordenado = ['Ordenação', 'Primos', 'Outros']
sizes_desordenado = [media_ord_desordenado, media_primos_desordenado, outros_desordenado]
colors_desordenado = ['lightblue', 'lightgreen', 'lightgray']
explode_desordenado = (0.05, 0.05, 0)  # explode as fatias principais

wedges, texts, autotexts = ax2.pie(sizes_desordenado, labels=labels_desordenado, autopct='%1.1f%%', 
                                  colors=colors_desordenado, explode=explode_desordenado, 
                                  startangle=90, textprops={'fontsize': 10})
ax2.set_title('Distribuição de Tempo\nArrays Desordenados', fontsize=12, fontweight='bold')

# Gráfico de pizza - Arrays Ordenados
ax3 = plt.subplot(2, 2, 4)
labels_ordenado = ['Ordenação', 'Primos', 'Outros']
sizes_ordenado = [media_ord_ordenado, media_primos_ordenado, outros_ordenado]
colors_ordenado = ['lightcoral', 'lightgreen', 'lightgray']
explode_ordenado = (0.1, 0, 0)  # explode a fatia da ordenação

wedges, texts, autotexts = ax3.pie(sizes_ordenado, labels=labels_ordenado, autopct='%1.1f%%', 
                                  colors=colors_ordenado, explode=explode_ordenado, 
                                  startangle=90, textprops={'fontsize': 10})
ax3.set_title('Distribuição de Tempo\nArrays Já Ordenados', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# Estatísticas
print("=== COMPARAÇÃO DE PERFORMANCE ===")
for i in range(len(tamanhos_desordenados)):
    tamanho = tamanhos_desordenados[i]
    tempo_des = tempos_desordenados[i]
    tempo_ord = tempos_ordenados[i]
    diferenca = tempo_ord / tempo_des
    print(f"Tamanho {tamanho:,}: Desordenado = {tempo_des:.2f}ms | Ordenado = {tempo_ord:.2f}ms | Diferença = {diferenca:.1f}x")
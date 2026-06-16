import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados1 = pd.read_csv("Tarefa2/dados/Tentativa1.csv")
dados2 = pd.read_csv("Tarefa2/dados/Tentativa2.csv")

std1 = np.std(dados1['Calor latente (j/g)'])
std2 = np.std(dados2['Calor latente (j/g)'])

# Erro estatístico 
err1 = np.sqrt((std1/np.sqrt(14))**2)
err2 = np.sqrt((std2/np.sqrt(16))**2)

plt.title(f"Frequênca de Calor Latente - Tentativa 1")
plt.xlabel("Calor latente (j/g)")
plt.ylabel("Frequência")
contagem, bordas, barras = plt.hist(dados1['Calor latente (j/g)'], bins=7, edgecolor='black')
plt.xticks(bordas, rotation=45) 
plt.xlim(bordas[0], bordas[-1])
plt.savefig("Tarefa2/graficos/tentativa1.png")
plt.close()

plt.title(f"Frequênca de Calor Latente - Tentativa 2")
plt.xlabel("Calor latente (j/g)")
plt.ylabel("Frequência")
contagem, bordas, barras = plt.hist(dados2['Calor latente (j/g)'], bins=7, edgecolor='black')
plt.xticks(bordas, rotation=45) 
plt.xlim(bordas[0], bordas[-1])
plt.savefig("Tarefa2/graficos/tentativa2.png")
plt.close()

with open("Tarefa2/dados/resultado.txt", "w") as f:
    f.write(f"Tentativa 1: {np.mean(dados1['Calor latente (j/g)'])} +- {err1}\n")
    f.write(f"Tentativa 2: {np.mean(dados2['Calor latente (j/g)'])} +- {err2}\n")
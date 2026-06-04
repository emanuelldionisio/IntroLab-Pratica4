import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# T_kelvin = 1 / (A + B * np.log(R) + C * (np.log(R) ** 3))

# Água a °C: 1.5

def steinharthart(res, a, b, c):
    return 1/(a + b * np.log(res) + c * np.log(res)**3)

dados = [pd.read_csv(f"Tarefa1/dados/term{i+1}.csv") for i in range(6)]
result = [0] * 6

for i in range(6):
    logs_R = np.log(np.array(dados[i]['res']))  # log(R)
    A = np.array([
        [1, logs_R[0], logs_R[0] ** 3],
        [1, logs_R[1], logs_R[1] ** 3],
        [1, logs_R[2], logs_R[2] ** 3]
    ])
    
    B = np.array([1 / dados[i]['temp'][j] for j in range(3)])  # 1/T_kelvin
    
    result[i] = np.linalg.solve(A, B)
    
    print(f"Termistor {i+1}: {result[i]}")

    res = np.linspace(100, 50000, 1000)

    plt.title(f"Termistor {i+1}")
    plt.xlabel("Resistência (Ohm)")
    plt.ylabel("Temperatura (K)")
    plt.plot(res, steinharthart(res, *result[i]))
    plt.savefig(f"Tarefa1/graficos/term{i+1}.png")
    plt.close()
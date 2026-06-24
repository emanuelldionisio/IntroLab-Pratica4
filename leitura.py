"""Modificar a variável porta para a desejada (Ex: /COM8, /dev/ttyUSB0)
Modificar a baudrate para a velocidade do monitor
Gera um .txt com a data atual"""

import serial
import time
from datetime import datetime
from uncertainties import ufloat
import uncertainties
import uncertainties.unumpy as unp
import numpy as np

class Termistor():
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
    def obter_temperatura(self, res):
        try:
            return 1 / (self.A + self.B * unp.log(res) + self.C * unp.log(res)**3)
        except ValueError:
            return ufloat(0, 0)

termistores = []
for i in range(6):
    dados_calibracao = np.load(f"calibracao/term{i+1}_calibrados.npz")
    valores_nominais = dados_calibracao["nominais.npy"]
    matriz_covariancia = dados_calibracao["covariancia"]
    A_coef, B_coef, C_coef = uncertainties.correlated_values(valores_nominais, matriz_covariancia)
    termistores.append(Termistor(A_coef, B_coef, C_coef))
porta='/dev/ttyUSB0'

# Configura a porta serial
ser = serial.Serial(
    port=porta,
    baudrate=115200,
    timeout=1
)

print(f"Lendo dados da {porta}...")

entrada1, entrada2, entrada3, entrada4, entrada5, entrada6 = [], [], [], [], [], []

try:
    t0 = time.perf_counter()
    while True:
        if ser.in_waiting > 0:
            """Ler quantidade de linhas igual à qtd de linhas imprimidas no serial"""
            res1 = ser.readline().decode('utf-8', errors='ignore').strip()
            res2 = ser.readline().decode('utf-8', errors='ignore').strip()
            # res3 = ser.readline().decode('utf-8', errors='ignore').strip()
            # res4 = ser.readline().decode('utf-8', errors='ignore').strip()
            # res5 = ser.readline().decode('utf-8', errors='ignore').strip()
            # res6 = ser.readline().decode('utf-8', errors='ignore').strip()
            _ = ser.readline().decode('utf-8', errors='ignore').strip()

            t = time.perf_counter() - t0

            temp1 = termistores[0].obter_temperatura(float(res1))
            temp2 = termistores[5].obter_temperatura(float(res2))
            # temp3 = term3.obter_temperatura(res3)
            # temp4 = term4.obter_temperatura(res4)
            # temp5 = term5.obter_temperatura(res5)
            # temp6 = term6.obter_temperatura(res6)

            entrada1.append([f"{t}", f"{temp1.nominal_value}", f"{temp1.std_dev}"])
            entrada2.append([f"{t}", f"{temp2.nominal_value}", f"{temp2.std_dev}"])
            # entrada3.append([f"{time.time()}", f"{temp3.nominal_value}", f"{temp3.std_dev}"])
            # entrada4.append([f"{time.time()}", f"{temp4.nominal_value}", f"{temp4.std_dev}"])
            # entrada5.append([f"{time.time()}", f"{temp5.nominal_value}", f"{temp5.std_dev}"])
            # entrada6.append([f"{time.time()}", f"{temp6.nominal_value}", f"{temp6.std_dev}"])

            print(f"{temp1}|\t" + 
                 f"{temp2}|\t" +
                #  f"{linha3}|\t" + 
                #  f"{linha4}" + 
                "")

except KeyboardInterrupt:
    print("\nLeitura interrompida.")

finally:
    ser.close()
    print("Porta serial fechada.")

"""Imprimir em um arquivo diferente para cada linha"""
with (
    open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_entrada1.txt", "w") as saida1,
    open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_entrada2.txt", "w") as saida2,
    # open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_entrada3.txt", "w") as saida3,
    # open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_entrada4.txt", "w") as saida4,
    # open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_entrada5.txt", "w") as saida5,
    # open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_entrada6.txt", "w") as saida6
):
    saida1.write("\n".join([",".join(linha) for linha in entrada1]))
    saida2.write("\n".join([",".join(linha) for linha in entrada2]))
    # saida3.write("\n".join(entrada3))
    # saida4.write("\n".join(entrada4))
    # saida5.write("\n".join(entrada5))
    # saida6.write("\n".join(entrada6))
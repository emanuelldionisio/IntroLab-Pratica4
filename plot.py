import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pot = 4.9
massa = 69.7
# Potencia do que deu certo 1: 9
# Massa do que deu certo 1: 160 + 58.1

# pot inox 9
# tempo inox 234

# 6.4

df = pd.read_csv(
    "2026-06-22_19-24-26_entrada1.txt",
    sep=":",
    names=["t", "T"]
)

df = df[3500:4500]

# Parse timestamps
tempo = pd.to_datetime(df["t"], format="%H-%M-%S-%f")

# Seconds since first measurement
tempo_s = (tempo - tempo.iloc[0]).dt.total_seconds()

tempo_s = tempo_s[:]
coiso = df["T"][:]

params, v = np.polyfit(tempo_s, coiso, 1, cov=True)
coisaParaPlotar = np.poly1d(params)(tempo_s)

print(params)
print(v)

coisa = pot / (params[0] * massa)
print(coisa)
plt.plot(tempo_s,coisaParaPlotar)
plt.plot(tempo_s, coiso)
plt.xlabel("Time (s)")
plt.ylabel("Temperature")
plt.show()
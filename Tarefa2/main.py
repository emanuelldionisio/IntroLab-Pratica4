def calcular_calor_latente(massa_gelo, tempo, potencia):
    """
    Calcula o calor latente de fusão do gelo a partir da massa, tempo e potência fornecidos pelo usuário.
    - `massa_gelo`: a massa do gelo (kg)
    - `tempo`: o tempo durante o qual a potência foi aplicada (s)
    - `potencia`: a potência aplicada para derreter o gelo (W)
    O calor latente é calculado usando a fórmula: Q = P * t / m
    onde Q é o calor latente, P é a potência, t é o tempo e
    m é a massa do gelo.
    """
    return potencia * tempo / massa_gelo

massa_gelo = float(input())
tempo = float(input())
potencia = float(input())

calor_latente = calcular_calor_latente(massa_gelo, tempo, potencia)

print(calor_latente)
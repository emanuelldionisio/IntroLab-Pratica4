import numpy as np

# T_kelvin = 1 / (A + B * np.log(R) + C * (np.log(R) ** 3))

logs_R = np.log(np.array([float(i) for i in input().split()]))  # log(R)
A = np.array([
    [1, logs_R[0], logs_R[0] ** 3],
    [1, logs_R[1], logs_R[1] ** 3],
    [1, logs_R[2], logs_R[2] ** 3]
])

B = np.array([1 / float(i) for i in input().split()])  # 1/T_kelvin

result = np.linalg.solve(A, B)

print(result)
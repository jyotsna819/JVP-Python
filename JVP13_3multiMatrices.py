from collections import defaultdict

data = [
    "a 0 0 1", "a 0 1 2",
    "a 1 0 3", "a 1 1 4",
    "b 0 0 5", "b 0 1 6",
    "b 1 0 7", "b 1 1 8"
]

A = defaultdict(dict)
B = defaultdict(dict)

for line in data:
    matrix, i, j, val = line.split()
    i, j, val = int(i), int(j), float(val)
    if matrix == 'a':
        A[i][j] = val
    else:
        B[i][j] = val

result = defaultdict(float)

for i in A:
    for j in B[0]:
        for k in A[i]:
            if k in B and j in B[k]:
                result[(i, j)] += A[i][k] * B[k][j]

for k, v in result.items():
    print(f'{k} {v}')

def obst(n, p, q):
    e = [[0]*(n+2) for _ in range(n+2)]
    w = [[0]*(n+2) for _ in range(n+2)]

    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]

    for length in range(1, n+1):
        for i in range(1, n-length+2):
            j = i + length - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j-1] + q[j]
            for r in range(i, j+1):
                cost = e[i][r-1] + e[r+1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost

    return e[1][n]

n = int(input("Enter number of keys: "))

p = list(map(float, input("Enter p, separated by spaces: ").split()))
q = list(map(float, input("Enter q, separated by spaces: ").split()))

if len(p) != n or len(q) != n + 1:
    print("Invalid input lengths for p or q.")
else:
    result = obst(n, p, q)
    print(f"Optimal cost: {result:.4f}")

# Initially just to get briefed with the Topic

# Question 1: Fibonnaci Series
'''
def Fibo(n):
    F = [0 for _ in range(n)]
    if n <= 1:
        return 1
    F[0] = F[1] = 1
    for i in range(2, n):
        res = Fibo(n-2) + Fibo(n-1)
        i += 1
    return res

f = Fibo(int(input("Enter Any Number: ")))
'''

# Question 2: Binomial Coefficient / Pascal Triangle
'''
def BCP(n, r):
    # Memoization Approach
    # if (n == r) or (r == 0):
    #     return 1
    # res = BCP(n-1, r-1) + BCP(n-1, r)
    # return res

    # Tablation Approach
    for i in range(n):
        for j in range(r):
            if (i >= j):
                if (i == j) or (j == 0):
                    M[i][j] = 1
                else:
                    M[i][j] = M[i-1][j-1] + M[i-1][j]   
    return M[n][r]                      

b = BCP(int(input("Enter Any Number: ")), int(input("Enter Any Power: ")))
'''

# Question 3: Floyd Warshall Shortest Path
'''
def Floyd(M[][], n):
    D = M
    P = 0
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if (D[i][j] > (D[i][k] + D[k][j])):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                    P[i][j] = k
    return D
'''

# Question 4: Matrix Chain Multiplication
'''
def MCM(n, d[]):
    for i in range(1, n):
        M[i][i] = 0
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i+d
            M[i][j] = min(M[i][k] + M[k+1][j] + (d[i-1]*d[k]*d[j]))
    return M[1][n]
'''

# Question 5: Binary Search Tree
'''
def BST(x, root):
    p = root
    while (p != NULL):
        if (p.key == x):
            return p
        if (p.key < root):
            p.left
        p.right
    return NULL
'''
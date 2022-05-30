import math
from copy import deepcopy
from tabulate import tabulate

def matrixChainProduct(d):
  #returns table M with entries [minimum multiplications, cutoff matrix]
  n = len(d)
  M = [[[0] for x in range(n)] for y in range(n)]
  for b in range(1, n):
    for i in range(1, n-b):
      k = i + b
      m = d[i-1] * d[k]
      M[i][k][0] = math.inf
      for j in range(i, k):
        N = M[i][j][0] + m * d[j] + M[j+1][k][0]
        if N == M[i][k][0]:
          M[i][k].append(j)
        elif N < M[i][k][0]:
          M[i][k][0] = N
          M[i][k][1:] = [j]
  M.pop(0)
  for x in range(n-1):
    M[x].pop(0)
  return M

def matrixMultShortestPaths(W):
  def matMul(A, B):
    n = len(A)
    C = [ [[0, 0] for j in range(n)]  for i in range(n)]
    for i in range(n):
      for j in range(n):
        C[i][j][0] = math.inf
        if i == j:
          C[i][j] = [0, 0]
        for k in range(n):
          #print(i, k, k, j)
          newCost = A[i][k][0] + B[k][j][0]
          if newCost < C[i][j][0]:
            #print(i, j, k)
            C[i][j][0] = newCost
            C[i][j][1] = k+1
    return C

  #returns table W with entries [shortest path length, intermediary node (0 is direct edge)]
  n = len(W)
  E = [[[x, 0] for x in y] for y in W]
  W = deepcopy(E)
  
  iter = 1
  while iter != n-1:
    if 2*iter < n:
      W = matMul(W, W)
      iter *= 2
    else:
      W = matMul(W, E)
      iter += 1
    #print(iter, tabulate(W))
  return W

def floydWarshall(W):
  #returns table W with entries [shortest path length, intermediary node (0 is direct edge)]
  n = len(W)
  D = deepcopy(W)
  D = [[[x, 0] for x in y] for y in D]
  for m in range(0, n):
    for i in range(0, n):
      for j in range(0, n):
        if D[i][m][0] + D[m][j][0] < D[i][j][0]:
          D[i][j][0] = D[i][m][0] + D[m][j][0]
          D[i][j][1] = m+1
  return D

def CYK(P, s):
  def getProductions(tail):
    result = set([])
    for rule in P:
      if tail in P[rule]:
        result.add(rule)
    return result
    
  n = len(s)
  V = [[[] for x in range(n)] for y in range(n)]
  for i in range(n):
    V[i][i] = list(getProductions(s[i]))
    V[i][i].sort()
  #print(V)
  for b in range(1, n+1):
    for i in range(0, n-b):
      k = i + b
      #print(i, k)
      for j in range(i, k):
        #print(j)
        for rule in P:
          for tail in P[rule]:
            #print(tail)
            if len(tail) == 1:
              continue
            if tail[0] in V[i][j] and tail[1] in V[j+1][k]:
              V[i][k].append(rule)
              V[i][k].sort()
  return V

# def makeTrees(V, P, startSymbol, string):
#   def getTrees(i, k, symbol):
#     print(i, k, symbol)
#     if i == k:
#       print(string[i])
#       return string[i]
#     for j in range(abs(i-k)):
#       #print(V[i-1][k-1-j], V[i-1-j][k-1])
#       print(j)
#       print(i, k-j-1, i-j-1, k)
#       for tail in P[symbol]:
#         if len(tail) == 1: continue
#         if tail[0] in V[i-1][k-1-j] and tail[1] in V[i-1-j][k-1]:
#           print(tail)
#           getTrees(i, k-j, tail[0])
#           getTrees(abs(i-j), k, tail[1])
#   getTrees(0, len(V)-1, startSymbol)

# def travellingSalesperson(d):
#   def powerset(list, minLen):
#     sets = list(itertools.combinations(s, ))
#   n = len(d)
#   l = {(frozenset([1, x])):d[0][x-1] for x in range(2, n+1)}
#   p = {(frozenset([1, x])):1 for x in range(2, n+1)}

#   for k in range(2, n):
#     format
#   print(l)
#   print(p)
  
if __name__ == "__main__":
  d = [3, 2, 5, 2, 4, 3]
  res = matrixChainProduct(d)
  print("Matrix chain product")
  print(tabulate(res))
  print()
  
  i = math.inf
  W = [[0, 4, i, -2, i, i],
       [4, 0, 3, i, i, i],
       [i, 3, 0, i, i, -2],
       [i, i, i, 0, 3, i],
       [i, -1, i, 3, 0, 4],
       [i, i, i, i, 4, 0]]
  res = floydWarshall(W)
  print("Floyd Warshall")
  print(tabulate(res))
  print()
  
  P = {
    "S":["AA", "BB", "a", "b"],
    "A":["AE", "BC", "a"],
    "B":["BE", "AD", "b"],
    "C":["AA", "CE"],
    "D":["BB", "DE"],
    "E":["AB", "BA", "EE"]
  }
  s = "aaabab"
  res = CYK(P, s)
  print("CYK Algorithm")
  print(tabulate(res))
  print()
  #makeTrees(res, P, "S", s)

  i = math.inf
  W = [[0, 5, 3, i, i, i],
       [i, 0, i, 5, i, i],
       [i, 4, 0, i, 3, i],
       [i, 8, i, 0, -5, 12],
       [i, 7, -2, i, 0, -1],
       [i, i, i, i, 8, 0]]
  res = matrixMultShortestPaths(W)
  print("MATRIX MULTIPLICATION")
  print(tabulate(res))
  print()

  # W = [[0, 5, 2, 2, 5],
  #      [5, 0, 2, 4, 6],
  #      [2, 2, 0, 1, 4],
  #      [2, 4, 1, 0, 2],
  #      [5, 6, 4, 2, 0]]
  # res = travellingSalesperson(W)
  # print("TRAVELLING SALESPERSON")
  # print(tabulate(res))
  # print()
  
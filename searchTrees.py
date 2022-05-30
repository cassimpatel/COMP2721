def verifySearch(sequence, upper, lower, key):
    sequence.append(key)
    #print(sequence)
    n = len(sequence)
    left = True
    if key < sequence[0]:
        left = True
    else:
        left = False
    for i in range(1, n):
        #print(key, sequence[i-1])
        if i == 0:
            left = key < sequence[0]
        else:
            left = key < sequence[i-1]
        #print("goin left", left)
        for j in range(i, n):
            #print(j)
            if left and sequence[j] > sequence[i-1]:
                return False
            elif not left and sequence[j] < sequence[i-1]:
                return False
            #print(i, j)
            #pass
            
    return True

searches = [
    [900, 5, 765, 105, 764, 333, 357, 352],
    [898, 56, 292, 740, 212, 555, 342, 344],
    [999, 106, 897, 212, 295, 898, 605],
    [8, 412, 411, 156, 259, 279, 294, 380, 360]
]
for sequence in searches:
    print(verifySearch(sequence, 1000, 1, 364))
print()
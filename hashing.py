from tabulate import tabulate

class HashEntry():
  status = "FREE"
  k = None
  i = None

  def __init__(self, key=None, state="FREE", info=None):
    self.status = state
    self.k = key
    self.i = info

  def __repr__(self):
    return "[{}] hash table entry '{}':'{}'".format(self.status, self.k, self.i)
  
  def copy(self):
    return HashEntry(self.k, self.status, self.i)

  def used(self):
    return self.status == "USED"

# uses linear probing
class HashTable():
  m = 0
  n = 0
  h1 = None
  T = []

  def __init__(self, size, hashFunc):
    self.m = size
    self.n = 0
    self.h1 = hashFunc
    self.T = [HashEntry() for i in range(m)]

  def copy(self):
    newObj = HashTable(self.m, self.h1)
    newObj.T = [entry.copy() for entry in self.T]
    return newObj

  def isEmpty(self):
    for entry in self.T:
      if entry.status == "USED":
        return False
    return True

  def setTable(self, keys):
    newTable = self.copy()
    if len(keys) != newTable.m:
      raise Exception("invalid size for manual table loading")

    for i in range(newTable.m):
      if keys[i] != None:
        newTable.T[i] = HashEntry(keys[i], "USED", None)
      else:
        newTable.T[i] = HashEntry(None, "FREE", None)
    return newTable

  def getLoadFactor(self):
    return self.n/self.m

  def h(self, k, i):
    return (self.h1(k) + i) % self.m
  
  def probingOrder(self, k):
    return [self.h(k, i) for i in range(self.m)]

  def member(self, key):
    for index in self.probingOrder(key):
      entry = self.T[index]
      #print("checking index", index, "for", key)
      if entry.status == "FREE":
        break
      elif entry.k == key:
        return True
    return False
  
  def lookUp(self, key):
    for index in self.probingOrder(key):
      entry = self.T[index]
      #print("checking index", index, "for", key)
      if entry.status == "FREE":
        break
      elif entry.k == key:
        return entry.i
    return None

  def insert(self, key, info=None):
    if self.getLoadFactor == 1:
      raise Exception("Cannot insert new element into a full table")
    elif self.member(key):
      raise Exception("Key already exists in dictionary")
      
    newHashTable = self.copy()
    for index in self.probingOrder(key):
      entry = self.T[index]
      if entry.status != "USED":
        newHashTable.T[index] = HashEntry(key, "USED", info)
        break
    newHashTable.n += 1
    return newHashTable

  def insertMultiple(self, keys, infos=None):
    num = len(keys)
    if infos == None:
      infos = [None for x in range(num)]
    newHashTable = self.copy()
    
    for i in range(num):
      newHashTable = newHashTable.insert(keys[i], infos[i])
    return newHashTable

  def delete(self, key):
    newHashTable = self.copy()

    for index in self.probingOrder(key):
      entry = self.T[index]
      if entry.status == "FREE":
        break
      elif entry.k == key:
        newHashTable.T[index].status = "FREE AGAIN"
        return newHashTable

    raise Exception("Key to remove is not in hash table")
    
  def getKeys(self):
    return [self.T[x].k for x in range(self.m) if self.T[x].used()]

  def getAverageSearchTime(self):
    keys = self.getKeys()
    probings = [0 for k in keys]

    for a in range(len(keys)):
      k = keys[a]
      for index in self.probingOrder(k):
        probings[a] += 1
        if self.T[index].used() and self.T[index].k == k:
          break
        elif self.T[index].status == "FREE":
          break
    return sum(probings)/len(probings)

  def show(self):
    result = []
    headers=["index", "status", "key", "info"]
    
    for i in range(self.m):
      entry = self.T[i]
      status = entry.status
      key = entry.k if entry.used() else ""
      info = entry.i if entry.used() else ""
      result.append([i, status, key, info])
      
    print(tabulate(result, headers, tablefmt="pretty"))

class QuadraticHashTable(HashTable):
  c1 = None
  c2 = None

  def __init__(self, size, hashFunc, c1, c2):
    self.m = size
    self.n = 0
    self.h1 = hashFunc
    self.c1 = c1
    self.c2 = c2
    self.T = [HashEntry() for i in range(self.m)]

  def copy(self):
    newObj = QuadraticHashTable(self.m, self.h1, self.c1, self.c2)
    newObj.T = [entry.copy() for entry in self.T]
    return newObj
    
  def h(self, k, i):
    return (self.h1(k) + int(self.c1*i + self.c2*i**i)) % self.m

class DoubleHashTable(HashTable):
  h2 = None

  def __init__(self, size, hashFunc, secondFunc):
    self.m = size
    self.n = 0
    self.h1 = hashFunc
    self.h2 = secondFunc
    self.T = [HashEntry() for i in range(self.m)]

  def copy(self):
    newObj = DoubleHashTable(self.m, self.h1, self.h2)
    newObj.T = [entry.copy() for entry in self.T]
    return newObj

  def h(self, k, i):
    return (self.h1(k) + i*self.h2(k)) % self.m

class BrentHashTable(DoubleHashTable):
  def copy(self):
    newObj = BrentHashTable(self.m, self.h1, self.h2)
    newObj.T = [entry.copy() for entry in self.T]
    return newObj
    
  def insert(self, key, info=None):
    if self.getLoadFactor == 1:
      raise Exception("Cannot insert new element into a full table")
    elif self.member(key):
      raise Exception("Key already exists in dictionary")
      
    newHashTable = self.copy()
    for index in newHashTable.probingOrder(key):
      entry = newHashTable.T[index]
      if entry.status != "USED":
        newHashTable.T[index] = HashEntry(key, "USED", info)
        break
      elif entry.status == "USED":
        j = index
        k2 = entry.k
        j1 = (j + self.h2(key)) % self.m
        j2 = (j + self.h2(k2)) % self.m

        if newHashTable.T[j1].used() and not newHashTable.T[j2].used():
          oldEntry = newHashTable.T[index]
          newHashTable.T[j2] = HashEntry(oldEntry.k, "USED", oldEntry.i)
          newHashTable.T[index] = HashEntry(key, "USED", info)
          break
    newHashTable.n += 1
    return newHashTable

  def insertMultiple(self, keys, infos=None):
    num = len(keys)
    if infos == None:
      infos = [None for x in range(num)]
    newHashTable = self.copy()
    
    for i in range(num):
      newHashTable = newHashTable.insert(keys[i], infos[i])
    return newHashTable

if __name__ == "__main__":
  print("Running hash table test")
  
  # Linear probing example
  m = 8
  def h1(k):
    return k % m
  x = HashTable(m, h1)
  x = x.insertMultiple([10, 19, 31, 22, 14, 16])
  x.show()
  print(x.getAverageSearchTime())

  # Quadratic probing example
  m = 8
  def h1(k):
    return k % m
  x = QuadraticHashTable(m, h1, 0.5, 0.5)
  x = x.insertMultiple([10, 19, 31, 22, 14, 16])
  x.show()
  print(x.getAverageSearchTime())

  # Double hashing example
  m = 7
  def h1(k):
    return k % 7
  def h2(k):
    return 1 + (k % 5)
  x = DoubleHashTable(m, h1, h2)
  x = x.insertMultiple([10, 19, 31, 22, 14, 16])
  x.show()
  print(x.getAverageSearchTime())

  # Brent's double hashing example
  m = 7
  def h1(k):
    return k % 7
  def h2(k):
    return 1 + (k % 5)
  x = BrentHashTable(m, h1, h2)
  x = x.insertMultiple([10, 19, 31, 22, 14, 16])
  x.show()
  print(x.getAverageSearchTime())

  print()

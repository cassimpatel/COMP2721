class HashEntry:
  status = "FREE"
  k = None
  i = None

  def __init__(self, key, state="FREE", info=None):
    self.status = state
    self.k = key
    self.i = info

  def __repr__(self):
    return None
  
  def __copy__(self):
    return None

  def __deepcopy__(self):
    return None

# uses linear probing
class HashTable:
  m = 0
  n = 0
  T = []
  h1 = None

  def __init__(self, size, hashFunc):
    return None

  def __repr__(self):
    return None

  def __copy__(self):
    return None

  def __deepcopy__(self):
    return None

  def isEmpty(self):
    return None

  def getLoadFactor(self):
    return None

  def h(self, k, i):
    return None
  
  def probingOrder(self, k):
    return None

  def member(self, key):
    return None
  
  def lookUp(self, key):
    return None

  def insert(self, key, info=None):
    # add functionality to deal with inserting an array of keys
    return None

  def delete(self, key):
    return None

  def getKeys(self):
    return None

  def getAverageSearchTime(self):
    return None

class QuadraticHashTable(HashTable):
  c1 = None
  c2 = None

  def __init__(self, size, hashFunc, c1, c2):
    return None

  def h(self, k, i):
    return None

class DoubleHashTable(HashTable):
  h2 = None

  def __init__(self, hashFunc):
    return None

  def h(self, k, i):
    return None


class BrentHashTable(DoubleHashTable):
  def insert(self, key, info=None):
    # add functionality to deal with array of keys
    return None

if __name__ == "__main__":
  print("Running hash table test")
  print()

class HashTable:
  m = 0
  n = 0
  h = []

  def __init__(self, m):
    self.m = m
    self.n = 0
    self.h = ["FREE" for x in range(m)]

  def isEmpty(self):
    return [type(x) == type(1) for x in self.h].contains("True")

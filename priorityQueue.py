import copy
import math

class HeapNode():
    # element key (priority) and auxiliary information
    k = None
    e = None

    def __init__(self, k, e=None):
        self.k = k
        self.e = e
    
    def __repr__(self):
        return "Priority {} heap node [{}]".format(self.k, self.e)

    def __copy__(self):
        newObj = HeapNode(self.k, self.e)
        return newObj

    def __lt__(self, other):
        return self.k < other.k

class BinaryHeap():
    H = []

    def __init__(self):
        self.H = []
    
    def __repr__(self):
        return "Binary heap: {}".format(", ".join([str(x.k) for x in self.H]))

    def __copy__(self):
        newObj = BinaryHeap()
        newObj.H = [copy.copy(x) for x in self.H]
        return newObj

    def isEmpty(self):
        return len(self.H) == 0

    def numElem(self):
        return len(self.H)

    def setUp(self, priorities, infos=None):
        newObj = copy.copy(self)
        newObj.H = []
        if infos == None:
            infos = [None for x in range(len(priorities))]
        for i in range(len(priorities)):
            newObj.H.append(HeapNode(priorities[i], infos[i]))
        return newObj

    def insert(self, k, i=None):
        newObj = copy.copy(self)
        newObj.H.append(HeapNode(k, i))
        newObj.toggleUp(newObj.numElem() - 1)
        return newObj

    def decreaseKey(self):
        pass

    def peek(self):
        minElem = self.H[0]
        return (minElem.i, minElem.k)

    def deleteMin(self):
        newObj = copy.copy(self)
        newObj.H[0], newObj.H[-1] = newObj.H[-1], newObj.H[0]
        del newObj.H[-1]
        newObj.toggleDown(0)
        return newObj

    def toggleUp(self, i):
        if i > 1:
            j = math.floor((i-1)/2)
            if self.H[i] < self.H[j]:
                self.H[i], self.H[j] = self.H[j], self.H[i]
                self.toggleUp(j)

    def toggleDown(self, i):
        # print("toggle down", i, self.H[i].k)
        i += 1
        n = self.numElem()
        if 2*i > n:
            return
        if 2*i < n:
            left = 2*i
            right = 2*i + 1
            # print("left", left, "right", right)
            j = left if self.H[left-1] < self.H[right-1] else right
        else:
            j = 2*i
        i -=1
        j -=1
        if self.H[j] < self.H[i]:
            self.H[i], self.H[j] = self.H[j], self.H[i]
            self.toggleDown(j)

    def buildHeap(self, array):
        newObj = copy.copy(self)
        newObj = newObj.setUp(array)
        for i in range(math.floor(len(array)/2), -1, -1):
            newObj.toggleDown(i)
        return newObj

class BinomialHeapNode(HeapNode):
    degree = None
    child = None
    sibling = None

    def __init__(self, k, e=None):
        self.k = k
        self.e = e
        self.degree = 0
        self.child = None
        self.sibling = None

    def __repr__(self):
        return "Priority {} degree-{} binomial heap node [{}]".format(self.k, self.degree, self.e)

    def __copy__(self):
        newObj = BinomialHeapNode(self.k, self.e)
        return newObj    

class BinomialTree():
    root = None

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __copy__(self):
        pass

    def link(self, other):
        pass

class BinomialHeap():
    root = None

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __copy__(self):
        pass

    def isEmpty(self):
        pass

    def insert(self):
        pass

    def minimum(self):
        pass

    def deleteMin(self):
        pass

    def peek(self):
        pass

    def merge(self, other):
        pass

if __name__ == "__main__":
    print("priority queue tests")

    x = BinaryHeap()
    print("Empty heap", x)
    x = x.buildHeap([2, 4, 5, 8, 6, 7])
    print(x)
    print("After insertion of 3", x.insert(3))
    print("After deletion of position 1", x.deleteMin())

    print()
# we need a node, so we write the class for Node
class Node:
    def __init__(self, key, value):
        self.key=key
        self.value = value
        # we need two pointers for the future use
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # we gotta know the capacity, since we use it if our put overexeeds the capacity 
        self.cap = capacity
        self.cache = {} # map key to node
        self.left, self.right = Node(0,0), Node(0,0)
        # initially we want these nodes to be connected to each other, since we want to put the node in the middle
        self.left.next = self.right
        self.right.prev = self.left
        # left for LRU, right for MRU

    #remove from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next,nxt.prev = nxt, prev

    
    # inser at right
    def insert(self, node):
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # TODO: update most recent
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache)> self.cap:
            #remove from the list and delte LRU from the cache(or the HashMap)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        

class Node:
    def __init__(self, term, docid, freq):
        self.term = term
        self.docid = docid
        self.freq = freq
        self.next = None

    def __repr__(self, term, docid, freq):
        return self.term, self.docid, self.freq

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        for node in self:
            nodes.append(str(node.term) + ", " + str(node.docid) + ", " + str(node.freq))
        return "Postings: " + str(nodes)

    def AddToFront(self, newterm, newid, newfreq):
        NewNode = Node(newterm, newid, newfreq)
        if self.head is None:
            self.tail = NewNode
        
        NewNode.next = self.head
        self.head = NewNode

    def AddToEnd(self, newterm, newid, newfreq):
        NewNode = Node(newterm, newid, newfreq)
        NewNode.next = None

        if self.tail is None:
            self.head = NewNode
        else:
            self.tail.next = NewNode
        
        self.tail = NewNode
    
    def GetList(self):
        for node in self:
            return node.term, node.docid, node.freq

    def GetTermList(self, value):
        test = []
        for node in self:
            if node.term == value:
                test.append([node.docid, node.freq])
        return test
                

    def Print(self):
        for node in self:
            print(str(node.docid) + " " + str(node.freq))
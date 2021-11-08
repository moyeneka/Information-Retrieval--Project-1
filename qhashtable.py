# Created by Ang Li
# October 2, 2016
# Modified by Marion Chiariglione
# September 22, 2018
import hashlib
from collections import deque

# Regular hashtable, except values are numDocs + Linked List pairs instead of frequency counts. Used for tracking all doc frequencies
class QueryHashTable(HashTable):
    # Pair of numDocs and Linked List for cross-file referencing
    class Entry:
        def __init__(self, data):
            self.numDocs = 1
            self.files = deque()
            self.files.append(data)

    def __init__(self, table_size):
        HashTable.__init__(self, table_size)

    
    # Override regular insert, replace frequency count with Entry class
    def insert(self, key, data): # insert k,v to the hash table
        hashvalue = self.hashfunction(key)  # location to insert
        if self.data[hashvalue] == None:
            #self.slots[hashvalue] = key
            self.data[hashvalue] = self.Entry(data)
            self.uniqueTokens += 1
        else:
            if self.data[hashvalue] == self.Entry(data):  # key already exists, update the value
                self.data[hashvalue].numDocs += 1
                self.data[hashvalue].files.append(data)

            else:
                nextslot=self.rehash(hashvalue) # index collision, using linear probing to find the location
                if self.data[hashvalue] == None:
                    #self.slots[nextslot] = key
                    self.data[nextslot] = self.Entry(data)
                    self.uniqueTokens += 1

                elif self.data[hashvalue] == self.Entry(data):
                    self.data[nextslot].numDocs += 1
                    self.data[nextslot].files.append(data)

                else:
                    while self.data[hashvalue] != None and self.data[hashvalue] != self.Entry(data):
                        nextslot=self.rehash(nextslot)
                        if self.data[hashvalue] == None:
                            #self.slots[nextslot] = key
                            self.data[nextslot] = self.Entry(data)
                            self.uniqueTokens += 1

                        elif self.data[hashvalue] == self.Entry(data):
                            self.data[nextslot].numDocs += 1
                            self.data[nextslot].files.append(data)



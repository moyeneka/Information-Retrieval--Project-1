# Created by Ang Li
# October 2, 2016
# Modified by Marion Chiariglione
# September 22, 2018
import hashlib
import linkedlist

class HashTable:
    def __init__(self, table_size):
        self.size=table_size # size of hash table
        self.term=[None]*self.size # initialize keys
        self.num_docs=[None]*self.size # initialize values
        self.list=[None]*self.size
        self.llist = linkedlist.LinkedList()
        
    def hashfunction(self,key): # hash function to find the location
        h = hashlib.sha1() # any other algorithm found in hashlib.algorithms_guaranteed can be used here
        h.update(bytes(key, encoding="ascii"))
        return int(h.hexdigest(), 16)%self.size

    def rehash(self, oldhash): # called when index collision happens, using linear probing
        return (oldhash+3)%self.size

    def insert(self, term, document, freq): # insert k,v to the hash table
        hashvalue = self.hashfunction(term)  # location to insert
        
        if self.term[hashvalue] == None:
            self.term[hashvalue] = term
            self.num_docs[hashvalue] = 1
            self.llist.AddToEnd(term, document, freq)
            
        else:
            if self.term[hashvalue] == term:  # key already exists, update the value
                self.num_docs[hashvalue] += 1
                self.llist.AddToEnd(term, document, freq)

            else:
                nextslot=self.rehash(hashvalue) # index collision, using linear probing to find the location
                if self.term[nextslot] == None:
                    self.term[nextslot] = term
                    self.num_docs[nextslot] = 1
                    self.llist.AddToEnd(term, document, freq)
                elif self.term[nextslot] == term:
                    self.num_docs[nextslot] += 1
                    self.llist.AddToEnd(term, document, freq)
                else:
                    while self.term[nextslot] != None and self.term[nextslot] != term:
                        nextslot=self.rehash(nextslot)
                        if self.term[nextslot] == None:
                            self.term[nextslot] = term
                            self.num_docs[nextslot] = 1
                            self.llist.AddToEnd(term, document, freq)

                        elif self.term[nextslot] == term:
                            self.num_docs[nextslot] += 1
                            self.llist.AddToEnd(term, document, freq)

        self.list[hashvalue] = self.llist.GetTermList(term)

    def get(self, key):  # get the value by looking for the key
        startslot = self.hashfunction(key)
        num_docs = None
        stop = False
        found = False
        position = startslot
        while self.term[position] != None and not found and not stop:
            if self.term[position] == key:
                found = True
                num_docs = self.num_docs[position]
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        return num_docs

    def intable(self, key):  # determine whether a key is in the hash table or not
        startslot = self.hashfunction(key)
        stop = False
        found = False
        position = startslot
        while self.term[position] != None and not found and not stop:
            if self.term[position] == key:
                found = True
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        return found

    def getCount(self):
        return self.utokens, self.ttokens

    def print(self):
        for i in range(0, self.size, 1):
            if self.term[i] != None:
                print(str(self.term[i]) + " " + str(self.num_docs[i]) + " " +str(self.list[i]))

    def writeToFile(self, filename1, filename2):
        dict = open(filename1, 'w')
        post = open(filename2, 'w')
        start = 0



        for i in range(0, self.size, 1):
            if self.term[i] != None:
                dict.write(str(self.term[i]) + " " + str(self.num_docs[i]) + " " + str(start) + "\n")
                post.write(str(self.list[i][0][0]) + " " + str(self.list[i][0][1]) + "\n")
                start = start + self.num_docs[i]
        dict.close()
        post.close()
        

                

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, num_docs):
        self.insert(key,num_docs)

    def __len__(self):
        return self.size


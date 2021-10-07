import sys
import glob
import os.path
import re
import ghashtable
import linkedlist
import hashtable

size1 = 5
size2 = 10
document_ht = hashtable.HashTable(size1)
global_ht = ghashtable.HashTable(size2)
print()
doc_id = 0
document_ht.insert("dog1")
document_ht.insert("dog")
document_ht.insert("cat")
document_ht.print()


print("Document hashtable should have been filled.\n")
print("Time to deal with its contents.\n")
for i in range(0, document_ht.size, 1):
    value, data = document_ht.gettable(i)
    if value != None:
        global_ht.insert(value, doc_id, data)
document_ht.__init__(size1)
doc_id += 1

document_ht.insert("dog1")
document_ht.insert("dog")
document_ht.insert("cat")
document_ht.insert("fish")

for i in range(0, document_ht.size, 1):
    value, data = document_ht.gettable(i)
    if value != None:
        global_ht.insert(value, doc_id, data)
document_ht.__init__(size1)

global_ht.print()



# document_ht.__init__(table_size)
# document_ht.insert("dog")
# document_ht.print()

# L = linkedlist.LinkedList()
# L.AddToEnd("test", 0, 1)
# L.AddToEnd("test2", 1, 1)
# L.AddToEnd("test", 2, 2)
# L.AddToEnd("test2", 3, 4)
# L.GetTermList("test")
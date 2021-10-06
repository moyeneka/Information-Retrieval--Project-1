import sys
import glob
import os.path
import re
import ghashtable
import linkedlist

table_size = 6
document_ht = ghashtable.HashTable(table_size)
document_ht.insert("dog1", 0, 1)

document_ht.insert("dog1", 2, 2)

document_ht.insert("cat", 1, 1)
document_ht.print()


# document_ht.print()

# document_ht.__init__(table_size)
# document_ht.insert("dog")
# document_ht.print()

# L = linkedlist.LinkedList()
# L.AddToFront(0, 1)
# L.AddToFront(1, 1)
# L.AddToEnd(2, 2)
# L.AddToEnd(3, 4)
# L.Print()
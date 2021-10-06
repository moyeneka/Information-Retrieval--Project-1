# ----------------------------------------------------------------*/
# Filename:  multiplefiles.py                                    
# Takes in and out directories: python3 multiplefiles.py <indir> <outdir> 
# ----------------------------------------------------------------*/

import ply
from ply import lex
from ply.lex import TOKEN
import sys
import glob
import os.path
import hashtable

# Document Hash Table
doc_size = 6848
document_ht = hashtable.HashTable(doc_size)

# list of TOKENS
tokens =[
    'TAG',
    'TEXT_TAG',
    'FLOAT',
    'TIME',
    'COMMA_NUMBER',
    'HYPENATED',
    'ABBREVIATED',
    'WORD',
    'WHITESPACE',
    'PUNCTUATION',
]

#---------  INSERT ANY CODE CALLED BY THE LEX RULES HERE --------

#  Section of code which specifies lex substitution patterns
DIGITS  = r'[0-9]+'
UPPERCASE = r'[A-Z]'

# tokens DEFINITION - Section which specifies regular expressions and action
+#rule for html tags
def t_TAG(t):
    r'\s*<[^>]*>\s*'
    pass

#When a HTML tag is in the middle of a word, such as a <b> tag
def t_TEXT_TAG(t):
    r'(\w+<[^>]*>\w+)+'
    t.value = re.sub("<[^>]*>", "", t.value)
    t.value = str(t.value).lower()
    return t

#for hypenated words
def t_HYPENATED(t):
    r"(\w+-\w+)(-\w+)*"
    t.value = re.sub("-*", "", t.value)
    t.value = str(t.value).lower()
    return t

#rule for floats, we ignore everything in the decimal place
def t_FLOAT(t):
    r"[-+]?\d*\.\d+"
    t.value = str(abs(int(float(t.value))))
    return t

#numbers which have commas in them, we just remove the comma
def t_COMMA_NUMBER(t):
    r"(\d*,\d+)+"
    t.value = re.sub(",", "", t.value)
    return t

#numbers that have a colon in them
def t_TIME(t):
    r"\w+:\w+"
    t.value = re.sub(":", "", t.value)
    return t

#This rule catches abbreviations as well as websites urls
def t_ABBREVIATED(t):
    r"(\w+\.\w+)(\.\w+)*"
    t.value = re.sub("\.", "", t.value)
    t.value = str(t.value).lower()
    return t

#Every string of alphanumeric characters that does not have a rule yet
def t_WORD(t):
    r'\w+'
    t.value = str(t.value).lower()
    return t

def t_PUNCTUATION(t):
    r'[!"#$%&\'\(\)\*\+,-./:;<=>?@\[\]^_`{|}~\\/]'
    pass

def t_WHITESPACE(t):
    r'\s+'
    pass

def t_error(t):
    # print("Illegal characters: ", t.value)
    t.lexer.skip(1)

def processDocumentHashtable():
   print("Document hashtable should have been filled.\n")
   print("Time to deal with its contents.\n")
   document_ht.print()
   document_ht.__init__(doc_size)

# Processing with multiple files 
inputDir = sys.argv[1]
outputDir = sys.argv[2]
if not os.path.exists(inputDir) or not os.path.exists(outputDir):
    print("Path not valid \n Enter valid path ")
    quit()

list_of_files = glob.glob(inputDir + '/*.html')
lexer = lex.lex()
# num_tokens is used to show that it shares the same memory when running lex
# which can be applied for your hash table
lexer.num_tokens = 0

# loop through all files in input directory
for file_name in list_of_files:
    myFile = open(file_name)
    lines = myFile.read()
    f=open(os.path.join(outputDir,
    os.path.basename(file_name + ".txt")) , 'w')
    try:
        lexer.input(lines)
        for token in lexer:
            document_ht.insert(str(token))
            lexer.num_tokens += 1            
    except EOFError:
        break
    
    print("Process file: ", file_name)
    f.close()

    processDocumentHashtable()

print("Total tokens: ", lexer.num_tokens)

print("Done tokenizing.  Good place to write the dict and post files.")
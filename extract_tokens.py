#----------------------------------------
# Filename:  extract_tokens.py
# To run:    python3 extract_tokens.py <infile>  
# e.g:       python3 extract_tokens.py input.txt > output.txt
#----------------------------------------

import ply
from ply import lex
from ply.lex import TOKEN
import sys
# list of TOKENS
tokens =[
    'whitespace',
    'him',
    'he',
    'his',
    'susan',
    'lowercase',
    'digit',
    'other'
]

#  Section of code which specifies lex substitution patterns
DIGITS  = r'[0-9]+'
UPPERCASE = r'[A-Z]'

# tokens DEFINITION - Section which specifies regular expressions and action
def t_whitespace(t):
    r'\n\t\s+'
    pass

def t_him(t):
    r'[hH]im'
    t.value = "her"
    return t

def t_he(t):
    r'[hH]e'
    t.value = "she"
    return t

def t_his(t):
    r'[hH]is'
    t.value = "her"
    return t

def t_susan(t):
    r'Susan'
    t.value = t.value[0]
    return t

def t_other(t):
    r'[a-z]+'
    return t

# In some applications, you may want to define tokens as a series of more complex regular expression rules.
@TOKEN(DIGITS)
def t_digit(t):    
    t.value = "NUMBER"
    return t

@TOKEN(UPPERCASE)
def t_lowercase(t):
    t.value = t.value[0].lower()
    return t

def t_error(t):
    # print("Illegal characters: ", t.value)
    t.lexer.skip(1)

# reading INPUT FILE

myFile = open(sys.argv[1])
result = ""
lexer = lex.lex()

with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)
            for token in lexer:
                result += token.value
        except EOFError:
            break
print(result)

# ----------------------------------------*/
# Given the following input file:         */
# He ran his car fast.                    */
# Susan 12345  ABC D.                     */
#                                         */
# Produces the following output:          */
# sheranhercarfast.SNUMBERabcd.           */
# ----------------------------------------*/

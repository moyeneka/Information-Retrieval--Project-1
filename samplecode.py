#----------------------------------------
# Filename:  identifier.py
# To run:    python3 identifier.py <infile>  
#----------------------------------------
import ply
from ply import lex
import sys

# list of TOKENS
tokens =[
    'id'
]

#  Section of code which specifies lex substitution patterns
DIGIT  = r'[0-9]'
LETTER = r'[A-Za-z]'

# tokens DEFINITION - Section which specifies regular expressions
t_id = r''+LETTER+'('+LETTER+'|'+ DIGIT+')*'

def t_error(t):
    # print("Illegal characters: ", t.value)
    t.lexer.skip(1)

# reading INPUT FILE

myFile = open(sys.argv[1])

lexer = lex.lex()

with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)

            for token in lexer:
                print("Identifier: ", token.value)
                
        except EOFError:
            break
# ----------------------------------------
#  Given the following input file:
#     1234 X Students 5Day Day5
#  Produces the following output:
#     Identifier: X
#     Identifier: Students
#     Identifier: Day
#     Identifier: Day5
# ----------------------------------------
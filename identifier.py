#----------------------------------------
# Filename:  identifier.py
# To run:    python3 identifier.py <infile>  
# e.g.:    python3 identifier.py simple.html output2.txt
#----------------------------------------
import ply
from ply import lex
from ply.lex import TOKEN
import sys

# list of TOKENS
tokens =[
    'id',
    'lowercase'
]

#  Section of code which specifies lex substitution patterns
DIGIT  = r'[0-9]'
LETTER = r'[A-Za-z]'

# tokens DEFINITION - Section which specifies regular expressions
t_id = r''+LETTER+'('+LETTER+'|'+ DIGIT+')*'

@TOKEN(t_id)
def t_lowercase(t):
    t.value = t.value.lower()
    return t

def t_error(t):
    # print("Illegal characters: ", t.value)
    t.lexer.skip(1)

# reading INPUT FILE
#Check for correct amount of arguments passed
if (len(sys.argv) != 3):
    sys.stderr.write("Argument count is incorrect.\n")
else:
    #Read file names from arguments
    InFile = str(sys.argv[1])
    OutFile = str(sys.argv[2])
    #myFile = open(sys.argv[1])

    lexer = lex.lex()

    with open(InFile, "r") as InputFile:
        print("Reading " + InFile)
        with open(OutFile, "w") as OutputFile:
            print("Writing to " + OutFile)
            for line in InputFile:
                try:
                    lexer.input(line)
                    for token in lexer:
                        OutputFile.write("Words: " + token.value + " :\n")
                    
                except EOFError:
                    break
    InputFile.close()
    OutputFile.close() 
# ----------------------------------------
#  Given the following input file:
#     1234 X Students 5Day Day5
#  Produces the following output:
#     Identifier: X
#     Identifier: Students
#     Identifier: Day
#     Identifier: Day5
# ----------------------------------------

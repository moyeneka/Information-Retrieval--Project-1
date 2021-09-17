#----------------------------------------
# Filename:  identifier.py
# To run:    python3 identifier.py <infile>  
# e.g.:    python3 identifier.py simple.html output2.txt
#----------------------------------------
import ply
from ply import lex
from ply.lex import TOKEN
import sys
import os

# list of TOKENS
tokens =[
    
    'lowercase',
    'html',
    'nonhtml'
    
]
#Another way to do 
#  Section of code which specifies lex substitution patterns
#DIGIT  = r'[0-9]'
#LETTER = r'[A-Za-z]'
# tokens DEFINITION - Section which specifies regular expressions
#t_id = r''+LETTER+'('+LETTER+'|'+ DIGIT+')*'

def t_html(t):
    r'(?:</?\w+>)|(?:<.+/?>)'
    pass


def t_nonhtml(t):
    r'(?:\d+.?\d+.?\d+)|\w+'
    return t


@TOKEN(t_nonhtml)
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
    fileName = os.path.basename(InFile)
    OutFile = str(sys.argv[2]+ fileName + ".txt")

    
    lexer = lex.lex()

    with open(InFile, "r") as InputFile:
        print("Reading " + InFile)
        with open(OutFile, "w") as OutputFile:
            print("Writing to " + OutFile)
            
            #reading inputs
            for line in InputFile:
                try:
                    #lexer stores all the tokens into lex and performs the arguments
                    lexer.input(line)
                    for token in lexer:
                        OutputFile.write("Words: " + token.value + " :\n")
                    
                except EOFError:
                    break
    
    InputFile.close()
    OutputFile.close() 
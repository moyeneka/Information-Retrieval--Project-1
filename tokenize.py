#Tokenizer Code

import ply
from ply import lex
import sys
# list of TOKENS
tokens =[
    'doc',
    
]
#  Section of code which specifies lex substitution patterns
DIGIT  = r'[0-9]'
#UPPERCASE = r'[A-Za-z]'
LETTER = r'[A-Z]'

# tokens DEFINITION - Section which specifies regular expressions
t_doc = r''+LETTER+'('+LETTER+'|'+ DIGIT+')*'

# Regular expression rules for our tokens

def t_error(t):
    # print("Illegal characters: ", t.value)
    t.lexer.skip(1)
#Check for correct amount of arguments passed
if (len(sys.argv) != 3):
    sys.stderr.write("Argument count is incorrect.\n")
else:
    #Read file names from arguments
    InFile = str(sys.argv[1])
    OutFile = str(sys.argv[2])
    
    lexer = lex.lex()
    #Open the files
    with open(InFile, "r") as InputFile:
        print("Reading " + InFile)
        with open(OutFile, "w") as OutputFile:
            print("Writing to " + OutFile)
            #Read line and split using blank space
            for line in InputFile:
                try:
                    lexer.input(line)
                    for token in lexer:
                        OutputFile.write("Words: " + token + " :\n")
                except EOFError:
                    break
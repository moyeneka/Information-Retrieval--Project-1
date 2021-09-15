import nltk
nltk.download('punkt')
import sys

InFile = str(sys.argv[1])
OutFile = str(sys.argv[2])
new_corpus = []

with open(InFile, "r") as InputFile:
    print("Reading: " + InFile)
    with open(OutFile, "w") as OutputFile:
        print("Writing to " + OutFile)
        for line in InputFile:
            try:
                corpus = str(line.strip())
                new_corpus += nltk.tokenize.word_tokenize(corpus)
            
            except EOFError:
                break
        for x in new_corpus:
            OutputFile.write(x + "\n")
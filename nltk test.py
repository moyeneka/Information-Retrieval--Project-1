import nltk
import sys
import os

InFile = str(sys.argv[1])
fileName = os.path.basename(InFile)
OutFile = str(sys.argv[2]+ fileName + ".txt")
html_tokenizer = nltk.RegexpTokenizer(r"(?:</?\w+>)|(?:<.+/?>)|_+", gaps=True)
non_html_tokenizer=nltk.RegexpTokenizer(r"(?:\d+.?\d+.?\d+)|\w+")
new_corpus = []

with open(InFile, "r") as InputFile:
    print("Reading: " + InFile)
    with open(OutFile, "w") as OutputFile:
        print("Writing to " + OutFile)
        for line in InputFile:
            try:
                corpus = str(line.strip())
                new_corpus += html_tokenizer.tokenize(corpus)
            
            except EOFError:
                break

        for x in new_corpus:
            clean_corpus = []
            clean_corpus += non_html_tokenizer.tokenize(x)
            for y in clean_corpus:
                OutputFile.write(y.lower() + "\n")
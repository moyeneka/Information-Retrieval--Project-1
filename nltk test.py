import nltk
import sys

InFile = str(sys.argv[1])
OutFile = str(sys.argv[2])
html_tokenizer = nltk.RegexpTokenizer(r"(?:</?\w+>)|(?:<.+/?>)", gaps=True)
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
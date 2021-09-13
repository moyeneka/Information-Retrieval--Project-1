#Tokenizer Code
import sys

#Check for correct amount of arguments passed
if (len(sys.argv) != 3):
    sys.stderr.write("Argument count is incorrect.\n")
else:
    #Read file names from arguments
    InFile = str(sys.argv[1])
    OutFile = str(sys.argv[2])

    #Open the files
    with open(InFile, "r") as InputFile:
        print("Reading " + InFile)
        with open(OutFile, "w") as OutputFile:
            print("Writing to " + OutFile)
            #Read line and split using blank space
            for line in InputFile:
                for token in line.split():
                    OutputFile.write(":" + token + ":\n")
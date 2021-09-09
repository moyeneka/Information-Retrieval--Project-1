import sys

if (len(sys.argv) != 3):
    sys.stderr.write("Argument count is incorrect.\n")
else:
    InFile = str(sys.argv[1])
    OutFile = str(sys.argv[2])

    with open(InFile, "r") as InputFile:
        print("Reading " + InFile)
        with open(OutFile, "w") as OutputFile:
            print("Writing to " + OutFile)
            for line in InputFile:
                for token in line.split():
                    OutputFile.write(":" + token + ":\n")
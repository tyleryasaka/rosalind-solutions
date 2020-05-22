datasetFile = open("datasets/rosalind_ba1c.txt", "r")
dnaString = datasetFile.readline().strip()

def reverseComplement(dnaString):
    complementMap = { "A": "T", "T": "A", "C": "G", "G": "C" }
    reverseComplementString = ""
    for i in range(len(dnaString) -1, -1, -1):
        reverseComplementString += complementMap[dnaString[i]]
    return reverseComplementString

outputFile = open("output/rosalind_ba1c.txt", "a")
outputFile.write(reverseComplement(dnaString))

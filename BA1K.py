datasetFile = open("datasets/rosalind_ba1k.txt", "r")
text = datasetFile.readline().strip()
k = int(datasetFile.readline().strip())

print("Generate the Frequency Array of a String")

def getKmerIndex(kmer):
    alphabet = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
    index = 0
    for i, base in enumerate(kmer):
        index += (4**(len(kmer) - i - 1) * alphabet[base])
    return index

def generateFreqArray(text, k):
    arr = [0] * 4**k
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmerIndex = getKmerIndex(kmer)
        arr[kmerIndex] += 1
    return arr

freqArr = generateFreqArray(text, k)
solution = " ".join(map(lambda x: str(x), freqArr))

outputFile = open("output/rosalind_ba1k.txt", "w")
outputFile.write(solution)

datasetFile = open("datasets/rosalind_ba2c.txt", "r")
text = datasetFile.readline().strip()
k = int(datasetFile.readline().strip())
profile = []
for str in datasetFile:
    profile.append(map(lambda x: float(x), str.strip().split(" ")))

print("Find a Profile-most Probable k-mer in a String")

def kmerProbability (kmer, profile):
    probabilities = []
    baseToRow = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
    for i in range(len(kmer)):
        row = baseToRow[kmer[i]]
        col = i
        probabilities.append(profile[row][i])
    product = 1
    for j in range(len(probabilities)):
        product = product * probabilities[j]
    return product

def mostProbableKmer (text, k, profile):
    mostProbable = None
    maxProbability = None
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        probability = kmerProbability(kmer, profile)
        if (maxProbability is None) or (probability > maxProbability):
            maxProbability = probability
            mostProbable = kmer
    return mostProbable

solution = mostProbableKmer(text, k, profile)

outputFile = open("output/rosalind_ba2c.txt", "w")
outputFile.write(solution)

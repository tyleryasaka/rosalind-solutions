from BA1G import hammingDistance
from BA1M import numberToPattern

datasetFile = open("datasets/rosalind_ba2b.txt", "r")
k = int(datasetFile.readline().strip())
dna = []
for str in datasetFile:
    dna.append(str.strip())

print("Find a Median String")

def medianString (dna, k):
    alphabet = ['A', 'C', 'G', 'T']
    minDistance = None
    median = None
    for i in range(4**k):
        pattern = numberToPattern(i, k)
        distance = 0
        for dna_str in dna:
            minDistanceInString = None
            for j in range(len(dna_str) - k + 1):
                kmer = dna_str[j:j+k]
                currentDistance = hammingDistance(kmer, pattern)
                if (minDistanceInString is None) or (currentDistance < minDistanceInString):
                    minDistanceInString = currentDistance
            distance += minDistanceInString
        if (minDistance is None) or (distance < minDistance):
            minDistance = distance
            median = pattern
    return median

solution = medianString(dna, k)

outputFile = open("output/rosalind_ba2b.txt", "w")
outputFile.write(solution)

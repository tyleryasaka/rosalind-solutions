from BA1N import getNeighbors
from BA1G import hammingDistance

datasetFile = open("datasets/rosalind_ba2a.txt", "r")
k, d = map(lambda x: int(x), datasetFile.readline().strip().split(" "))
dna = []
for str in datasetFile:
    dna.append(str.strip())

print("Implement MotifEnumeration")

def motifEnumeration (dna, k, d):
    patterns = set()
    for dna_index, dna_str in enumerate(dna):
        if dna_index == 0:
            for i in range(len(dna_str) - k + 1):
                kmer = dna_str[i:i+k]
                neighbors = getNeighbors(kmer, d)
                for neighbor in neighbors:
                    patterns.add(neighbor)
        else:
            new_patterns = set()
            for i in range(len(dna_str) - k + 1):
                kmer = dna_str[i:i+k]
                for pattern in patterns:
                    if hammingDistance(kmer, pattern) <= d:
                        new_patterns.add(pattern)
            patterns = new_patterns
    return patterns

motifs = motifEnumeration(dna, k, d)
solution = " ".join(motifs)

outputFile = open("output/rosalind_ba2a.txt", "w")
outputFile.write(solution)

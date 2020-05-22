datasetFile = open("datasets/rosalind_ba1e.txt", "r")
genome = datasetFile.readline().strip()
otherArgs = datasetFile.readline().strip()
k, L, t = map(lambda x: int(x), otherArgs.split(" "))

def findClumps(genome, k, L, t):
    kmerIndex = {}
    clumpedKmers = set()
    for i in range(len(genome) - k + 1):
        kmer = genome[i:i+k]
        if kmer in kmerIndex:
            currentIndex = kmerIndex[kmer]
            currentIndex.append(i)
            if len(currentIndex) >= t:
                clumpStart = currentIndex[-t]
                if i - clumpStart <= L:
                    clumpedKmers.add(kmer)
        else:
            kmerIndex[kmer] = [i]
    return clumpedKmers

solution = " ".join(findClumps(genome, k, L, t))

outputFile = open("output/rosalind_ba1e.txt", "a")
outputFile.write(solution)

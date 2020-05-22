datasetFile = open("datasets/rosalind_ba1d.txt", "r")
pattern = datasetFile.readline().strip()
genome = datasetFile.readline().strip()

def findInText(pattern, genome):
    indices = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i+len(pattern)] == pattern:
            indices.append(i)
    return indices

solution = " ".join(map(lambda x: str(x), findInText(pattern, genome)))

outputFile = open("output/rosalind_ba1d.txt", "a")
outputFile.write(solution)

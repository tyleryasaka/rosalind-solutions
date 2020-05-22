datasetFile = open("datasets/rosalind_ba1f.txt", "r")
genome = datasetFile.readline().strip()

print("Find a Position in a Genome Minimizing the Skew")

def minSkew(genome):
    indices = [0]
    skew = 0
    min = 0
    for i in range(len(genome)):
        if genome[i] == 'G':
            skew += 1
        elif genome[i] == 'C':
            skew -= 1
        if skew < min:
            indices = [i + 1]
            min = skew
        elif skew == min:
            indices.append(i + 1)
    return indices

solution = " ".join(map(lambda x: str(x), minSkew(genome)))

outputFile = open("output/rosalind_ba1f.txt", "a")
outputFile.write(solution)

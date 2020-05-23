datasetFile = open("datasets/rosalind_ba1n.txt", "r")
pattern = datasetFile.readline().strip()
d = int(datasetFile.readline().strip())

print("Generate the d-Neighborhood of a String")

neighborsCache = {}

def getCache(pattern, d):
    if pattern in neighborsCache:
        forPattern = neighborsCache[pattern]
        if not forPattern is None:
            if str(d) in forPattern:
                return forPattern[str(d)]
    return None

def setCache(pattern, d, val):
    forPattern = {}
    if pattern in neighborsCache:
        forPattern = neighborsCache[pattern]
    forPattern[str(d)] = val
    neighborsCache[pattern] = forPattern

def getNeighbors(pattern, d):
    cached = getCache(pattern, d)
    if cached is not None:
        return cached
    neighbors = set([pattern])
    if (d == 0) or len(pattern) == 0:
        return neighbors
    alphabet = 'ATCG'
    for base in alphabet:
        if not (pattern[0] == base):
            suffixes = getNeighbors(pattern[1:], d - 1)
        else:
            suffixes = getNeighbors(pattern[1:], d)
        for suffix in suffixes:
            neighbors.add(base + suffix)
    setCache(pattern, d, neighbors)
    return neighbors

neighborhood = getNeighbors(pattern, d)
solution = "\n".join(neighborhood)

outputFile = open("output/rosalind_ba1n.txt", "w")
outputFile.write(solution)

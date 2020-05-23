from itertools import product
from BA1A import patternCount

datasetFile = open("datasets/rosalind_ba1i.txt", "r")
text = datasetFile.readline().strip()
k, d = map(lambda x: int(x), datasetFile.readline().strip().split(" "))

print("Find the Most Frequent Words with Mismatches in a String")

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

def frequentWordsWithMismatches(text, k, d):
    counts = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        neighborhood = getNeighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor in counts:
                counts[neighbor] += 1
            else:
                counts[neighbor] = 0
    frequentPatterns = set()
    maxCount = None
    for pattern in counts:
        count = counts[pattern]
        if maxCount is None or count > maxCount:
            frequentPatterns = set([pattern])
            maxCount = count
        elif count == maxCount:
            frequentPatterns.add(pattern)
    return frequentPatterns, maxCount

frequentPatterns, maxCount = frequentWordsWithMismatches(text, k, d)
solution = " ".join(frequentPatterns)

outputFile = open("output/rosalind_ba1i.txt", "w")
outputFile.write(solution)

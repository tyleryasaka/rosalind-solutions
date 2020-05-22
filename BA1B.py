from BA1A import patternCount

datasetFile = open("datasets/rosalind_ba1b.txt", "r")
text = datasetFile.readline().strip()
k = int(datasetFile.readline().strip())

print("Find the Most Frequent Words in a String\n")

def frequentWords(text, k):
    frequentPatterns = set()
    maxCount = None
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        count = patternCount(text, pattern)
        if maxCount is None or count > maxCount:
            frequentPatterns = set([pattern])
            maxCount = count
        elif count == maxCount:
            frequentPatterns.add(pattern)
    return frequentPatterns, maxCount

frequentPatterns, maxCount = frequentWords(text, k)

print(" ".join(frequentPatterns))

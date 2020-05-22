from BA1G import hammingDistance

datasetFile = open("datasets/rosalind_ba1h.txt", "r")
pattern = datasetFile.readline().strip()
text = datasetFile.readline().strip()
d = int(datasetFile.readline().strip())

print("Find All Approximate Occurrences of a Pattern in a String")

def approximateMatch(pattern, text, d):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        distance = hammingDistance(pattern, text[i:i+len(pattern)])
        if distance <= d:
            occurrences.append(i)  # all chars (except up to 2) matched; record
    return occurrences

solution = " ".join(map(lambda x: str(x), approximateMatch(pattern, text, d)))

outputFile = open("output/rosalind_ba1h.txt", "w")
outputFile.write(solution)

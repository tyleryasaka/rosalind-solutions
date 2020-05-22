datasetFile = open("datasets/rosalind_ba1a.txt", "r")
text = datasetFile.readline().strip()
pattern = datasetFile.readline().strip()

print("Compute the Number of Times a Pattern Appears in a Text\n")

def patternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(patternCount(text, pattern))

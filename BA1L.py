datasetFile = open("datasets/rosalind_ba1l.txt", "r")
pattern = datasetFile.readline().strip()

print("Implement PatternToNumber")

def patternToNumber(pattern):
    alphabet = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
    num = 0
    for i, base in enumerate(pattern):
        num += (4**(len(pattern) - i - 1) * alphabet[base])
    return num

solution = str(patternToNumber(pattern))

outputFile = open("output/rosalind_ba1l.txt", "w")
outputFile.write(solution)

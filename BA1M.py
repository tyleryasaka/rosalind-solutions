datasetFile = open("datasets/rosalind_ba1m.txt", "r")
num = int(datasetFile.readline().strip())
k = int(datasetFile.readline().strip())

print("Implement NumberToPattern")

def numberToPattern(num, k):
    alphabet = "ACGT"
    pattern = ""
    for i in range(k):
        offset = num % 4
        pattern = alphabet[offset] + pattern
        num = (num - offset) / 4
    return pattern

solution = numberToPattern(num, k)

outputFile = open("output/rosalind_ba1m.txt", "w")
outputFile.write(solution)

datasetFile = open("datasets/rosalind_ba1g.txt", "r")
a = datasetFile.readline().strip()
b = datasetFile.readline().strip()

print("Compute the Hamming Distance Between Two Strings")

def hammingDistance(a, b):
    distance = 0
    for i in range(len(a)):
        if not a[i] == b[i]:
            distance += 1
    return distance

solution = str(hammingDistance(a, b))

outputFile = open("output/rosalind_ba1g.txt", "a")
outputFile.write(solution)

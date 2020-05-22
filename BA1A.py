dataset_file = open("datasets/rosalind_ba1a.txt", "r")
t = dataset_file.readline().strip()
p = dataset_file.readline().strip()

def PatternCount(t, p):
    count = 0
    for i in range(len(t) - len(p) + 1):
        if t[i:i+len(p)] == p:
            count += 1
    return count

print(PatternCount(t, p))

words = ["model", "data", "python", "data", "model", "analysis", "data"]

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

repeated = []
for word, count in frequency.items():
    if count > 1:
        repeated.append(word)

print("Frequency:", frequency)
print("Repeated words:", repeated)
file = open("foo.txt")
numLines = 0
numWords = 0
uniqueWords = set()
for line in file:
	numLines += 1
	words = line.split()
	for word in words:
		numWords += 1
		uniqueWords.add(word)
print(numLines, "lines")
print(numWords, "words")
print(len(uniqueWords), "unique words")

print("File cursor is at", file.tell())
for line in file:
	print(line.strip())
file.seek(0, 0)
print("File cursor is at", file.tell())
for line in file:
	print(line.strip())

file.close()

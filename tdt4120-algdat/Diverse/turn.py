word = [1,2,3,4,5,6,7]
for x in xrange(len(word) / 2):
    word[x], word[-x - 1] = word[-x - 1], word[x]

print word

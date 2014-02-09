text = """Python is a general-purpose, interpreted high-level programming language[11] whose design philosophy emphasizes code readability. Its syntax is said to be clear[12][13] and expressive.[14] Python has a large and comprehensive standard library.[15]

Python supports multiple programming paradigms, primarily but not limited to object-oriented, imperative and, to a lesser extent, functional programming styles. It features a fully dynamic type system and automatic memory management, similar to that of Scheme, Ruby, Perl, and Tcl. Like other dynamic languages, Python is often used as a scripting language, but is also used in a wide range of non-scripting contexts. Using third-party tools, Python code can be packaged into standalone executable programs. Python interpreters are available for many operating systems.

CPython, the reference implementation of Python, is free and open source software and has a community-based development model, as do nearly all of its alternative implementations. CPython is managed by the non-profit Python Software Foundation."""

# Make a word lowercase and remove characters that are not letters
def cleanWord(originalWord):
	word = ""
	for letter in originalWord.lower():
		if letter.isalpha():
			word += letter
	return word

def usesAWordMoreThanOnce(text):
	words = text.split()
	uniqueWords = set()
	for originalWord in words:
		word = cleanWord(originalWord)
		if word in uniqueWords:
			return True
		uniqueWords.add(word)
	return False

# Counts the occurrences of each word
words = text.split()
frequencies = {}
for originalWord in words:
	word = cleanWord(originalWord)
	frequencies[word] = frequencies.get(word, 0) + 1
print(len(frequencies), "unique words")
for word in frequencies:
	print(word, ":", frequencies[word])

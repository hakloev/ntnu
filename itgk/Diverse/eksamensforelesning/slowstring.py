# Not important for ITGK, but nice to know for later: repeated string concatenation is slow when the strings become long.
# This also applies to many other languages, such as Java and C#.
# Watch as the string concatenation becomes slower and slower the longer the string is, while the list appending keeps the same speed.

print("List appending (fast):")
numbers = []
for x in range(100000000):
	if x % 1000000 == 0:
		print(x)
	numbers.append(42)
print(len(numbers))

print("String concatenation (slower and slower):")
text = ""
for x in range(100000000):
	if x % 1000000 == 0:
		print(x)
	text += "a"
print(len(text))

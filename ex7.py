def vigenere(word, key):
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	d = {letters[i] : i for i in range(len(letters))}

	table = [letters[i::] + letters[:i:] for i in range(len(letters))]

	result = ""
	for i in range(len(word)):
		result = result + table[d[word[i]]][d[key[i]]]

	return result


c = vigenere("attackatdawn", "lemonlemonle")
print(c)

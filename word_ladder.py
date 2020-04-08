words = ['log', 'cog', 'hog', 'dig', 'lot', 'hit', 'lit', 'kit', 'jot', 'rot', 'fit', 'lip', 'rim']

start = 'hit'

target = 'cog'


def _distance(c1, c2):
	c = 0
	for w in range(len(c1)):
		if c1[w] != c2[w]:
			c+=1
	return c


def _adjacent(target, words):
	fx = []
	for word in words:
		if _distance(target, word) == 1:
			fx.append(word)
	
	return fx


def find_ladder(start, target, words):
	while True:
		adj = _adjacent(start, words)
		words.remove(start)
		least = {}
		for word in adj:
			least[_distance(word, target)] = word
		m = min(least.keys())
		start = least[m]
		print(words, start)
		if start == target:
			break


find_ladder(start, target, words)

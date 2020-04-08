'''
hangman.py

UTF-8

@author: Noirdemort
'''

import json
import random

def play_for_word(word):
	'''
		Interface for playing game
		Processing Logic
	'''
	l = len(word)

	print(f"\n [+] The length of word is {l}.")
	blank = ['#' for _ in range(l)]
	
	for i in range(l):
		z = input(" Enter letter >> ").strip().lower()
		if not z:
			continue
		# select first letter
		z = z[0]
		replace = [k for k in range(l) if word.startswith(z, k)] # find occurences
		for k in replace:
			blank[k] = z
		print(''.join(blank))
		
		# pigeon-hole principle 
		if ''.join(blank) == word:
			print(" [+] Congrats, you won 1337")
			return

	print("Rounds Over")	
	if blank == word:
		print(" [+] Congrats, you won 1337")
	else:
		print(" [-] LOL, You n00b")


def load_file(path):
	'''
	Loads JSON file containing wordlist
	{ "words": ['',...]}

	:return list(str)
	'''
	if not path:
		path = "words.json"
	with open(path, 'r') as f:
		data = json.load(f)
		word_list = data['words']
	return word_list


print("\t Hangman")

while True:
	print("1. Start [default]")
	print("2. Quit (q)")
	n = input().strip().lower()

	if n == "q":
		exit(0)

	try: 
		word = random.choice(load_file(None))
	except: 
		word = "monogram"
	play_for_word(word)

'''
wayfarer.py

@author: Noirdemort

License: GPL v3

Encoding: UTF-8
'''

import time
import json
import argparse


'''
TODO:

	a. Add multiplayer support
	b. Non Linear story support
	c. Add Scoring support

Use a structured JSON to convert any story into text based adventure

{
	"title": "Story Title",
	"start" : {
		"preface": ["Lines to be printed when here"],
		"question": "The question that should be asked",
		"answers" : {
			"ans1":{
					"preface"...	
				},
			"ans2": {
					...
				},
			"ans3": "quit" // exits the program
		}
	}
}

'''

def _possible_input(question, answers):
	for i in range(len(answers)):
		answers[i] = answers[i].strip().lower()

	print(question)
	n = input(">> ").strip().lower()
	while n not in answers:
		print("------ What are you trying to do/say? I don't understand-----")
		n = input(">> ").strip().lower()
	return n


def storyfarer(storyline):
	title = storyline["title"]
	story = storyline["start"]
	print(f"\n\t\t {title}")
	while True:
		for line in story["preface"]:
			print(line)
			time.sleep(0.3)
		ans = _possible_input(story["question"], story["answers"].keys())
		if story["answers"][ans] == "quit":
			print("Exiting...")
			exit(0)
		story = story["answers"][ans]


if __name__=='__main__':
	parser = argparse.ArgumentParser(prog='WayFarer', description="Text based adventure playground")
	parser.add_argument('--file', '-f', help="JSON File Name", required=True)
	args = parser.parse_args()
	if not os.path.isfile(args.file):
		print("[!] File not found")
		exit(1)
	
	with open(args.file, 'r') as f:
		storyline = json.load(f)
	
	storyfarer(storyline)
	

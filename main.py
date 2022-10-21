from random import choice

with open('./words.txt', 'r') as f:
	answers = f.read().split()

word = choice(answers)

unknown = ["*", "*", "*", "*", "*"]

while ("*" in unknown):
	print(str(unknown)[1:-1].replace(",", "").replace("'", ""))
	guess = list(input("Guess a 5 lettered word\n\n||"))
	print(str(guess)[1:-1].replace(",", "").replace("'", ""))
	for let in range(len(guess)):
		if guess[let] == word[let]:
			print("G", end = " ")
			unknown[let] = guess[let]
			guess[let] = "+"
		elif guess[let] in word:
			if word.count(guess[let]) > 1 or word.index(guess[let]) != let:
				print("Y", end = " ")
		elif not (guess[let] in word):
			print("x", end = " ")
	print()

print("\n\nWord was " + word)

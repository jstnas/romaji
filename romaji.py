import json
import random
import colorama
from colorama import Fore, Back

class Romaji:
	character_file = "characters.json"
	word_file = "words.json"

	def __init__(self):
		colorama.init()
		# Load the characters from a json file.
		with open(self.character_file, 'r', encoding="utf8") as f:
			self.character_dict = json.load(f)
		# Load the words from a json file.
		with open(self.word_file, 'r', encoding="utf8") as f:
			self.word_dict = json.load(f)

	def get_characters(self, characters: [str], mode: int):
		output = ""
		for c in characters:
			output += self.character_dict[c][mode]
		return output

	def get_random_word(self):
		# Choose a random word from the dict.
		random_word = random.choice(list(self.word_dict.keys()))
		character = self.get_characters(self.word_dict[random_word].split(" "), 0)

		return self.get_answer(f"What is the romaji of {character}? ", random_word)

	def get_random_character(self):
		random_mode = random.randrange(0, 1)
		random_character = random.choice(list(self.character_dict.keys()))
		character = self.get_characters([random_character], random_mode)

		return self.get_answer(f"What is the romaji of {character}? ", random_character)

	def get_answer(self, prompt: str, result: str):
		answer = input(prompt).lower()

		if answer == result:
			print(f"{Fore.GREEN}Correct{Fore.RESET}")
			return True
		else:
			print(f"{Fore.RED}Incorrect, the answer was {result}{Fore.RESET}")
			return False

	def random_game(self, words=6):
		correct = 0
		for i in range(words):
			if self.get_random_character():
				correct += 1
		print(f"You got {Fore.GREEN}{correct}{Fore.RESET}/{words} correct")


if __name__ == '__main__':
	romaji = Romaji()
	try:
		romaji.random_game()
	except KeyboardInterrupt:
		print("exiting!")
	except Exception as e:
		print("e")

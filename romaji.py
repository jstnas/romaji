import json
import random


class Romaji:
    character_file = "characters.json"
    word_file = "words.json"

    # 0 for hiragana, 1 for katakana
    mode = 0

    def __init__(self):
        # Load the characters from a json file.
        with open(self.character_file, 'r', encoding="utf8") as f:
            self.character_dict = json.load(f)
        # Load the words from a json file.
        with open(self.word_file, 'r', encoding="utf8") as f:
            self.word_dict = json.load(f)

    def get_kana(self, characters: [str]):
        output = ""
        for c in characters:
            output += self.character_dict[c][self.mode]
        return output

    def random_word(self):
        # Choose a random word from the dict.
        random_word = random.choice(list(self.word_dict.keys()))
        kana = self.get_kana(self.word_dict[random_word].split(" "))
        answer = input(f"What is the romaji of {kana}? ").lower()

        if answer == random_word:
            print("correct")
            return True
        else:
            print("incorrect")
            return False

    def random_game(self, words=6):
        correct = 0
        for i in range(words):
            if self.random_word():
                correct += 1
        print(f"You got {correct}/{words} correct")


if __name__ == '__main__':
    romaji = Romaji()
    romaji.random_game()

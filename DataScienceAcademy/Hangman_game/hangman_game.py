# Hangman Game (Jogo da Forca)
# Object oriented programming
# Data Science Academy - Python fundaments - Lab3

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Buit Method
    def __init__(self, word):
        self.word = word
        self.missed_letters = [] 
        self.guessed_letters = []
		
	# Words guessing Method
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True		
		
	# Is it finished?
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)
		
	# Is there a winner?
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

	# Hide letters Method
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

	# Status reporting and board printing
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\n Word: ' + self.hide_word())
        print('\n Wrong letters: ',)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print('Correct letters: ',)
        for letter in self.guessed_letters:
            print(letter,)
        print()

# Random word selection and reading
def rand_word():
        with open("words.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Main function 
def main():

	# Object
    game = Hangman(rand_word())

	# While the game is not finished, print the status, request a letter and read the character
    while not game.hangman_over():
        game.print_game_status()
        letter_input = str(input('\n Insert one letter: '))
        game.guess(letter_input)

	# Status checking
    game.print_game_status()

	# Priting the results
    if game.hangman_won():
        print('\nCongrats! You won!!')
    else:
        print ('\nGame over! You lose.')
        print ('The word was ' + game.word)
		

# Executa o programa		
if __name__ == "__main__":
	main()

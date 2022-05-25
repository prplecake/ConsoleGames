import random


class RockPaperScissors():

	_options = [
		"rock",
		"paper",
		"scissors"
	]

	def getRandomNumber(self):
		return random.randrange(0, 3, 1)

	def OpponentChoice(self, n):
		return self._options[n]

	def UserChoice(self):
		choice = input("Make a decision (rock, paper, scissors): ").lower()
		print(choice)
		if choice not in self._options:
			print("Invalid input. You lose.")
			exit()
		return choice

	def ScoreGame(self, opponentChoice, userChoice):
		_matrix = {
			"rock": {
				"rock": "tie",
				"paper": "lose",
				"scissors": "win",
			},
			"paper": {
				"rock": "win",
				"paper": "tie",
				"scissors": "lose",
			},
			"scissors": {
				"rock": "lose",
				"paper": "win",
				"scissors": "tie",
			},
		}
		return _matrix[userChoice][opponentChoice]

	def PlayGame(self):
		_userScore = 0
		_opponentScore = 0

		while ((_userScore < 3) and (_opponentScore < 3)):
			_opponentChoice = self.OpponentChoice(self.getRandomNumber())
			_userChoice = self.UserChoice()

			result = self.ScoreGame(_opponentChoice, _userChoice)

			if result == "win":
				print("You win!")
				_userScore += 1
			elif result == "tie":
				print("We tied...")
			elif result == "lose":
				print("You lose!")
				_opponentScore += 1
			print()

		print()
		if (_userScore > _opponentScore):
			print("You won!")
		else:
			print("I won!")

		return

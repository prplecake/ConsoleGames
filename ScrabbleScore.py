class ScrabbleScore():

	letterScore = {
		1: "eaionrtlsu",
		2: "dg",
		3: "bcmp",
		4: "fhvwy",
		5: "k",
		8: "jx",
		10: "qz",
	}

	def GetScore(self, string):
		if (string == ""):
			return 0

		_list = [x.strip('') for x in string.lower()]

		score = 0

		for c in _list:
			for k, v in self.letterScore.items():
				if c in v:
					score += k
		return score

	def Play(self):
		print()
		_input = input("Enter a string: ")
		score = self.GetScore(_input)
		print("Your score: {}".format(score))

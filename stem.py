def porterStemmer(text):
	'''step 1a
		1aa-replace sses by ss
		1ab-delete s if the word root has vowel (not 1st letter before s)
		1ac-replace ied or ies by i if word root has more than one letter
		otherwise replace by ie
		1ad-if suffix is us or ss, do nothing

	'''
	newList = []
	vowel = ['a', 'e', 'i', 'o', 'u']
	for word in text:
		#1aa
		if(word[-4:] == "sses"):
			word = word[:-4]
			word = word + "ss"
		#1ac
		size = len(word)
		if(word[-3:] == "ied" or word[-3:] == "ies"):
			word = word[:-3]
			if(size >= 5):
				word = word + 'i'
			else:
				word = word + 'ie'
		#1ab
		if(word[-1:] == "s" and word[-2:] != "ss" and word[-2:] != "us"):
			test = word[:-2]
			for c in test:
				if c in vowel:
					word = word[:-1]
					break

		'''step 1b
		1ba-replace eed/eedly with ee if its after first non vowel
		following a vowel
		1bb-delete ed/edly/ing/ingly if preceding word part has a vowel
		then
		if word ends in at/bl/iz, add an e
		or if ends with double letter that's not ll/ss/zz, remove last letter
		or if word is short, add e
		'''
		firstNonVowel = False
		previousVowel = False
		replaceEED = False
		if(word[-3:] == "eed" or word[-5:] == "eedly"):
			'''
			for c in word:
				if(firstNonVowel == False and previousVowel == True):
					if c not in vowel:
						firstNonVowel == True
				if c in vowel:
					previousVowel = True
				else:
					previousVowel = False

				if(firstNonVowel == True and previousVowel == True):
					replaceEED = True
					'''
#		if(replaceEED == True):
			if(word[-3:] == "eed"):
				word = word[:-3]
				word = word + "ee"
			if(word[-5:] == "eedly"):
				word = word[:-5]
				word = word + "ee"
		newList.append(word)
	return newList

def main():
	text = ["cheese","stresses", "dresses", "cried", "tied", "curried", "smellies", "dies", "planes", "brfis", "agreed", "feed", "sdjhfeed"]
	newText = porterStemmer(text)
	print("----TEXT----")
	print(*text, sep='\n')
	print("----NEW TEXT----")
	print(*newText, sep='\n')

if __name__ == '__main__':
	main()
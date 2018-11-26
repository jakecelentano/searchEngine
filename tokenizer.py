
import re

def replacer(text):
	#common english abbreviations separated by periods
	text = text.replace("u.s.a.", "usa")
	text = text.replace("a.m.", "am")
	text = text.replace("a.d.", "ad")
	text = text.replace("p.m.", "pm")
	text = text.replace("n.g.", "ng")
	text = text.replace("n.b.g.", "nbg")
	text = text.replace("a.b.c.","abc")
	text = text.replace("b.c.", "bc")
	text = text.replace("o.k.", "ok")
	text = text.replace("p.s.", "ps")
	text = text.replace("i.e.", "ie")

	#punctuation
	text = text.replace("/", " ")
	text = text.replace("(", " ")
	text = text.replace(")", " ")
	text = text.replace(".", " ")
	text = text.replace(",", " ")
	text = text.replace(":", " ")
	text = text.replace(";", " ")
	text = text.replace("\"", " ")
	text = text.replace("_" , " ")
	text = text.replace("-" , " ")
	text = text.replace("'" , " ")
	return text


def tokenize(text):
	text = replacer(text)
	text = re.split(r'\s*', text)
	return text



def stopRemove(splitList):
	#take in text
	file = "stopwords.txt"
	f = open(file, 'r')
	text = f.read().lower()
	f.close()
	#split on new lines
	stopList = text.split("\n")
	#new list of all words not in stop word list
	l3 = [x for x in splitList if x not in stopList]

	return l3


def porterStemmer(text):








def main():
	#get the file input, save to 'text' variable
	file = "tokenization-input-part-A.txt"
	f = open(file, 'r')
	text = f.read().lower()
	f.close()

	#use tokenize function, replace punct and split on space
	splitList = tokenize(text)
	#remove all stop words
	splitstopList = stopRemove(splitList)

	print(*splitstopList, sep='\n')




if __name__ == '__main__':
	main()

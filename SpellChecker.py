from textblob import Textlob

def Convert(string):
	li = list(string.split())
	return li
str1 = input("Enter your text: ")
words=Convert(str1)
corrected_words = []
for i in words:
	corrected_words.append(TextBlob(i))
print("Wrong spellings :", words)
print("Corrected spellings are :")
for i in corrected_words:
	print(i.correct(), end= " ")

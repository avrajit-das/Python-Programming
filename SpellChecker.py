from textblob import TextBlob
def Convert(string):
    li = list(string.split())
    return li
str1= input("Enter your text: ") 
print("Example: I am good boy or girl")
words=Convert(str1)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Worng spelling: ", words)
print("Corrected spelling are: ")
for i in corrected_words:
    print(i.correct(), end=" ")
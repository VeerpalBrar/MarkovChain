from textblob import TextBlob
import numpy


with open('alice.txt', 'r') as content_file:
    content = content_file.read().replace('\n', '')

print(type(content))
blob = TextBlob(content);
allWords = blob.words

uniqueWords = []

for word in allWords:
    if word not in uniqueWords:
        uniqueWords.append(word)

length = len(uniqueWords)
transition = numpy.zeros(shape=(length,length));

for i in range(1, len(allWords)):
    row = uniqueWords.index(allWords[i-1])
    column = uniqueWords.index(allWords[i])
    transition[row, column] +=1;

#divide element by row sum
with numpy.errstate(divide='ignore',invalid='ignore'):
    transition = transition/transition.sum(axis=1, keepdims=True)



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

length = len(unique_words)
transition = numpy.zeros(shape=(length,length));

for i in range(0, length):
    for j in range(0, len(allWords)-1):
       if allWords[j] == uniqueWords[i]:
           index = uniqueWords.index(allWords[j+1])
           transition[i, index] +=1;

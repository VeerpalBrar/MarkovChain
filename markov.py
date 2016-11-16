from textblob import TextBlob
import numpy


with open('alice.txt', 'r') as content_file:
    content = content_file.read().replace('\n', '')

print(type(content))
blob = TextBlob(content);
w = blob.words

unique_words = []

for word in w:
    if word not in unique_words:
        unique_words.append(word)

n = len(unique_words)
transition = numpy.zeros(shape=(n,n));

for i in range(1, n+1):
    index = 0;
    while(index != -1):
        pos = w.index(unique_words[i-1])
        j = w.index(unique_words[i+1])
        transition[i-1, j] +=1;
print(transition)



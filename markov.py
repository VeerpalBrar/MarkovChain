from textblob import TextBlob
import numpy

order = 3  # the length of n-grams. Must be integer >= 0
sentenceLength = 50  # how many words the generated output should be

with open('alice.txt', 'r') as content_file:
    content = content_file.read().replace('\n', ' ')

blob = TextBlob(content);
allWords = blob.words

uniqueWords = []
for word in allWords:
    if word not in uniqueWords:
        uniqueWords.append(word)

gramWords = blob.ngrams(n=order);

rowLength = len(gramWords)
colLength = len(uniqueWords)
transition = numpy.zeros(shape=(rowLength,colLength));

for i in range(order, len(allWords)):
    row = gramWords.index(allWords[i-order:i])
    column = uniqueWords.index(allWords[i])
    transition[row, column] +=1;


# divide element by row sum
with numpy.errstate(divide='ignore',invalid='ignore'):
    transition /= transition.sum(axis=1, keepdims=True)

# begin text generation
markov = []
current = numpy.random.randint(0, len(gramWords))
markov.extend(gramWords[current])
for i in range(sentenceLength):
    rand = numpy.random.random(1)[0]
    sum = 0;
    for next in range(0, colLength):
        sum += transition[current][next]
        if sum > rand :
            break;
    if(next >= colLength):
        break 

    gram = [gramWords[current][1], gramWords[current][2], uniqueWords[next]]
    if(gram not in gramWords):
        break;
    current = gramWords.index(gram)
    markov.extend([uniqueWords[next]])
print("output: ", " ".join(markov))

import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import numpy

order = 2  # the length of n-grams. Must be integer >= 0
sentenceLength = 50  # how many words the generated output should be
num_of_outputs = 50 # how many different markov chains you want to generate

with open(r'C:\Users\Veerpal\Documents\GitHub\markov\text.txt', 'r') as content_file:
    content = content_file.read()

# generate n grams
allWords = nltk.word_tokenize(content)
gramWords = list(ngrams(allWords, order))
gramWords = [list(elem) for elem in gramWords]

#find all unique words
uniqueWords = []
for word in allWords:
    if word not in uniqueWords:
        uniqueWords.append(word)

#generate transition matrix
rowLength = len(gramWords)
colLength = len(uniqueWords)
print(rowLength, colLength)
transition = numpy.zeros(shape=(rowLength,colLength));

for i in range(order, len(allWords)):
    row = gramWords.index(allWords[i-order:i])
    column = uniqueWords.index(allWords[i])
    transition[row, column] +=1;


# divide element by row sum to get easier probabilities
with numpy.errstate(divide='ignore',invalid='ignore'):
    transition /= transition.sum(axis=1, keepdims=True)

# begin text generation
for chain in range(num_of_outputs):
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
        
        gram = []
        for num in range(1, order):
            gram.append(gramWords[current][num])
        gram.append(uniqueWords[next])

        if(gram not in gramWords):
            break;
        current = gramWords.index(gram)
        markov.extend([uniqueWords[next]])

    #generate output
    output = markov[0]
    characters='.,;?!'
    for word in markov[1:]:
        if word in characters:
            output+=word
        else:
            output+=" " + word
    print("output "+ str(chain+1) + ": ", output)       


# imports
import nltk
import nltk.corpus
from nltk.tokenize import RegexpTokenizer
from gensim.models import Word2Vec, KeyedVectors
from math import sqrt

# Takes in a statement and returns tokens without punctuations while making sense of the words hence "w+"
tokenizer = RegexpTokenizer(r'\w+')

# Expressions to be compared
exp1  = "The king and the queen had three children. Harry, Ron and Ginny were inseparable. Harry was the most fierce man."
exp2  = "The Weasleys also had three children. Draco, Neville and Luna were very strong wizards. Luna was a rather strange woman."

# tokens obtained from expressions
tokens1 = tokenizer.tokenize(exp1)
tokens2 = tokenizer.tokenize(exp2)
# print(tokens1)
# print(tokens2)

# joint vector to be obtain the 
expressions = [exp1, exp2]
expVec = [nltk.word_tokenize(exp) for exp in expressions]
# print(expVec)

# training the model
model = Word2Vec(expVec, min_count=1, size=32)

# Initializing the values
sum1 = 0
sum2 = 0
sumtot = 0
sum_1 = 0
sum_2 = 0
sum1_tot = 0
sum2_tot = 0

# adding up all the vectors of the first and second expression
for token_a, token_b in zip(tokens1, tokens2):
    sum1 += model.wv[token_a]
    sum2 += model.wv[token_b]

# finding the dot product of vectors
for i,j in zip(sum1, sum2):
    sum_1 += i**2
    sum_2 += j**2
    sumtot += i*j
    
# to find the magnitude, we take square root
sum1_tot = sqrt(sum_1)
sum2_tot = sqrt(sum_2)

# final step to find the cosine and display it's value
cosineSim = sumtot/(sum1_tot * sum2_tot)
print(cosineSim)



# Note: The result displayed is cos(x) where x is the angle between the two vectors.
# The more similar the vectors are, the closer to one the value will be.
# This will signify that the angle between the vectors is negligible and hence they are very similar.

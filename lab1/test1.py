from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

p_stemmer = PorterStemmer()
sb_stemmer = SnowballStemmer('english')
sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."
print (sentence)
for token in word_tokenize (sentence):
 print (p_stemmer.stem(token))
 print (sb_stemmer.stem(token))
 print ("---")
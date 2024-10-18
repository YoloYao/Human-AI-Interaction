import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet') # These two lines only need to be run once
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
lemmatiser = WordNetLemmatizer()
sentence = "I am writing a few words, and I am hoping they don't get chopped up too much."
posmap = {
 'ADJ': 'a',
 'ADV': 'r',
 'NOUN': 'n',
 'VERB': 'v'
}
print(sentence)
post = nltk.pos_tag( word_tokenize(sentence), tagset='universal')
print(post)
for token in post :
  word = token[0]
  tag = token[1]
  if tag in posmap.keys() :
    print(lemmatiser.lemmatize(word, posmap[tag]))
  else :
    print(lemmatiser.lemmatize(word))
  print(" ---")
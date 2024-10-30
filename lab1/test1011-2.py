import nltk
n_param = 2
from nltk import word_tokenize, sent_tokenize
from nltk.util import pad_sequence
from nltk.lm import MLE, Laplace
from collections import Counter
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
document = open("data/dataset2.txt", encoding="utf8").read()
# document = "this is a test sentence! And this is another one. And this, is another one again"
tokenized = [word_tokenize(sent) for sent in sent_tokenize(document)]
corpus, vocab = padded_everygram_pipeline(n_param, tokenized)
lm = Laplace(n_param)
lm.fit(corpus, vocab)
print("Size of vocabulary:", str(len(lm.vocab)))
# Let us print all the unigrams and their scores
for vocab_token in lm.vocab:
    score = lm.score(vocab_token)
    print("Unigram: [" + vocab_token + "] : " + str(score))
# Let us print all the bigrams and their scores 
for vocab_token_prev in lm.vocab:
    for vocab_token in lm.vocab:
        score = lm.score(vocab_token, [vocab_token_prev])
        print("Bigram: ["+ vocab_token_prev + ", " + vocab_token + "] : " + str(score))

print(lm.generate(20 , text_seed =['i'], random_seed =1))
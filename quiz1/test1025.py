import numpy as np
import random
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score
import os

import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')


nltk.download('punkt')
nltk.download('stopwords')
np.random.seed(1024)
random.seed(1024)
corpus = [
    "I'm looking for flights to Kuala Lumpur from London Heathrow. What are the cheapest options available in November?",
    "What airlines fly direct to Kuala Lumpur from the UK?",
    "I need to book a flight to Kuala Lumpur for two adults and one child. We'd prefer to fly with British Airways or Malaysia Airlines. What dates have the best prices?",
    "Can you find me a flight to Kuala Lumpur with a layover in Dubai? I'd like to spend a couple of days there on my way.",
    "What's the average flight time from London to Kuala Lumpur? Are there any airlines that offer a faster route?",
    "I'd like to fly to Kuala Lumpur in business class. Can you show me some options with lie-flat seats and good in-flight entertainment?",
    "I need to book a multi-city flight to Kuala Lumpur with a return flight from Singapore. Can you help me with that?",
    "Are there any budget airlines that fly to Kuala Lumpur from Europe? I'm looking for the most affordable option, even if it means a longer journey.",
    "What's the baggage allowance for flights to Kuala Lumpur with Emirates? Can I take a surfboard as checked baggage?",
    "I need to find a flight to Kuala Lumpur that departs after 6pm. I have a meeting in the afternoon and can't leave earlier."]


def jaccard_similarity(doc1, doc2):
    set1 = set(nltk.word_tokenize(doc1))
    set2 = set(nltk.word_tokenize(doc2))
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0
    return intersection / union


# 3. 构建文档-词项矩阵（Term-Document Matrix）
vectorizer = CountVectorizer()  # 或使用其他加权方式，如 TfidfVectorizer
X_counts = vectorizer.fit_transform(corpus)

# 使用 TF-IDF 转换词频矩阵
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X_counts)

query_vector = vectorizer.transform(corpus)
query_tfidf = tfidf_transformer.transform(query_vector)

cosine_similarities = cosine_similarity(query_tfidf, X_tfidf).flatten()

ranked_doc_indices = cosine_similarities.argsort()[::-1]

print("\nTop relevant documents:")
print(ranked_doc_indices[:5])
print(cosine_similarities[0])
# for index in ranked_doc_indices[:5]:
#     print(f"Document {
#           index + 1} (Score: {cosine_similarities[index]:.4f}): {corpus[index]}")

simli = 0
# for index in corpus:
    
print(jaccard_similarity(corpus[0], corpus[1]))
# 示例数组
numbers = [1, 2, 3, 4, 5]

# 初始化总值
total_sum = 0

# 二层循环，遍历每两个数的组合
for i in range(len(corpus)):
    for j in range(i + 1, len(corpus)):
        # 每两个数相加
        total_sum += jaccard_similarity(corpus[0], corpus[1])

print("每两个数相加后的总值:", total_sum)
# python写一段二层循环计算5个对象的数组中每两个数相加后的总值
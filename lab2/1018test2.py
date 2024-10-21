import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')

# 文档预处理


def preprocess_documents(documents):
    ps = PorterStemmer()
    processed_docs = []

    for doc in documents:
        # 分词
        tokens = word_tokenize(doc)
        # 词干提取
        stemmed_tokens = [ps.stem(token)
                          for token in tokens if token.isalpha()]
        processed_docs.append(' '.join(stemmed_tokens))

    return processed_docs


# 1. 数据集
documents = [
    "Natural language processing with Python and machine learning.",
    "Machine learning models can classify data and predict outcomes.",
    "We build a search engine using cosine similarity and NLP.",
    "Information retrieval involves ranking documents by relevance.",
    "Natural language models understand human queries and respond."
]
document = open("data/dataset1.txt", encoding="utf8").read()
# documents.append(document)
# 2. 文档预处理
processed_documents = preprocess_documents(documents)

# 3. 构建文档-词项矩阵（Term-Document Matrix）
vectorizer = CountVectorizer()  # 或使用其他加权方式，如 TfidfVectorizer
X_counts = vectorizer.fit_transform(processed_documents)

# 使用 TF-IDF 转换词频矩阵
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X_counts)

# 4. 处理用户查询并进行检索


def search(query, vectorizer, tfidf_transformer, X_tfidf, documents):
    # 查询预处理
    query_processed = preprocess_documents([query])

    # 查询向量化
    query_vector = vectorizer.transform(query_processed)
    query_tfidf = tfidf_transformer.transform(query_vector)

    # 计算与每篇文档的余弦相似度
    cosine_similarities = cosine_similarity(query_tfidf, X_tfidf).flatten()

    # 对结果进行排序
    ranked_doc_indices = cosine_similarities.argsort()[::-1]

    # 打印排名前 5 的文档
    print(f"Query: {query}")
    print("\nTop relevant documents:")

    for index in ranked_doc_indices[:5]:
        print(f"Document {
              index + 1} (Score: {cosine_similarities[index]:.4f}): {documents[index]}")


# 5. 测试查询
# query = "machine learning and NLP"
# search(query, vectorizer, tfidf_transformer, X_tfidf, documents)
stop = False
while not stop:
    query = input("Enter your query , or STOP to quit , and press return : ")

    if query == "STOP":
        stop = True
    else:
        print(f'You are searching for { query }')
        search(query, vectorizer, tfidf_transformer, X_tfidf, documents)

# 6.评估查询
# 模型返回的文档索引（假设返回的是排序后的前 3 个文档）
retrieved_doc_indices = [1, 2, 3]  # 模型认为文档 1, 2, 3 相关

# 实际与查询相关的文档索引
relevant_doc_indices = [1, 2, 4]  # 实际上文档 1, 2, 4 相关

# 生成二进制的相关性向量
# 假设文档集合大小为 5，则需要生成长度为 5 的二进制向量表示每个文档是否相关
num_documents = 5

# 模型返回的结果的二进制表示（1 表示相关，0 表示不相关）
y_pred = [1 if i in retrieved_doc_indices else 0 for i in range(num_documents)]

# 实际相关文档的二进制表示
y_true = [1 if i in relevant_doc_indices else 0 for i in range(num_documents)]

# 计算精确率和召回率
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
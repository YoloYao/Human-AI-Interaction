from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 示例数据和向量化器
corpus = ["I love programming.", "Python is a great language.", "Data science is fascinating."]
vectorizer = TfidfVectorizer()
vector_data = vectorizer.fit_transform(corpus)  # 原有的向量矩阵

# 用户输入
user_input = "I love data science."

# 将用户输入进行向量化
input_vector = vectorizer.transform([user_input])

# 打印输入内容的特征权重值
input_features = vectorizer.get_feature_names_out()
input_vector_array = input_vector.toarray()[0]

print("Input vector weights:")
for feature, weight in zip(input_features, input_vector_array):
    if weight > 0:
        print(f"{feature}: {weight:.4f}")

# 计算输入向量与原有向量矩阵的相似度
similarities = cosine_similarity(input_vector, vector_data)

# 打印每个向量的相似度
print("\nSimilarities with original vectors:")
for i, score in enumerate(similarities[0]):
    print(f"Similarity with document {i}: {score:.4f}")
from sklearn.feature_extraction.text import CountVectorizer

# 训练数据
train_data = ["This is a book", "That book is nice"]

# 测试数据
test_data = ["I like this book", "This book is amazing"]

# 对训练数据使用 fit_transform
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(train_data)  # 学习词汇表并转换

# 对测试数据使用 transform
X_test_counts = vectorizer.transform(test_data)  # 仅转换，不重新学习词汇表

print("训练集向量:\n", X_train_counts.toarray())
print("测试集向量:\n", X_test_counts.toarray())

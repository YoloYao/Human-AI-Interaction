from urllib import request
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn . linear_model import LogisticRegression
from nltk.stem.snowball import PorterStemmer
from sklearn . metrics import accuracy_score, f1_score, confusion_matrix
import os
from sklearn.model_selection import train_test_split
import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

doc_urls = {
    "Russia": "http://www.gutenberg.org/cache/epub/13437/pg13437.txt",
    "France": "http://www.gutenberg.org/cache/epub/10577/pg10577.txt",
    "England": "http://www.gutenberg.org/cache/epub/10135/pg10135.txt",
    "USA": "http://www.gutenberg.org/cache/epub/10947/pg10947.txt",
    "Spain": "http://www.gutenberg.org/cache/epub/9987/pg9987.txt",
    "Scandinavia": "http://www.gutenberg.org/cache/epub/5336/pg5336.txt",
    "Iceland": "http://www.gutenberg.org/cache/epub/5603/pg5603.txt"
}
documents = {}
for country in doc_urls.keys():
    content = request.urlopen(doc_urls[country]).read().decode(
        'utf-8', errors='ignore')
    documents[country] = content
all_text = documents.values()


# 1.构建词频矩阵
count_vect = CountVectorizer(
    stop_words=stopwords.words('english'), ngram_range=(1, 2))
X_train_counts = count_vect.fit_transform(all_text)
tf_transformer = TfidfTransformer(
    use_idf=True, sublinear_tf=True).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf)

# 2.词频矩阵构建，调用词干提取
# p_stemmer = PorterStemmer()
# analyzer = CountVectorizer().build_analyzer()


# def stemmed_words(doc):
#     return (p_stemmer.stem(w) for w in analyzer(doc))


# stem_vectorizer = CountVectorizer(analyzer=stemmed_words)
# print(stem_vectorizer.fit_transform(
#     ['This sentence should get seriously mangled in the stemming process , but it is fine.']))
# print(stem_vectorizer.get_feature_names_out())

# 3.划分测试集
label_dir = {
    "positive": "data/positive",
    "negative": "data/negative"
}

data = []
labels = []

# for label in label_dir.keys():
#     for file in os.listdir(label_dir[label]):
#         filepath = label_dir[label] + os.sep + file
#         with open(filepath, encoding='utf8', errors='ignore', mode='r') as review:
#             content = review.read()
#             data.append(content)
#             labels.append(label)

# X_train, X_test, y_train, y_test = train_test_split(
#     data, labels, test_size=0.25, random_state=1)
# count_vect = CountVectorizer(stop_words=stopwords.words('english'))
# X_train_counts = count_vect.fit_transform(X_train)
# tfidf_transformer = TfidfTransformer(
#     use_idf=True, sublinear_tf=True).fit(X_train_counts)
# X_train_tf = tfidf_transformer.transform(X_train_counts)
# classifier = LogisticRegression(random_state=0).fit(X_train_tf, y_train)
# X_new_counts = count_vect.transform(X_test)
# X_new_tfidf = tfidf_transformer.transform(X_new_counts)
# predicted = classifier.predict(X_new_tfidf)
# # 评估模型准确度
# print(confusion_matrix(y_test, predicted))
# print(accuracy_score(y_test, predicted))
# print(f1_score(y_test, predicted, pos_label='positive'))
# print(X_train_tf)

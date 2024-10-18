import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
from gensim.models import Word2Vec
from nltk.corpus import gutenberg
import nltk

# 下载和加载语料库
nltk.download('gutenberg')
sentences = gutenberg.sents('austen-emma.txt')  # 将文本分成句子

# 训练 Word2Vec 模型
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# 查看某个词的词向量
print(model.wv['Emma'])

# 找出与某个词最相关的词
print(model.wv.most_similar('Emma'))

# 保存模型到文件
model.save("module/word2vec.model")

# 或者只保存词向量
model.wv.save("module/word2vec.wordvectors")
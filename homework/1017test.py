import pickle
import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
import nltk
from nltk.util import ngrams
from collections import Counter

# 下载示例语料库
nltk.download('gutenberg')
from nltk.corpus import gutenberg

# 从语料库加载文本
text = gutenberg.words('austen-emma.txt')  # 使用简·奥斯汀的《艾玛》作为示例语料库

# 生成三元组 n-gram (三元模型)
trigrams = list(ngrams(text, 3))

# 计算 n-gram 的频率
trigram_freq = Counter(trigrams)

# 打印最常见的 5 个 n-gram
print(trigram_freq.most_common(5))

with open('ngram_model.pkl', 'wb') as f:
    pickle.dump(trigram_freq, f)
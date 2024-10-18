import pickle

# 从文件中加载 n-gram 频率模型
with open('ngram_model.pkl', 'rb') as f:
    trigram_freq = pickle.load(f)

# 使用模型
print(trigram_freq.most_common(50))
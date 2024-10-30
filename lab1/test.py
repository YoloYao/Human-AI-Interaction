# 
import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
import nltk
nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()
# 
# 下载网页内容
# from urllib import request
# url = "http://example.org"
# raw = request.urlopen(url).read().decode('utf-8')
# print(raw)
# 
# 下载网页内容
# import nltk
# from urllib import request
# url = "http://www.gutenberg.org/files/84/84-0.txt"
# content = request.urlopen(url).read().decode('utf-8', errors = 'ignore')
# print(content)
# 
# 
# with open ('newfile.txt ', 'r', encoding ='utf-8') as f:
#     for line in f :
#       print(line)
# import nltk

# 下载停用词
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# 
# text = " Artificial intelligence is cool but I am not too keen on Skynet ."
# text_tokens = word_tokenize(text)
# tokens_without_sw = [word.lower() for word in text_tokens if not word in stopwords.words()]
# print(tokens_without_sw)
# filtered_sentence = (" ").join(tokens_without_sw)
# print(filtered_sentence )
# text = nltk.Text(tokens_without_sw)
# print(text)
# print('hello')

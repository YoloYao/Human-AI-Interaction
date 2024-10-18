import os
# with open('data/dataset1.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)

document_path = "data"
corpus = {}
for file in os.listdir(document_path):
    filepath = document_path + os.sep + file
    with open(filepath, encoding='utf-8', errors='ignore', mode='r') as document:
        content = document.read()
        document_id = file
        corpus[document_id] = content
print('Build corpus finished.')

stop = False
while not stop:
    query = input("Enter your query , or STOP to quit , and press return : ")
    
    if query == "STOP":
        stop = True
    else:
        print(f'You are searching for { query }')       

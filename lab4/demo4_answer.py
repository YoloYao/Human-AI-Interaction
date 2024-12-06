import random

def calculate_similarity(query, known_responses):
    """
    模拟计算用户输入与已知回答的相似度。
    返回相似度分数（0-1之间）。
    """
    return random.uniform(0, 1)  # 模拟一个相似度分数

def google_search(query):
    """
    模拟通过搜索引擎获取结果。
    如果搜索成功，则返回模拟结果，否则返回None。
    """
    simulated_results = ["Here is a related article I found.", "This might help: example.com/article"]
    return random.choice(simulated_results) if random.random() > 0.5 else None

def get_alternative_answer(query, known_responses, threshold=0.7):
    """
    根据用户查询返回最佳答案，如果相似性低于阈值则提供可替代答案。
    """
    similarity = calculate_similarity(query, known_responses)
    print(f"Similarity score: {similarity:.2f}")

    if similarity > threshold:
        # 从已知回答中随机选择一个匹配的答案（假设有多个可能答案）
        return random.choice(known_responses)
    else:
        # 如果相似度低于阈值，尝试通过搜索获取答案
        google_result = google_search(query)
        if google_result:
            return google_result
        else:
            return "I can't find what you're looking for. Please try rephrasing your question."

# 示例运行
known_responses = [
    "The capital of France is Paris.",
    "The square root of 16 is 4.",
    "Water boils at 100 degrees Celsius."
]

print("Ask me anything!")
user_query = input()

# 获取答案
answer = get_alternative_answer(user_query, known_responses)
print(f"Response: {answer}")

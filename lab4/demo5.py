def compare_intent(user_input, intent_threshold=0.7):
    """
    模拟意图匹配，返回与用户输入最相关的意图和对应的响应。
    """
    # 模拟意图库
    intent_responses = {
        "feelings_user_positive": "I'm glad to hear that! Keep up the positivity!",
        "feelings_user_negative": "I'm sorry to hear that. I'm here to listen if you want to talk.",
        "neutral": "I see. Feel free to share more about it.",
    }

    # 模拟匹配分数
    intent_scores = {
        "feelings_user_positive": 0.8,  # 假设匹配分数
        "feelings_user_negative": 0.6,
        "neutral": 0.5,
    }

    # 根据分数和阈值匹配意图
    matched_intent = max(intent_scores, key=intent_scores.get)
    if intent_scores[matched_intent] >= intent_threshold:
        return matched_intent, intent_responses[matched_intent]
    else:
        return "neutral", intent_responses["neutral"]

def handle_user_feelings(chatbot_name="Chatbot"):
    """
    根据用户输入的情绪生成个性化响应。
    """
    print(f"{chatbot_name}: How are you feeling today?")
    user_input = input("You: ").strip().lower()

    # 调用意图匹配函数
    intent_feelings = compare_intent(user_input)

    # 根据意图生成相应的回应
    if "feelings_user_positive" in intent_feelings[0]:
        print(f"{chatbot_name}: {intent_feelings[1]}")
    elif "feelings_user_negative" in intent_feelings[0]:
        print(f"{chatbot_name}: {intent_feelings[1]}")
    else:
        print(f"{chatbot_name}: {intent_feelings[1]}")

# 测试运行
handle_user_feelings()

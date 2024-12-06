def read_available_options(option_type):
    """
    模拟读取可用选项，例如酒店列表或其他服务。
    """
    options = {
        "hotel": ["Hotel A", "Hotel B", "Hotel C"],
        "accommodation": ["Apartment X", "Villa Y", "Hostel Z"]
    }
    return options.get(option_type, [])

def suggest_alternatives(user_input, similarity_index, threshold=0.7):
    """
    根据用户输入和相似度提供推荐，并提示其他可用选项。
    """
    print(f"Similarity index: {similarity_index:.2f}")
    
    if similarity_index < threshold:
        # 根据输入的关键词推荐相关选项
        if "hotel" in user_input or "accommodation" in user_input:
            available_hotels = read_available_options("hotel")
            if available_hotels:
                print("Sorry, we currently only have the following hotels available:\n" + ", ".join(available_hotels))
            else:
                print("Sorry, we don't have any hotels available at the moment.")
        else:
            print("I'm sorry, I couldn't understand your request. Could you try asking about hotels or accommodations?")
    else:
        print("Your input matches well with our services. Proceeding with your request!")

# 主函数模拟用户交互
def discoverable_features_demo():
    print("Welcome! How can I assist you today?")
    user_input = input("You: ").strip().lower()

    # 模拟相似度计算（实际中可能是 NLP 模型输出）
    from random import uniform
    similarity_index = uniform(0.5, 1.0)  # 模拟一个随机相似度分数

    # 提供可发现性建议
    suggest_alternatives(user_input, similarity_index)

# 测试运行
discoverable_features_demo()

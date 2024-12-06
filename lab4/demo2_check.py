def validate_input(answer, seats_reserve, seats_in_row, chatbot_name="Chatbot"):
    """
    验证用户输入是否符合预期的要求
    """
    if answer.isdigit():
        print(f"{chatbot_name}: Your answer should not be a number!")
    elif answer == '':
        print(f"{chatbot_name}: Your answer should not be empty!")
    else:
        print(f"{chatbot_name}: Your answer is valid.")

    if not seats_reserve.isdigit() or int(seats_reserve) not in range(1, seats_in_row + 1):
        print(f"{chatbot_name}: Please choose a seat within our cinema (1-{seats_in_row}).")
        return False
    else:
        print(f"{chatbot_name}: Seat {seats_reserve} reserved successfully.")
        return True

# 示例输入
chatbot_name = "CinemaBot"
seats_in_row = 10  # 假设电影院每排有10个座位

print(f"{chatbot_name}: Welcome to the cinema booking system! Please enter a message:")
answer = input()  # 模拟用户输入的消息
print(f"{chatbot_name}: How many seats would you like to reserve?")
seats_reserve = input()  # 模拟用户输入的座位号

# 验证用户输入
if validate_input(answer, seats_reserve, seats_in_row, chatbot_name):
    print(f"{chatbot_name}: Thank you for your input! Proceeding with booking...")
else:
    print(f"{chatbot_name}: Let's try again.")

import random

def detect_confidence(user_input, intent):
    """
    模拟置信度检测函数。
    假设如果用户输入与意图匹配度低于阈值则返回低置信度。
    """
    confidence_threshold = 0.75  # 设置置信度阈值
    confidence_score = random.uniform(0.5, 1.0)  # 模拟置信度分数
    print(f'Detected intent: {intent}, Confidence score: {confidence_score:.2f}')
    return confidence_score >= confidence_threshold, confidence_score

def booking_flow():
    print('Welcome to the booking service! Please enter the number of seats you want to book:')
    user_input = input()
    intent = "book_seats"  # 假设检测到的意图
    is_confident, confidence_score = detect_confidence(user_input, intent)
    
    if not is_confident:
        print(f"I'm not very confident about your input. You said: '{user_input}'. Is this correct? (yes/no)")
        while True:
            reply = input().lower()
            if reply == 'yes':
                break
            elif reply == 'no':
                print('Please re-enter the number of seats you want to book:')
                user_input = input()
                is_confident, confidence_score = detect_confidence(user_input, intent)
                if is_confident:
                    break
                else:
                    print(f"I'm still not confident. You said: '{user_input}'. Is this correct? (yes/no)")
            else:
                print("Please reply with 'yes' or 'no'.")
    
    print('These are your booking details: You have booked ' + str(user_input) +
          ' seat(s). \nIf you are happy to proceed with your booking click enter or type \'cancel\' to cancel your booking.')
    
    while True:
        reply = input()
        if reply == '':
            booking_reference = random.randint(1000, 9999)  # 生成随机预订参考号
            print('Booking confirmed! Booking reference: ' + str(booking_reference))
            break
        elif reply.lower() == 'cancel':
            print('Booking cancelled.')
            break
        else:
            print("Invalid input. Press enter to confirm or type 'cancel' to cancel.")

# 测试运行
booking_flow()

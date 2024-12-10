class TicketBookingBot:
    def __init__(self):
        self.context = {}

    def add_to_context(self, key, value):
        self.context[key] = value

    def get_response(self, user_input):
        # 检查上下文中是否已经存储了一些信息
        if "book a ticket" in user_input.lower():
            response = "Sure! Where would you like to go?"
        elif "to" in user_input.lower() and "destination" not in self.context:
            destination = user_input.split("to")[-1].strip()
            self.add_to_context("destination", destination)
            response = f"Got it! Traveling to {destination}. When do you want to leave?"
        elif "at" in user_input.lower() and "departure_time" not in self.context:
            departure_time = user_input.split("at")[-1].strip()
            self.add_to_context("departure_time", departure_time)
            response = f"Leaving at {departure_time}. How many tickets would you like?"
        elif user_input.isdigit() and "num_tickets" not in self.context:
            num_tickets = int(user_input)
            self.add_to_context("num_tickets", num_tickets)
            response = f"Booking {num_tickets} ticket(s) to {self.context['destination']} at {self.context['departure_time']}. Is that correct?"
        elif "yes" in user_input.lower():
            response = "Great! Your tickets are booked. Thank you!"
            # 清空上下文，模拟结束会话
            self.context.clear()
        elif "no" in user_input.lower():
            response = "Okay, let's start over. Where would you like to go?"
            # 重新开始对话
            self.context.clear()
        else:
            response = "I'm here to help with booking your ticket. Please provide the necessary details."

        return response

# 使用示例
bot = TicketBookingBot()
print(bot.get_response("I want to book a ticket"))           # 用户开始预订
print(bot.get_response("to Paris"))                          # 用户指定目的地
print(bot.get_response("at 5 PM"))                           # 用户指定出发时间
print(bot.get_response("2"))                                 # 用户指定票数
print(bot.get_response("yes"))                               # 用户确认预订
class ShoppingProgress:
    """
    模拟一个购物进度类，用于跟踪用户的购物状态和剩余步骤。
    """
    def __init__(self, total_steps):
        self.total_steps = total_steps
        self.current_step = 0

    @property
    def steps_remaining(self):
        return self.total_steps - self.current_step

    @property
    def completed(self):
        return self.current_step >= self.total_steps

    def advance_step(self):
        if not self.completed:
            self.current_step += 1
            print(f"Step {self.current_step} completed!")
        else:
            print("You have already completed all steps.")

def track_shopping_progress():
    """
    主函数，用于跟踪用户购物的上下文和进度。
    """
    print("Welcome to the shopping assistant! Let's track your shopping progress.")
    total_steps = int(input("Enter the total number of steps to complete your shopping: "))
    shopping = ShoppingProgress(total_steps)

    while not shopping.completed:
        print(f"There are {shopping.steps_remaining} steps remaining to complete your shopping.")
        action = input("Type 'next' to move to the next step or 'quit' to stop: ").strip().lower()

        if action == 'next':
            shopping.advance_step()
        elif action == 'quit':
            print("Shopping progress saved. See you next time!")
            break
        else:
            print("Invalid input. Please type 'next' or 'quit'.")

    if shopping.completed:
        print("All done! Ready to check out?")

# 测试运行
track_shopping_progress()

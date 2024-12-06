def collect_children_data():
    """
    收集孩子的年龄数据，允许用户输入年龄或跳过。
    """
    have_children = True
    child_string = ""
    count = 0  # 用于跟踪第几个孩子

    print("Welcome! Please enter the age of your children. Type 'skip', 'no', or 'none' to indicate no children.")

    while have_children:
        child_input = input("What is the age of the child? Or type 'skip' to finish: ").strip().lower()

        # 处理用户选择跳过或没有孩子
        if child_input in ["skip", "no", "none"]:
            have_children = False
            print("No more children to add. Thank you!")
        
        # 处理输入的孩子年龄
        elif child_input.isdigit():
            if count < 1:
                child_string += f"1_{child_input}"
            else:
                child_string += f" 2C{count}_{child_input}"
            count += 1
            print(f"Child {count} added with age: {child_input}")
        
        # 无效输入处理
        else:
            print("Sorry! I don't understand. Please provide the age of the child in numbers or type 'skip'.")
    
    # 返回收集的孩子数据
    return child_string

# 示例运行
child_data = collect_children_data()
print(f"Collected child data: {child_data}")
